
# [Automated COVID-19 Impact Analysis Dashboard](https://lookerstudio.google.com/u/0/reporting/548774be-64bd-4723-9ecf-5298514072e6/page/XpNkD?s=kDIHNCaHr9M)


## Overview
<div align="justify">
  
**Project Objective**: This project is the second iteration of a manual Covid-19 impact analysis dashboard. It aims to automate the process by creating a full data pipeline. The pipline leverages Google Cloud services to create a seamless process for extracting, loading, transforming, and visualizing important COVID-19 metrics and leveraging Terraform (IaC) to manage those cloud resourcs. The initial metrics the dashboard analyzes are cases, deaths, vaccinations and their respective rates. The data can be queried and visualized globally, per continent and per country. Which gives the user the ability to drill down into the data, from general to specific. The initial manual dashboard repo can be found [here](https://github.com/MarwanH7/COVID-19-Impact-Analysis-Dashbaord/tree/main)

**Target Audience (clients)**: This project has a wide range of clients who would want to make data-driven decisions, here are some example industries:

- **Hospital Administrators and Healthcare Facilities**: Provides insights for hospitals, healthcare professionals, and public health agencies to keep an eye on important metrics, which can potentially helps in resource allocation, understanding disease spread, and vaccine distribution strategies allowing the user to adjust their policies and protocols accordingly.
  
- **Government Health Departments and Policy Makers**: Assists policymakers in understanding the impact of measures taken, predicting disease trends, and making informed decisions on public health policies and interventions.
  
- **Hospitality & Tourism**: Aids industry professionals in monitoring travel advisories, understanding the impact of COVID-19 on travel behavior, and making informed decisions regarding operational strategies and marketing campaigns.

    
## Readme.md Content 

* Extract,Load,Transform (ELT) Overview
* Flow Diagram
* Full Pipeline step by step 
* Reproducibility 
* Features to add in the next iteration
* Aknowledgments

## ELT Overview 

- **Data Pipeline Automation:**
  
  -  Google Cloud Platform is used as the cloud provider.
  -  Terraform (IaC) is used to manage all the resources on the cloud platform.
  -  The raw data is extracted from Our [World In Data data set](https://github.com/owid/covid-19-data).
  -  The data is then loaded to Google Cloud Storage for initial processing (casting,nulls).
  -  The data is then moved from Google Cloud storage bucket to a BigQuery data warehouse for processing.
  -  Using dbt the data is transformed and specific desired columns are queried for the dashboard.
  -  These 6 steps are all scheduled and ran without the need of the user/client. 
 
- **Dashboard Creation:**
  
  -  The final tables are accessed by connecting directly from BigQuery to Google Looker studio for visualizations.


## Flow Digram 


![Flow_Diagram](https://github.com/MarwanH7/Automated-COVID-19-Impact-Analysis-Dashbaord-Looker_Studio-/assets/56262986/9fc357e5-642b-4a42-b847-18b504086dc5)



## Full Pipeline Step by Step 


  
1. **Data Source:** 
<div align="justify">
    
  The raw data is extracted from [World In Data data set](https://github.com/owid/covid-19-data) which collects and combines the data from different sources such as Johns Hopkins University and WHO and made available to the public at this github repository [here](https://github.com/owid/covid-19-data)

2. **Setting up Google cloud resources with Terraform**
  Two main files to setup terraform
    
    * **'main.tf'** file in the '/Infrastructure' directory contains configurations for provisioning resources on Google Cloud Platform (GCP). I have the google cloud data lake bucket and the BiQuery data warehouse. Users can modify this file to suit their infrastructure requirements, altering variables such as region, project, adding a VM instance depending on the type they require etc.
    *  **variables.tf**: This has all the variables defined that are used by main.tf such as project, region, storage_class, Table_names etc.

3. **Prefect workflow orchestration**: 

  Prefect is an orchestration for data intensive workflow pipelines. Using @flows that contain @tasks and a great UI that keeps track, schedules, sends notifications for all your python scripts. Since I decided to use use the [Medallion Architecture](https://www.databricks.com/glossary/medallion-architecture#:~:text=A%20medallion%20architecture%20is%20a,Silver%20%E2%87%92%20Gold%20layer%20tables)  for data flow, prefect allowed me to schedule each step using cron, and progressively improve the structure and quality of data as it flows throught the pipeline. 
  
  **Prefect set up**
  
  1. Deployment building of .py scripts.
  2. Creating a .yaml file for script 
  3. Deployment apply that .yaml file 
  
  **My Deployments**
  
  1. Raw Data to Google Cloud Storage
  2. Google Cloud Storage To Bigquery
  3. Bigquery dbt Staging Model
  4. Bigquery dbt Production model


![Deployments](https://github.com/MarwanH7/Automated-COVID-19-Impact-Analysis-Dashbaord-Looker_Studio-/assets/56262986/dc952744-f4ae-45f4-8475-a479e1106251)


4. **dbt models:** 
  For modelling I used Kimballs Dimensional Modeling, which takes advantage of having a staging area, then a production one. Within the /Source/dbt directory:
  
  **Set up:**
  
  dbt_project.yml file:contains configurations for the DBT project
  
  **staging model:** Scripts for the staging data model reside in this section, it applies some transformations to desired column names based on understanding of the data during the EDA step. As well as some casting to make sure data types for the schema are correct. 
  
  **production model:** Scripts for the production data model reside in this section, it queries specifc columns and aggregates such as cases, deaths, vaccinations and their respective rates for the dashboard. 
  

5. **Looker Studio Dashboard:** 

Dashboard diagram and link to looker dash. Be sure to adjust the date selection at the top right of the dashboard to reflect the numbers correctly. The start date is Jan 1 2020.


<img width="1785" alt="Dashboard" src="https://github.com/MarwanH7/Automated-COVID-19-Impact-Analysis-Dashbaord-Looker_Studio-/assets/56262986/31987da6-38b4-4605-9f4f-6c2a79831ad3">



## Project Structure
- **`/Infrastructure`:** Scripts for terraform resource creation.
- **`/Source`:** Prefect work flow orchestration scripts and deployment files 
- **`/Source/dbt`:** Staging and production model scripts


## Reproducibility 
1. Clone this repo locally or on your VM.
2. Create an env and pip install the requirements.txt file.
3. Edit the terraform variables.tf and main.tf to create your desired resources.
4. Create/edit the prefect orchestration scripts to fit your own project design.
5. Create/edit the dbt scripts to fir your own project design (I used Kimballs Dimensional Modeling & Medallion Architecture for data flow).
6. Connect from looker studio to the bigquery data set to create your visulizations. 

## Features to add in the next iteration 
* CI/CD pipeline using GitHub Actions (schema tests, staging model test, function consistency)
* Use NLP to write reports automatically to the column in the lookder dashboard to summarize the updates in the metrics
* Implement triggers, automations, and notifications instead of set scheduled models to the pipeline to make it more robust 

## Acknowledgements

A lot of the knowledge used to automate my dashboard was from going throught the course material of [DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp). Such an amazing community, definitly recommend checking out their material ! 



## Contributors
- [Marwan. E]

