Overview:
For our final project, we plan to investigate if higher education degrees are beneficial around the world. We plan to gather data from around the world and see if countries with higher college enrollment rates have lower unemployment rates. We will look into unemployment rates from the past 10 years, alongside college degree rates globally. To accomplish our goal, we will combine three datasets that discuss countries' unemployment rates, adults from ages 25 to 64 and their highest education levels, and the gross enrollment ratio for each country.
Our project outline will have four main components. We will first clean each dataset by removing empty values, and renaming any columns that we deem fit. For example, this could be renaming values that are abbreviated country names, or have their regions, and then changing them to their corresponding country. After cleaning our data, we will then merge these three datasets by country and year. In order to answer our research questions, we will include relevant summary statistics and data visualizations. Overall, our goal is to identify a correlation between higher education rates and unemployment rates to understand if higher education is a smart financial decision for adults.

Team: Sarah: Overview & Research Questions, Sambhavi:, Anthony: Datasets, Zoe: Timeline/Project Management

Research or Business Question(s): 
1. Is there a correlation between higher education rates and lower unemployment rates?
2. Within the past 10 years, has the relationship between higher education and unemployment changed?
3. Do the United States' college enrollments compare to other countries?
4. Can we identify employment and higher education outliers? 

Datasets: 
The first dataset was created by the International Monetary Fund (IMF), through its World Economic Outlook report, which consists of economic indicators for each country annually. Created during the biannual WEO exercise, this dataset contains a list of countries and their unemployment rates from 2017 to 2026. This dataset will serve as the outcome variable to measure unemployment and examine the relationship between education and unemployment rate for each country reported.
  
The second dataset is derived from The Organisation for Economic Co-Operation and Development, through its Education at a Glance statistics, with the purpose of measuring the distribution of adults from the age of 25 to 64 by their highest level of education attained. The dataset itself is separated into different time periods, with most of the entries in 2025. Each row of observation is a country, and the percentage of adults that attained: below upper secondary education, upper secondary or post secondary non-tertiary education, and tertiary education. The first column, below upper-secondary, includes no formal education to high school graduation. The second column, upper-secondary or post-secondary non-tertiary includes high school to certain vocational or technical programs that do not qualify for higher education. Finally, the third column of tertiary education includes bachelor’s, master’s, doctor’s degrees and equivalent programs. This dataset will provide the main education variables that allows us to test whether countries with higher educational attainment have lower unemployment rates. 

The final dataset is obtained from the World Bank Group and it measures gross enrollment ratio for each country reported for the year 2025. The gross enrollment ratio is the total number of students enrolled in higher education, compared with the population of the age group expected to attend higher education. Since this ratio counts students of all ages, the enrollment ratio could exceed 100% if older adults return to school or student repeat years. This dataset will provide a complementary education indicator that can help examine the relationship between higher education and changes in unemployment. 

We can integrate these datasets to answer our research question of the relationship between education and unemployment rate by using country and year as the common identifiers, to capture the unemployment rates, completed level of education, and the participation in higher education. The first dataset will serve as the dependent variable with unemployment rate, while the second and third dataset have independent variables such as the percentage of adults with tertiary education and the gross tertiary enrollment ratio that can reveal associations between the independent variable and the dependent variable.

Timeline

Our team will complete the project in stages, focusing on data acquisition, quality assessment, cleaning, integration, analysis, and documentation. We will divide tasks among all four team members and use GitHub to track our progress and contributions. The timeline may be adjusted based on feedback and data availability.

| Task | Description | Target Completion | Responsible Team Member(s) |
|---|---|---|---|
| **1. Project Plan** | Finalize our research questions, datasets, methodology, and team responsibilities. Submit the project plan through GitHub. | October 22 | All Team Members |
| **2. Data Acquisition & Organization** | Download the IMF, OECD, and World Bank datasets, verify their integrity, review licensing restrictions, and organize files in the repository. | October 29 | Anthony |
| **3. Initial Data Quality Assessment** | Evaluate the datasets for accuracy, completeness, timeliness, and consistency. Identify missing values, duplicates, and differences in country and year coverage. | November 3 | Sambhavi |
| **4. Data Cleaning** | Address missing values, standardize country names and year formats, remove duplicates, and document cleaning decisions. | November 7 | Sarah |
| **5. Data Integration** | Merge the cleaned datasets by country and year, identify unmatched records, and document the integration process. | November 11 | Zoe |
| **6. Post-Integration Quality Assessment** | Evaluate the merged dataset for accuracy, completeness, timeliness, and consistency to verify that the integration was successful. | November 14 | Sambhavi |
| **7. Data Analysis & Visualization** | Calculate summary statistics, examine correlations between higher education and unemployment, identify outliers, and create visualizations comparing countries and trends over time. | November 18 | Sarah, Anthony |
| **8. Workflow Automation & Reproducibility** | Develop separate scripts connected by an automated workflow. Document software dependencies and test that the project runs from data acquisition through analysis. | November 21 | Zoe, Anthony |
| **9. Metadata & Documentation** | Create a data dictionary, machine-readable metadata, and documentation covering data sources, licensing, file organization, and reproducibility. | November 24 | Sambhavi, Zoe |
| **10. Final Report & Submission** | Complete the README with our methodology, findings, challenges, and conclusions. Review the project requirements, verify contributions, and create the final GitHub release. | November 30 | All Team Members |

If we find that the datasets do not have enough overlapping countries or years, we will adjust the scope of our analysis. We will also revise our timeline based on project progress and feedback from the interim status report.

Constraints:

One major constraint is that our three datasets differ in country coverage, time periods, and definitions of higher education. The IMF dataset includes unemployment rates from 2017 to 2026, while the OECD dataset focuses on educational attainment among adults aged 25–64 and may not cover every country in the IMF dataset. The World Bank dataset measures gross tertiary enrollment rather than the percentage of adults who have completed a degree. These differences may limit the number of countries and years available after merging the datasets.

Another challenge is handling missing values and inconsistencies, such as different country names, incomplete records, and differences in how education is measured. Additionally, a correlation between education and unemployment does not necessarily mean that higher education causes lower unemployment, since other economic and social factors may influence both. We will also need to review each source's licensing and terms of use to ensure that we can appropriately use and share the data in our public GitHub repository.

Gaps:

We still need to determine how much the three datasets overlap in country coverage and time periods, particularly whether the OECD data provides enough historical observations to answer our question about changes over the past ten years. We also need to confirm whether the World Bank enrollment data supports our intended time frame. If the overlap is limited, we may need to narrow our analysis to the countries and years with sufficient data.

We also need to conduct a formal data quality assessment before deciding how to clean and merge the datasets. This includes identifying missing values, duplicates, inconsistent country identifiers, and potential outliers. Finally, we need to finalize our file organization, data integration strategy, and automated workflow so that our cleaning and analysis can be reproduced. We will also verify the relevant data licenses and document our sources and processing steps.

