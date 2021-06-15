import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator
from tasks.simple import _connect_to_irods


with DAG(
        dag_id='irods_to_xnat',
        description='Simple DAG that connects to IRODS',
        start_date=dt.datetime(2021, 6, 15),
) as dag:
    connect_to_irods = PythonOperator(
        task_id='connect_to_irods',
        python_callable=_connect_to_irods,
    )
