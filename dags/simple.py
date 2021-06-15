import datetime as dt

from airflow import DAG
from airflow.operators.python import PythonOperator
from irods.session import iRODSSession


def _connect_to_irods():
    print('Connecting to IRODS...')
    # Note that the following call ALWAYS returns a session object...
    # Even if IP address is wrong
    session = iRODSSession(
        host='137.120.31.123',
        port=1247,
        user='rods',
        password='irods', zone='nlmumc')
    print(session.collections)


with DAG(
        dag_id='irods_to_xnat',
        description='Simple DAG that connects to IRODS',
        start_date=dt.datetime(2021, 6, 15),
) as dag:

    connect_to_irods = PythonOperator(
        task_id='connect_to_irods',
        python_callable=_connect_to_irods,
    )
