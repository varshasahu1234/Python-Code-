# import pyttsx3
# import speech_recognition as sr 
# import webbrowser
# import datetime

# # Initialize text-to-speech
# engine = pyttsx3.init()

# def speak(text):
#     print("Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()

# # Take voice input

# def take_command():
#     r =sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening....")
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)

#     try:
#         print("Recognizing....")
#         command = r.recognize_google(audio).lower()
#         print("You Said:", command)
#     except Exception as e:
#         speak("Sorry, I didn't catch that. Please say it again.")
#         return ""

#     return command

# # Functions

# def open_youtube():
#     webbrowser.open("https://www.youtube.com/")
#     speak("Opening YouTube")

# def open_Google():
#     webbrowser.open("https://www.google.com/")
#     speak("Opening Google")

# def tell_time():
#     time = datetime.datetime.now().strftime("%I,%M,%p")
#     speak(f"The current time is {time}")

# def tell_joke():
#     tell_joke = "Why do programmer prepare dark mode? Because light attracts bugs."

# #  Main Assistant loop
# def run_assistant():
#     speak("Hello, I am your voice assistance. How can I help you?")
    
#     while True:
#         command = take_command() 
        
#         if "open youtube" in command:
#             open_youtube()

#         elif "open google" in command:
#             open_Google()

#         elif "time" in command:
#             tell_time()

#         elif "joke" in command:
#             tell_joke()
        
#         elif "exit" in command or "quit" in command:
#             speak("GoodBye!")
#             break
        
#         elif command == "":
#             continue
        
#         else:
#             speak("Sorry, I don't understand that command")
# # Run
# run_assistant()