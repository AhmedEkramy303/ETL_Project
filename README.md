# 1️⃣ ETL Project with Airflow and PostgreSQL
# مشروع ETL باستخدام Airflow وPostgreSQL

---

## Project Description / وصف المشروع
**English:**  
This project is an ETL pipeline that extracts COVID-19 data from a public API, cleans and transforms it, and loads it into a PostgreSQL database. The pipeline is fully automated using Apache Airflow.

**العربية:**  
هذا المشروع عبارة عن نظام ETL يقوم باستخراج بيانات COVID-19 من API عام، تنظيف وتحويل البيانات، ثم تحميلها في قاعدة بيانات PostgreSQL. يتم تشغيل النظام بالكامل بشكل تلقائي باستخدام Apache Airflow.

---

## Tech Stack / التقنيات المستخدمة
- Python (pandas, requests) / بايثون (pandas و requests)  
- SQL (PostgreSQL) / SQL (PostgreSQL)  
- Apache Airflow / أباتشي ايرفلو  
- Docker / دوكر  
- YAML / YAML  

---

## Project Structure / هيكل المشروع
ETL_Project/
├── dags/ # Airflow DAGs
├── scripts/ # ETL scripts: extract, transform, load
├── config.yaml # Configuration file
├── requirements.txt
└── Dockerfile

yaml
Copy code

---

## Installation / طريقة التشغيل
**English:**  
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Setup PostgreSQL database and user.

Initialize Airflow database:

bash
Copy code
airflow db init
Start Airflow webserver:

bash
Copy code
airflow webserver
Start Airflow scheduler:

bash
Copy code
airflow scheduler
العربية:

تثبيت المتطلبات:

bash
Copy code
pip install -r requirements.txt
إعداد قاعدة بيانات PostgreSQL وإنشاء مستخدم.

تهيئة قاعدة بيانات Airflow:

bash
Copy code
airflow db init
تشغيل خادم الويب Airflow:

bash
Copy code
airflow webserver
تشغيل Airflow scheduler:

bash
Copy code
airflow scheduler
Usage / طريقة الاستخدام
English:

The ETL pipeline will run automatically according to the Airflow DAG schedule (daily).

Extracted and cleaned data is loaded into the covid_data table in PostgreSQL.

العربية:

سيعمل نظام ETL تلقائيًا وفقًا لجدول DAG في Airflow (يوميًا).

البيانات المستخرجة والمنقحة سيتم تحميلها في جدول covid_data داخل PostgreSQL.

Example Output / مثال على الناتج
Country	NewConfirmed	TotalConfirmed	NewDeaths	TotalDeaths	Date
Egypt	150	150000	5	8000	2025-09-07
