# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n-1)
    
print(sum(5))

# wrute a recursive functionto printall element in list.
# hints: use list & index as perameters.


# for reverse
def list_el(list,idx):
    if(idx < 0):
        return
    else:
        print(list[idx])
        return list_el(list,idx-1)

list1 = [1,3,6,0,6,3]
idx = len(list1) - 1
list_el(list1,idx)

# for forward

def print_list(list,idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]
print_list(fruits)