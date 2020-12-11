import requests
import pandas as pd
import json
import sqlite3

r = requests.get('https://test.biografklubdanmark.dk/api/v1/apps/movies')

data =r.json()['data']
#movies = json.dumps(data, indent=2)
#print(movies)

#print(type(data))

df = pd.DataFrame(data)
df = df.applymap(str)
#print(df.head())
#print(df.columns)


conn = sqlite3.connect('api.db')
c = conn.cursor()

df.to_sql("api",conn)










