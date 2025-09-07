# ETL_Project, Data_Warehouse_Project, Real_Time_Kafka_Project
# مشاريع ETL, Data Warehouse و Real-Time Kafka

---

## 1️⃣ ETL Project with Airflow and PostgreSQL
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

---

## 2️⃣ Data Warehouse Project
### Project Description / وصف المشروع
**English:**  
Builds a Data Warehouse with fact and dimension tables for customer sales. Includes ETL scripts to load data and SQL queries for analysis.

**العربية:**  
يبني Data Warehouse يحتوي على Fact و Dimension Tables لمبيعات العملاء، ويشمل سكريبتات ETL لتحميل البيانات واستعلامات SQL للتحليل.

### Tech Stack / التقنيات المستخدمة
- SQL (PostgreSQL)  
- Python (pandas)  
- Jupyter Notebook  

### Project Structure / هيكل المشروع
```
Data_Warehouse_Project/
├── sql/            # SQL scripts: create tables, load data, queries
├── data/           # Sample CSV data
├── notebooks/      # Jupyter Notebook for analysis
├── requirements.txt
└── README.md
```

### Installation / طريقة التشغيل
```bash
pip install -r requirements.txt
# Setup PostgreSQL database
# Run SQL scripts:
# \i sql/create_tables.sql
# \i sql/load_data.sql
# Open Jupyter Notebook
jupyter notebook notebooks/analytics.ipynb
```

### Usage / طريقة الاستخدام
- Run SQL queries to analyze sales by product, customer, or city  
- Use Jupyter Notebook for visual analysis  

---

## 3️⃣ Real-Time Kafka Project
### Project Description / وصف المشروع
**English:**  
Processes real-time sales data using Kafka and Python. Producer generates random data, consumer processes it and stores in PostgreSQL.

**العربية:**  
يعالج بيانات المبيعات في الوقت الحقيقي باستخدام Kafka وPython. يقوم Producer بتوليد بيانات عشوائية، وConsumer بمعالجتها وتخزينها في PostgreSQL.

### Tech Stack / التقنيات المستخدمة
- Python  
- Kafka  
- SQL (PostgreSQL)  
- Docker  

### Project Structure / هيكل المشروع
```
Real_Time_Kafka_Project/
├── producer/       # Data generator
├── consumer/       # Stream processor
├── sql/            # Create tables
├── docker-compose.yml
├── requirements.txt
└── README.md
```

### Installation / طريقة التشغيل
```bash
pip install -r requirements.txt
docker-compose up -d  # Start Kafka and Zookeeper
python producer/data_generator.py
python consumer/stream_processor.py
```

### Usage / طريقة الاستخدام
- Producer sends data to Kafka topic `sales_topic`  
- Consumer inserts data into PostgreSQL in real-time  
