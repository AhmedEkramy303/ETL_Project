import requests
import yaml
import pandas as pd

with open('config.yaml') as f:
    config = yaml.safe_load(f)

response = requests.get(config['api']['url'])
data = response.json()
df = pd.DataFrame(data['Countries'])
df.to_csv('data.csv', index=False)