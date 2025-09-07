# ETL Project with Airflow and PostgreSQL

**هدف المشروع:** استخراج بيانات COVID من API، تنظيفها، وتحميلها في قاعدة بيانات PostgreSQL باستخدام Airflow.

**المهارات:** Python, Pandas, SQL, Airflow, YAML, Docker

**تشغيل المشروع:**
1. إعداد PostgreSQL: إنشاء قاعدة بيانات ومستخدم.
2. تثبيت المتطلبات:
   pip install -r requirements.txt
3. تشغيل Airflow:
   airflow db init
   airflow webserver
   airflow scheduler