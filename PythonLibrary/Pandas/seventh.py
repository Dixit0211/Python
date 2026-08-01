import pandas as pd
import numpy as np
from io import StringIO,BytesIO

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(df.head())

df1 = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/planets.csv')
print(df1.head())

# This link is verified and working
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
# Read the TSV file explicitly stating the tab separator
df2 = pd.read_csv(url, sep='\t')
# Check if it loaded successfully by printing the first 5 rows
print(df2.head())
