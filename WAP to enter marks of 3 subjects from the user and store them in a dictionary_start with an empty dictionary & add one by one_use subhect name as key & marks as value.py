marks = {}

x = int(input("Enter the marks phy:"))
marks.update({"phy": x})

y = int(input("Enter the marks maths:"))
marks.update({"maths": y})

z = int(input("Enter the marks chem:"))
marks.update({"chem": z})

print(marks)