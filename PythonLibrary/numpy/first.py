#initialy lets import numpy



import numpy as np

my_list = [1,2,3,4,5]

arr = np.array(my_list) #<class 'numpy.ndarray'> and the list converted into array
print(type(arr))
print(arr)

print(arr.shape) # give shape  (5,) specify the how many rows and columns in the array

# multinested array

my_list1 = [1,2,3,4,5]
my_list2 = [6,7,8,9,10]
my_list3 = [4,2,3,8,5]

# convert list into array

arr1 = np.array([my_list1,my_list2,my_list3])

print(arr1)
print(arr1.shape) # give (3,5)

# condition of reshape is row * column = total no. of element
print(arr1.reshape(5,3)) # it create view not change in the original one condition 

"""
if you want to change in original one
    import numpy as np

    arr1 = np.arange(15)   # shape (15,)
    arr1 = arr1.reshape(5,3)   # reassign back

    print("New shape:", arr1.shape)   # (5,3)

"""


