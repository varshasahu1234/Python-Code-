import pyttsx3


engine = pyttsx3.init()

# name = input("What is your good name : ")

# message = f"Hello {name}, I am Jarvis, Your Personal Assistant. How can I help you ?"

# print(message)

with open("file.txt","r") as file:
    message = file.read()

engine.say(message)
engine.runAndWait()


