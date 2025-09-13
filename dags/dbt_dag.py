import os
from datetime import datetime

# Cosmos (Astronomer) imports
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

# Your dbt project lives here inside the container
# (Windows: C:\Users\xqq_r\dbt-dag\dags\dbt\data_pipeline)
DBT_PROJECT_PATH = "/usr/local/airflow/dags/dbt/data_pipeline"

# Airflow Snowflake connection you will create in Admin -> Connections
SNOWFLAKE_CONN_ID = "snowflake_conn"

# Optional: override dbt binary via env var if needed
DBT_EXECUTABLE = os.environ.get("DBT_EXECUTABLE", "dbt")

# Map Airflow connection -> dbt profile (keep secrets in the connection)
profile_cfg = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id=SNOWFLAKE_CONN_ID,
        profile_args={
            "database": "dbt_db",     # change if needed
            "schema": "dbt_schema",   # change if needed
            # You can also add: "warehouse": "MY_WH", "role": "MY_ROLE"
        },
    ),
)

# Create a DAG that runs your dbt project with Cosmos
dbt_dag = DbtDag(
    dag_id="dbt_dag",
    project_config=ProjectConfig(DBT_PROJECT_PATH),
    profile_config=profile_cfg,
    execution_config=ExecutionConfig(dbt_executable_path=DBT_EXECUTABLE),
    operator_args={
        "install_deps": True,  # install packages from packages.yml if present
    },
    start_date=datetime(2025, 9, 10),
    schedule="@daily",
    catchup=False,
    tags=["dbt", "snowflake", "cosmos"],
)
