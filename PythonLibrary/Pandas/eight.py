import pandas as pd
import numpy as np
from io import StringIO,BytesIO

df = pd.read_json('https://raw.githubusercontent.com/domoritz/maps/master/data/iris.json')
print(df)
df1 = pd.read_json('Pandas/inventory.json')
print(df1)

# Your raw JSON string written directly in the code
json_string = '''
[
  {"id": 1, "name": "Alice", "role": "AI Engineer"},
  {"id": 2, "name": "Bob", "role": "Backend Developer"}
]
'''
# Wrapping it in io.StringIO is the safest, most modern way to read raw strings in Pandas
df2 = pd.read_json(StringIO(json_string))
print(df2)

data = '''
{"employee_name" : "james" , "email" : "joyboy800@gmail.com" , "job_profile" : [{"title1" : "Team Leader" , "title2" : " Sr.Devloper.."}]}
'''
df3 = pd.read_json(StringIO(data))
print(df3)

df4 = pd.read_json('https://jsonplaceholder.typicode.com/posts' )
print(df4)
print(df4.describe())

dfr = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', header = None)
print(dfr)

#convert json to csv
df4.to_csv('wine.csv')
print(df4)

#convert json to different json formats
# it convert object into string
print(df3.to_json()) # it give column_name and key value pair
print('\n')
"""{"employee_name":{"0":"james"},"email":{"0":"joyboy800@gmail.com"},"job_profile":{"0":{"title1":"Team Leader","title2":" Sr.Devloper.."}}}"""
print(df3.to_json(orient='index'))
print('\n')
"""{"0":{"employee_name":"james","email":"joyboy800@gmail.com","job_profile":{"title1":"Team Leader","title2":" Sr.Devloper.."}}}"""
print(df3.to_json(orient='split'))
print('\n')
print(df3.to_json(orient='table'))
print('\n')
print(df3.to_json(orient='values'))
