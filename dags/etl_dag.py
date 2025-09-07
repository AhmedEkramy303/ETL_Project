from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.insert(0, '/opt/airflow/scripts')
from extract import extract
from transform import transform
from load import load

def extract_task():
    extract()

def transform_task():
    transform()

def load_task():
    load()

with DAG('etl_covid_dag', start_date=datetime(2025,9,7), schedule_interval='@daily', catchup=False) as dag:
    t1 = PythonOperator(task_id='extract', python_callable=extract_task)
    t2 = PythonOperator(task_id='transform', python_callable=transform_task)
    t3 = PythonOperator(task_id='load', python_callable=load_task)

    t1 >> t2 >> t3