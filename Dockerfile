FROM apache/airflow:2.7.1-python3.11
COPY scripts/ /opt/airflow/scripts/
COPY dags/ /opt/airflow/dags/
COPY requirements.txt /opt/airflow/
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt