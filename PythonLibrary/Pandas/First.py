import pandas as pd
import numpy as np

# pd.Dataframes(data = None, index = None, columns =  None)
df = pd.DataFrame(np.arange(0,20).reshape(5,4),index=['Row1','Row2','Row3','Row4','Row5'] ,  columns = ['column1','column2','column3','column4'])
print(df)
df.to_csv("FirstCsv.csv")

# Accessing the elements
## 1.  .loc  2.   .iloc (index location) --> in this we focusing on row and columns

print(df.loc['Row1'])
print(type(df.loc['Row1'])) # <class 'pandas.Series'>

print(df.iloc[0:3,0:3]) # in python programming indexing starting from 0

## take the elements from the column2
print(df.iloc[:,1:2])

print(type(df.iloc[:,:]))  # <class 'pandas.DataFrame'> for this you have more then one column or row
print(type(df.iloc[0,1:4])) # <class 'pandas.Series'>
print(type(df.iloc[0:3,0])) # <class 'pandas.Series'>

# convert Dataframes into array
print(df.iloc[:,2:].values)
print(type(df.iloc[:,2:].values)) # <class 'numpy.ndarray'>
print(df.iloc[:,:].values)
print(df.iloc[:,:].values.shape)

print(df.isnull().sum())

print(df['column1'].value_counts()) # it give the total occurance of number each unique number in columns
print(df['column1'].unique())
print(type(df['column1'].unique())) # give array

print(df['column1']) #type is series not for the row
print(df[['column1','column2']]) # this is two dimensional so use two sqaure bracket