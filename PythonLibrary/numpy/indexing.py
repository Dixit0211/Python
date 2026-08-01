import numpy as np

# accessing array element

arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr[3])

# accessing two dimensional array
arr1 = np.array([[1,2,3,4,5],
                  [2,3,4,5,6],
                  [9,7,6,8,9]])

print(arr1[:,:])
print(arr1[0:2,:]) # you print until2 row so you choose the 0th and 1st row 
print(arr1[0:2,0:2]) # give the 0th and 1st row and colunms
print(arr1[1:,3:]) # it select the 1st and 2nd rows or 3rd and 4th row 
print(arr1[1:2,1:4]) # row - 1 and column - 1,2,3

arr = np.arange(0,10,step = 2) # it start value with 0 and increase by 2 up to 10
print(arr) # [0 2 4 6 8]
arr = np.arange(0,10) # (lower value, higher value)
print(arr) # [0 1 2 3 4 5 6 7 8 9]

"""
Syntax:
    np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)

Parameters:
    start: The starting value of the sequence.
    stop: The ending value of the sequence.
    num: Number of samples to generate (default = 50).
    endpoint: If True (default), the stop value is included; if False, it is excluded.
    retstep: If True, returns the step size along with the array.
    dtype: Data type of the output array.

--> np.linspace() in NumPy is used to generate evenly spaced numbers over a specified interval. It’s especially useful when you want a sequence of values between two endpoints, divided into a specific number of steps.
"""

print(np.linspace(1,10,50))

# copy() function and broadcasting

arr = np.arange(1,10)
print(arr)
arr[3:] = 100 
print(arr)

arr1 = arr
arr1[3:] = 500
print(arr1)  # arr1 and arr is give me the same output if you change in one array the change is make in two array also
print(arr)
# array is actually a refernce type  we share the sam memory  to prevent this we have copy() function

arr1 = arr.copy()
arr1[3:] = 1000
print(arr1)
print(arr)

# Some conditions very useful in exploratory data analysis
val = 2
print(arr < val) # they print only true or false
print(arr * val)
print(arr % val)

# if you want the ecxect elment that less then value the write query
print(arr[arr<10])

# np.ones(shape, dtype = None, order = 'C)

print(np.ones(4)) # [1. 1. 1. 1.] default dtype is float
print(np.ones(4, dtype=int))
print(np.ones((2,5),dtype = int))

# random distribution  --. it select the random value in the given shape between 0 and 1 here distirbution is uniform
print(np.random.rand(3,3))
# importan notes (mean = 0, standard deviation = 1).
arr_ex = np.random.randn(4,4) # randn return a sample(or samples) from the "Standard normal" distribution
print(arr_ex)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arr_ex = np.random.randn(4,4)
df = pd.DataFrame(arr_ex.reshape(16,1), columns=["values"])

sns.displot(df["values"], kde=True)
plt.show()   # <-- forces the graph window to appear

# randint(low, high=None, size=None, dtype='1')
# return random integers from 'low' (inclusive) to 'high'(exclisive)
print(np.random.randint(0,100,8).reshape(4,2))

# random_sample(size = None)
# return random floats in the half-open interval [0.0, 1.0]
print(np.random.random_sample((1,5)))