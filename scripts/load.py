import pandas as pd
import psycopg2
import yaml

with open('config.yaml') as f:
    config = yaml.safe_load(f)

conn = psycopg2.connect(
    host=config['postgres']['host'],
    port=config['postgres']['port'],
    database=config['postgres']['database'],
    user=config['postgres']['user'],
    password=config['postgres']['password']
)

cur = conn.cursor()
df = pd.read_csv('data_clean.csv')

cur.execute("""
CREATE TABLE IF NOT EXISTS covid_data (
    Country TEXT,
    CountryCode TEXT,
    Slug TEXT,
    NewConfirmed INT,
    TotalConfirmed INT,
    NewDeaths INT,
    TotalDeaths INT,
    NewRecovered INT,
    TotalRecovered INT,
    Date TIMESTAMP
)
""")
conn.commit()

for _, row in df.iterrows():
    cur.execute("""
    INSERT INTO covid_data (Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, tuple(row))
conn.commit()
cur.close()
conn.close()