# biblioteca pentru recunoastere vocala
pip install SpeechRecognition
pip install pyaudio

import speech_recognition as sr
from unitree_sdk import Go2Robot  # Asigură-te că SDK-ul Unitree e instalat și configurat

#initializare robot
robot = Go2Robot(ip_address='192.168.123.161')  # IP-ul standard pentru Go2, ajustează dacă e altul

#initializare recunoastere vocala
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Ascult... spune 'Salut'!")
    audio = recognizer.listen(source)

try:
    #convertirea audio in text
    text = recognizer.recognize_google(audio, language="ro-RO")  # Recunoaștere vocală în limba română
    print(f"Am recunoscut: {text}")

    if "salut" in text.lower():
        print("Comandă: Salut detectată! Ridic piciorul.")
        
        #comanda catre robot: ridică piciorul din fata
        robot.move_leg(leg='front_left', angle=45, speed=0.5)
        
    else:
        print("Comandă necunoscută.")
except Exception as e:
    print("Eroare la recunoaștere sau control:", str(e))
