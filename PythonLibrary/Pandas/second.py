import numpy as np
import pandas as pd

# csv means coma seprated values

df = pd.read_csv('mercedesbenz.csv')
print(df)

print(df.head())
print(df.info())

# df.describe() give the differen values like count, mean, std, min, 25%, 50%, 75%,max

print(df.describe())  # in this only integer and float column is consider in the table
# in this 25,50,75 is percentail not percentage 
# here percentage is how much scored out of total and percentail is how your score rank among other

# in csv default seprated perameter is ',' but we can change 
test_csv  = pd.read_csv('FirstCsv.csv')
print(test_csv)

test_csv1  = pd.read_csv('FirstCsv.csv',sep=';')
print(test_csv1)
# but problem is this add unnanme column at first place it contain pervious row name

# Get the unique category counts
print(df['X0'].value_counts())
# it print total occurence of unique element in first column

# if you wnat the pecific element 
print(df[df['y'] > 100]) 

#df.corr() is a DataFrame method that calculates the pairwise correlation between numerical columns in your DataFrame.
print(df.corr())
