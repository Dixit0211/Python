import pandas as pd
import numpy as np

from io import StringIO,BytesIO

## specifying column data type

data = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11')

print(data)
print(type(data)) # <class 'str'>

df = pd.read_csv(StringIO(data), dtype = object)
print(df)

print(df['a'])
print(df['a'][1]) # here data type is srring
# in integer NaN is not ther so it give error for fixing these


data1 = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11,12')

df1 = pd.read_csv(StringIO(data1), dtype = float)
print(df1)

df1 = pd.read_csv(StringIO(data1), dtype = int)
print(df1)

df = pd.read_csv(StringIO(data), dtype = {'b': int, 'c': float, 'a':np.int64})
print(df)
print(df['a'][1])

## check the datatype
print(df.dtypes)
"""
a      int64
b      int64
c    float64
d    float64
dtype: object
"""
