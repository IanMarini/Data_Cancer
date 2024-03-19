import request
import json
import pandas as pd

url= 'https://cancer-data.p.rapidapi.com/records
df= request.get(url)
print(df)