# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:54:26 2019

@author: Utkarsh
"""

def convert():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("Now listening, \nPlease Speak")
        audio = r.listen(source)
        
    try:
        print("Processing....")
        #r.recognize_google_cloud(audio)
        print("You said:-")
        print(r.recognize_google(audio))
    except:
        print("Didn't recognize that, please try again")
        return -1