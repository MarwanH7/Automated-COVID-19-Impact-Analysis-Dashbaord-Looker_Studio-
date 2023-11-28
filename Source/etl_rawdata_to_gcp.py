
from pathlib import Path
import pandas as pd 
from prefect import task, flow
from prefect_gcp import GcpCredentials, GcsBucket
import numpy as np


## First task is to fetch the data and return it as a pandas dataframe
@task(log_prints = True, retries = 2) 
def fetch(dataset_url: str) -> pd.DataFrame:
    """ Read raw covid data from url into pandas dataframe"""
    df = pd.read_csv(dataset_url)
    return df 


## Second task is to clean that dataframe and return a clean dataframe
@task(log_prints=True)
def clean(df=pd.DataFrame) -> pd.DataFrame:
    """Clean dataset"""
    ## Date to datetime
    df.date= pd.to_datetime(df.date)
    ## Replacing nan in float columns to zero for SQL compatibility
    float_columns = df.select_dtypes(include=np.float).columns
    df[float_columns] = df[float_columns].fillna(0)
    ## Checking for null values
    nan_values = df[float_columns].isna().sum()
    print(f"Column NAN = {nan_values}")
    ## Drop duplicates
    df.drop_duplicates(inplace=True)
    ## Rename column
    df.rename(columns={"location": "country"}, inplace=True)
    print(f"columns: {df.dtypes}")
    print(f"The latest date: {df['date'].max()}")
    return df


## Write out the dataframe locally 

@task()
def write_local(df: pd.DataFrame, dataset_file: str) -> Path:
    """Write DataFrame out locally as parquet file"""
    
    #path = Path(f"{dataset_file}.parquet")
    path = Path(f"Data{dataset_file}.parquet")
    if not path.parent.is_dir():
        path.parent.mkdir(parents=True)
    path = Path(path).as_posix()
    df.to_parquet(path)
    return path


## Load the dataframe into google cloud storage (lake)
@task()
def write_gcs(path: Path) -> None:
    """Upload local parquet file to GCS"""
    gcs_block = GcsBucket.load("covid-dash-data")
    #gcs_block.upload_from_path(from_path=path, to_path= "path")
    gcs_block.upload_from_path(from_path=path, to_path= "../data/")
    return

## Main ETL Function 
@flow()
def rdata_to_gcs() -> None:
    """The main ETL function"""
    dataset_file = "covid-data"
    dataset_url = f"https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-{dataset_file}.csv"
    #Fetch function returns the df from url and creates a variable df 
    df = fetch(dataset_url)
    # Clean function returns the cleaned df and creates a variable df_clean
    df_clean = clean(df)
    # Write local function returns the path to the parquet file and creates a variable path
    path = write_local(df_clean, dataset_file)
    #test_dataframe_schema(path)
    write_gcs(path)



if __name__ == "__main__":
    rdata_to_gcs()

