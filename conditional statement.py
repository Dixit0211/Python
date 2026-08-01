"""
if-elif-else(SYNTAX)

if(condition):
   statement1
elif(condition):
   statement2
else:
   statementN

"""

age = int(input("Enter the your age:"))

if(age >= 18):
   print("eligiable for the vote.")
else:
   print("you are not eligibale for.")

light = str(input("enter the traffic light:"))

if(light == "red"):
   print("stop")
elif(light == "green"):
   print("go")
elif(light == "yellow"):
   print("look") 
else:
   print("technicaal issue")