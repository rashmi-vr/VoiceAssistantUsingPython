# import speech_recognition as sr

# def takeCommand():
#     r = sr.Recognizer()                                                                                   
#     with sr.Microphone() as source:                                                                      
#         print("listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)
    
#     try:
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"User said {query}\n")

#     except Exception as e:
#         print(e)
#         print("say that again please...")
#         return "None"

#     return query
# takeCommand()