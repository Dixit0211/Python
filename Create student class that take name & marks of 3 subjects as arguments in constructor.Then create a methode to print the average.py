#createstudent class that takes name & marks of 3 subjects as arguments in constructor. Then create a metode to print the average

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return sum(self.marks)/3
    
s1 = Student("Tony",[98,87,90])
print(s1.name)
print(s1.marks)
print("hii",s1.name,"your avg score is:",s1.average())

s2 = Student("Joy",[97,94,91])
print(s2.name)
print(s2.marks)
print("hii",s2.name,"your avg score is:",s2.average())

s3 = Student("Root",[94,87,89])
print(s3.name)
print(s3.marks)
print("hii",s3.name,"your avg score is:",s3.average())

# second methode for calculating average
"""
def get_avg(self):
    sum = 0
    for val in self.marks:
        sum += val
    print("hii",self.name,"your avg score is:",sum/3)
"""