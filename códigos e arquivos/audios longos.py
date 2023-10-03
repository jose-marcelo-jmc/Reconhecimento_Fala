import speech_recognition as sr
import time

def tratar_audio(rec, audio):
    global acabou
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)
    if "encerrar gravação" in texto:
        acabou = True

acabou = False

rec = sr.Recognizer()

with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('Comece a falar')

parar_ouvir = rec.listen_in_background(microfone, tratar_audio)

while True:
    time.sleep(0.1)
    if acabou == True:
        break

parar_ouvir(wait_for_stop=False)