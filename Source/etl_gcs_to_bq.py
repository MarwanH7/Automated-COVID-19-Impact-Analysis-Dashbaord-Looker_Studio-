import os
from pathlib import Path
import pandas as pd 
from prefect import task, flow
from prefect_gcp import GcpCredentials, GcsBucket
import numpy as np


#Extract data from GCS
@task(retries=3)
def extract_from_gcs() -> Path:
    """Download data from GCS"""
    gcs_path = f"Data/covid-data.parquet"
    gcs_block = GcsBucket.load("covid-dash-data")
    gcs_block.get_directory(from_path=gcs_path, local_path=f"../data/")
    return Path(f"../data/{gcs_path}")


#Pandas read parquet file and return dataframe
@task()
def fetch(path: Path) -> pd.DataFrame:
    """Read parquet from GCS"""
    df = pd.read_parquet(path)
    print(f"Shape of the dataframe: {df.shape}")
    print(f"The latest date: {df['date'].max()}")
    return df

# Write dataframe to Big Query in chunks
@task()
def write_bq(df: pd.DataFrame) -> None:
    """Write DataFrame to BiqQuery"""
    ## Load credentials from service account
    gcp_credentials_block = GcpCredentials.load("covid-dashp-credentials")
    ## Using a pandas method to write to Big Query 
    df.to_gbq(
        destination_table=f"Covid_19.Covid_data",
        # location = os.getenv("REGION"),
        project_id=("noble-trainer-406002"),
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="append",
    )

@flow()
def etl_gcs_to_bq(log_prints=True):
    """Main ETL flow to load data into Big Query"""
    ## Extract data from GCS
    path = extract_from_gcs()
    ## Read the data from GCS (PARQUET FILE)
    df = fetch(path)
    ## Write the data to Big Query
    write_bq(df)

if __name__ == "__main__":
    etl_gcs_to_bq()