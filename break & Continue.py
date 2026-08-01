"""
Break : used to terminate the loop when encountered.

continue : terminates execution in the current iteration & continues exucation of the loop with the next iteration.
"""
i = 1
while i <= 10:
    print(i)
    if(i == 9):
        break
    i += 1
print("End of the loop.")

j = 1 
while j <= 10:
    if(j == 6):
        j += 1
        continue # skip all element after the continue stetment 
    print(j)
    j += 1