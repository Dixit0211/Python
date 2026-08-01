import pyttsx3 as pt

engine = pt.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)


name = input("Enter your name:")
text = f"your name is {name}"
engine.say(text)
engine.runAndWait()
age = int(input("Enter the your age:"))
print(age)