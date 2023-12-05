import os
from prefect import flow
from prefect_dbt.cli.commands import DbtCoreOperation

@flow
def dbt_staging_m_run():
    dbt_path = f"{os.getcwd()}/dbt"
    dbt_op = DbtCoreOperation(
        commands=[
            "dbt debug",
            "dbt run --select 'stg_covid'"
        ],
        working_dir=dbt_path,
        project_dir=dbt_path,
        profiles_dir=dbt_path,
    ).run()

if __name__ == "__main__":
    dbt_staging_m_run()

    