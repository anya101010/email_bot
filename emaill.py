import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
engine=pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def info():  
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice=listener.listen(source)
            info=listener.recognize_google(voice) 
            print(info) 
            return info.lower() 
    except:
        pass           



def send_email(receiver,subject,message):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('ananyakr32873@gmail.com','bbpt7dvd8macosx')
    email=EmailMessage()
    email['From']='ananyakr32873@gmail.com'
    email['To']=receiver
    email['Subject']=subject
    email.set_content(message)
    server.send_message(email)

email_list={
    'ananya':'ananya15606@gmail.com',
    'dog':'mariananikpal@gmail.com',
    'me':'anya1549@gmail.com'
}                 

def get_email_info():
    talk('to whom you want to send email')
    name= info()
    receiver = email_list[name]
    print(receiver)
    talk('what is the subject of your email?')
    subject=info()
    talk('tell me the text in your email')
    message=info()
    send_email(receiver,subject,message)


get_email_info()    