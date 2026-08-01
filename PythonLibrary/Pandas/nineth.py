import pandas as pd
import numpy as np
from io import StringIO,BytesIO

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
dfs = pd.read_html(url)
"""
    import pandas as pd
    
    url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'
    dfs = pd.read_html(url)
    
    # Check the type of 'dfs'
    print(type(dfs))    
    # Output: <class 'list'>
    
    # Check the type of 'dfs[0]'
    print(type(dfs[0])) 
    # Output: <class 'pandas.core.frame.DataFrame'>
"""

print(dfs)
print('\n')
print(dfs[0])

"""
all pandas objects are required with to-pickle methodes which use python's cPickle module to save data structure to disk
using the pickle formate
"""

# Use the 'r' before the string to handle Windows backslashes properly
file_path = r"C:\Users\91816\Downloads\PythonLibrary\Pandas\Deloitte.xlsx"

df_excel = pd.read_excel(file_path)
print(df_excel.head())

df_excel.to_pickle('df_excel')
dffs = df_excel.to_pickle('df_excel')
print(type(dffs))
