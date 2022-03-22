import speech_recognition as sr
#import os
#import pyttsx3 as pt



'''def speak(audioString):
    print(audioString)    
    engine = pt.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-40)

    engine.say(audioString)
    engine.runAndWait()

speak('Hey I am Alexa')'''


r=sr.Recognizer()
with sr.Microphone() as source:      #download pipwin pyaudio#
     
    # speak('i am waiting for your question')
     print('say something')

     r.adjust_for_ambient_noise(source)
     audio=r.listen(source)
try:
    print(r.recognize_google(audio,language="en-US"))
    question = r.recognize_google(audio)
    if 'alexa' in question:
        question = question.replace('alexa','')
        print(question)
        
        if 'what are you doing' in question:
            print('Nothing')
        elif 'how are you' in question: 
            print('im fine , thank you,how can i help you')
        elif 'where is pig' in question:
            print('vaadu pedda jaffa gaadu vaadi gurinchi adagaku')
    
        else:
            print('come again')
            #print('come again')   
except sr.UnknownValueError:
    print('i didnt get your voice properly,sorry')
    print('Speech complete')
    print('Finished')
         #print('iam waiting your question')
    
