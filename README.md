##  ETL Project with Airflow and PostgreSQL
### Project Description / وصف المشروع
**English:**  
ETL pipeline that extracts COVID-19 data from a public API, cleans and transforms it, and loads it into a PostgreSQL database. Fully automated using Apache Airflow.

**العربية:**  
نظام ETL لاستخراج بيانات COVID-19 من API، تنظيفها وتحويلها، ثم تحميلها في قاعدة بيانات PostgreSQL بشكل تلقائي باستخدام Airflow.

### Tech Stack / التقنيات المستخدمة
- Python (pandas, requests)  
- SQL (PostgreSQL)  
- Apache Airflow  
- Docker  
- YAML  

### Project Structure / هيكل المشروع
```
ETL_Project/
├── dags/          # Airflow DAGs
├── scripts/       # ETL scripts: extract, transform, load
├── config.yaml
├── requirements.txt
└── Dockerfile
```

### Installation / طريقة التشغيل
**English:**  
```bash
pip install -r requirements.txt
# Setup PostgreSQL database and user
airflow db init
airflow webserver
airflow scheduler
```

**العربية:**  
```bash
pip install -r requirements.txt
# إعداد قاعدة بيانات PostgreSQL وإنشاء مستخدم
airflow db init
airflow webserver
airflow scheduler
```

### Usage / طريقة الاستخدام
- Runs automatically via Airflow DAG (daily)  
- Loads data into `covid_data` table in PostgreSQL  

### Example Output / مثال على الناتج
| Country | NewConfirmed | TotalConfirmed | NewDeaths | TotalDeaths | Date       |  
|---------|-------------|----------------|-----------|-------------|------------|  
| Egypt   | 150         | 150000         | 5         | 8000        | 2025-09-07 |  

