import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator
from irods.session import iRODSSession


def _connect_to_irods():
    print('Connecting to IRODS...')
    session = iRODSSession(
        host='137.120.31.124',
        port=1247,
        user='rods',
        password='irods', zone='nlmumc')
    print(session)


with DAG(
        dag_id='irods_to_xnat',
        description='Simple DAG that connects to IRODS',
        start_date=dt.datetime(2021, 6, 15),
) as dag:

    connect_to_irods = PythonOperator(
        task_id='connect_to_irods',
        python_callable=_connect_to_irods,
    )
