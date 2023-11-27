
# Automated COVID-19 Impact Analysis Dashboard

## Overview
This project aims to automate the data pipeline for COVID-19 impact analysis. It leverages Google Cloud services to create a seamless process for extracting, transforming, and visualizing COVID-19 metrics. This project is the second phase in the creation of an automated data pipeline for COVID-19 impact analysis. It builds upon the manually executed MVP, implementing automation through Google Cloud services. Repo is found [here](https://github.com/MarwanH7/COVID-19-Impact-Analysis-Dashbaord/tree/main)


## Features
- **Data Pipeline Automation:**
  - Utilization of Google Cloud Storage as a data lake for storing raw data.
  - Automated data ingestion into Google BigQuery for data warehousing.
  - Integration of dbt for managing and transforming data tables within BigQuery.

- **Dashboard Creation:**
  - Visualization of insights using Looker Studio, directly connected to the BigQuery dataset.

## Roadmap
1. **Setting Up Data Lake and Data Warehouse with IaC (Infrastructure as Code):**
   - Creating Google Cloud Storage buckets for the data lake using Terraform.
   - Configuring Google BigQuery as the data warehouse through Terraform scripts.

2. **Automation Implementation (CI Step 2):**
   - Building automated data pipelines using Google Cloud services.
   - dbt setup for managing transformations in BigQuery.

3. **Dashboard Creation:**
   - Creating visualizations and dashboards in Looker Studio.

## Usage
- **Setting Up Data Pipelines:** Detailed steps to configure Google Cloud services for automated ETL processes.
- **Accessing the Dashboard:** Instructions for accessing and utilizing the Looker Studio dashboard.

## Project Structure
- **`/Infrastructure`:** Scripts terraform resource creation.
- **`/ETL_scripts`:** Scripts for automated data ingestion and transformation.
- **`/Looker_Dashboard`:** Contains Looker Studio files for the visual dashboard.
- **`/dbt`:** Configuration and transformation files for dbt.

## Getting Started
1. Configure Google Cloud services following the provided instructions.
2. Run the automated scripts to set up the data pipeline.
3. Access the Looker Studio dashboard to visualize the COVID-19 impact metrics.

## Contributors
- [Marwan. E]
