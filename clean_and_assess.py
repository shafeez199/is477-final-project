#!/usr/bin/env python3
Notes:
The raw folder must contain IMF raw data.csv, OECD Raw data.csv,
World Bank Group Raw data.csv. Outputs only the three *_cleaned.csv files.
Keep those raw CSVs outside the cleaned-data folder; they are needed only
when re-running cleaning, not for analysis with the cleaned data.

Missing values stay blank (never imputed); OECD has no reference year;
World Bank gross enrollment ratios may correctly exceed 100; IMF 2025–2026
may contain forecasts (confirm against IMF metadata); educational attainment
and tertiary enrollment are NOT interchangeable measures.
"""
import argparse
import csv
import collections
import re
from pathlib import Path

SOURCE_FILES = {
    "IMF": "IMF raw data.csv",
    "OECD": "OECD Raw data.csv",
    "World Bank": "World Bank Group Raw data.csv",
}
OUTPUT_FILES = {"IMF":"IMF_cleaned.csv", "OECD":"OECD_cleaned.csv", "World Bank":"World_Bank_cleaned.csv"}
MISSING = {"", "..", "NA", "N/A", "NULL", "null", "nan"}
# Aggregate codes observed in the supplied World Bank file. Do not include them
# as country observations; use is_aggregate=false for country-only analyses.
WB_AGGREGATE_CODES = set("""AFE AFW ARB CEB CHI CSS EAP EAR EAS ECA ECS EMU EUU FCV HIC HPC IBD IBT IDA IDB IDX INX LAC LCN LDC LIC LMC LMY LTE MEA MIC MNA NAC OED OSS PRE PSS PST SAS SSA SSF SST TEA TEC TLA TMN TSA TSS UMC WLD""".split())

ALIASES={
 'China, People\'s Republic of':'China', 'China (People’s Republic of)':'China',
 'China (People\'s Republic of)':'China', 'Korea, Republic of':'Korea, Rep.',
 'Korea':'Korea, Rep.', 'Türkiye, Republic of':'Turkiye', 'Türkiye':'Turkiye',
 'Czech Republic':'Czechia', 'Slovak Republic':'Slovak Republic',
 'Egypt, Arab Republic of':'Egypt, Arab Rep.', 'Iran, Islamic Republic of':'Iran, Islamic Rep.',
 'Fiji, Republic of':'Fiji', 'Belarus, Republic of':'Belarus',
 'Azerbaijan, Republic of':'Azerbaijan', 'Armenia, Republic of':'Armenia',
 'Kazakhstan, Republic of':'Kazakhstan', 'Croatia, Republic of':'Croatia',
 'Estonia, Republic of':'Estonia', 'Latvia, Republic of':'Latvia',
 'Lithuania, Republic of':'Lithuania', 'Poland, Republic of':'Poland',
 'Slovenia, Republic of':'Slovenia', 'Moldova, Republic of':'Moldova',
 'Netherlands, The':'Netherlands', 'North Macedonia, Republic of':'North Macedonia',
 'Uzbekistan, Republic of':'Uzbekistan', 'Serbia, Republic of':'Serbia',
 'Andorra, Principality of':'Andorra', 'Bahrain, Kingdom of':'Bahrain',
 'Liechtenstein, Principality of':'Liechtenstein', 'San Marino, Republic of':'San Marino',
 'São Tomé and Príncipe, Democratic Republic of':'Sao Tome and Principe',
 'Aruba, Kingdom of the Netherlands':'Aruba',
 'Hong Kong Special Administrative Region, People\'s Republic of China':'Hong Kong SAR, China',
 'Macao Special Administrative Region, People\'s Republic of China':'Macao SAR, China',
 'Venezuela, República Bolivariana de':'Venezuela, RB',
 'Vietnam':'Viet Nam', 'Russian Federation':'Russian Federation',
 'Kosovo, Republic of':'Kosovo', 'Puerto Rico':'Puerto Rico',
 'Taiwan Province of China':'Taiwan Province of China',
}


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames, list(reader)


def cleaned_number(raw):
    val = (raw or "").strip()
    if val in MISSING:
        return ""
    # Keep a nonnumeric value visibly unchanged for auditing, not silently coerced.
    if re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[Ee][+-]?\d+)?", val):
        return str(float(val))
    return val


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", default=".")
    parser.add_argument("--output-dir", default=".")
    args = parser.parse_args()
    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    raw = {name:read_csv(Path(args.input_dir) / filename) for name,filename in SOURCE_FILES.items()}
    wb_names = {row["Country Name"] for row in raw["World Bank"][1]}
    country_sets = {}
    for source, (fields, rows) in raw.items():
        country_field = "Country Name" if source == "World Bank" else "Country"
        fields = [f for f in fields if f] # World Bank has a blank trailing column
        years = [f for f in fields if f.isdigit() and len(f) == 4]
        output_fields = ["country_standardized", "country_original", "country_match_status", "is_aggregate"] + [f for f in fields if f != country_field]
        cleaned = []
        keys_seen = set()
        missing_values = 0
        duplicate_count = 0
        renamed = 0
        for row in rows:
            original = row[country_field].strip()
            standardized = ALIASES.get(" ".join(original.split()), " ".join(original.split()))
            renamed += original != standardized
            is_aggregate = (source == "World Bank" and row.get("Country Code") in WB_AGGREGATE_CODES) or (source == "OECD" and original in {"OECD", "G20", "European Union (25 countries)"}) or (source == "IMF" and (original in {"G7", "Advanced Economies", "Euro Area (EA)"} or original.startswith("Other Advanced Economies")))
            key = (standardized,) if source == "OECD" else (standardized, row.get("Indicator Code", row.get("Indicator", "")))
            if key in keys_seen:
                duplicate_count += 1
                continue
            keys_seen.add(key)
            cleaned_row = {
                "country_standardized": standardized,
                "country_original": original,
                "country_match_status": "reference_name" if source == "World Bank" else ("matched_world_bank_name" if standardized in wb_names else "not_in_world_bank_reference"),
                "is_aggregate": str(bool(is_aggregate)).lower(),
            }
            for field in fields:
                if field == country_field:
                    continue
                val = (row.get(field) or "").strip()
                if field in years or (source == "OECD" and field != "Country"):
                    missing_values += val in MISSING
                    cleaned_row[field] = cleaned_number(val)
                else:
                    cleaned_row[field] = val
            cleaned.append(cleaned_row)
        with (output / OUTPUT_FILES[source]).open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=output_fields)
            writer.writeheader()
            writer.writerows(cleaned)
        country_sets[source] = {r["country_standardized"] for r in cleaned if r["is_aggregate"] == "false"}
        count_per_year = {y:sum(bool(r[y]) for r in cleaned) for y in years}
        print(f"{source}: {len(rows)} input rows, {len(cleaned)} cleaned; "
              f"{missing_values} missing numeric cells; {duplicate_count} duplicate keys; "
              f"{renamed} standardized country names; years: "
              f"{years[0]+'–'+years[-1] if years else 'not specified'}")
        if source == "World Bank":
            print(f"  Recent coverage (nonmissing): 2024={count_per_year.get('2024')}, 2025={count_per_year.get('2025')}")
        if source == "OECD":
            for r in cleaned:
                vals = [r[f] for f in fields if f != country_field]
                if all(v != "" for v in vals) and abs(sum(float(v) for v in vals)-100)>1:
                    print(f"  Review OECD percentage total: {r['country_original']} = {sum(float(v) for v in vals):.1f}%")
    shared = set.intersection(*country_sets.values())
    print(f"Country names shared across all 3 (excluding known aggregates): {len(shared)}")
    print("Quality notes: OECD contains no year; all missing numeric values remain blank; no imputation performed.")

if __name__ == "__main__":
    main()
