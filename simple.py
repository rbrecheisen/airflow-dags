import datetime as dt

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator


with DAG(
        dag_id='simple',
        description='Simple DAG that connects to XNAT',
        start_date=dt.datetime(2021, 6, 1),
        schedule_interval="@daily",
) as dag:
    connect = DockerOperator(
        task_id='connect',
        image='brecheisen/simple-connect:latest',
        command='connect.py',
    )
