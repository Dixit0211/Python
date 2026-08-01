import pandas as pd
import numpy as np

from io import StringIO, BytesIO

data = ('col1,col2,col3\n'
        'x,y,1\n'
        'a,b,2\n'
        'c,d,3')

print(type(data)) # <class 'str'>

print(pd.read_csv(StringIO(data)))
print(StringIO()) # give me the address of object

## Read from the specific columns
"""
The issue with your code lies in the way you're using the usecols parameter.
usecols can accept a callable, but the callable must return True if the column should be included. In your case:

        df = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['col1','col3'])

        Here’s the subtle bug:
                x.upper() converts the column name to uppercase.
                But your list ['col1','col3'] is lowercase.
                So the condition will always evaluate to False, meaning no columns will be selected.

        ✅ Correct Fix
        You should make both sides consistent in case:

                df = pd.read_csv(StringIO(data), usecols=lambda x: x.lower() in ['col1','col3'])
        or
                df = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1','COL3'])
"""
df = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['col1','col3'])
print(df) # so in this no column is selected

df = pd.read_csv(StringIO(data), usecols=['col1', 'col3'])
print(df)
 
df.to_csv('JDK.csv')
