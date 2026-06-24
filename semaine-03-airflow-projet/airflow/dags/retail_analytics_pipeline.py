"""
DAG bootcamp — Pipeline retail analytics TPCH

Orchestre les transformations dbt sur Snowflake :
  dbt run → dbt test

À configurer :
  - Variable Airflow DBT_PROJECT_DIR (chemin projet dbt)
  - profiles.yml accessible dans le conteneur (~/.dbt/profiles.yml)
"""

from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

DBT_PROJECT_DIR = "/opt/dbt/ae_bootcamp"
DBT_PROFILES_DIR = "/opt/airflow/.dbt"

default_args = {
    "owner": "ae_bootcamp",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="retail_analytics_pipeline",
    default_args=default_args,
    description="dbt run + dbt test sur modèles TPCH retail",
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["bootcamp", "dbt", "tpch"],
) as dag:

    start = EmptyOperator(task_id="start")

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"""
            cd {DBT_PROJECT_DIR} &&
            dbt deps &&
            dbt run --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=f"""
            cd {DBT_PROJECT_DIR} &&
            dbt test --profiles-dir {DBT_PROFILES_DIR}
        """,
    )

    end = EmptyOperator(task_id="end")

    start >> dbt_run >> dbt_test >> end
