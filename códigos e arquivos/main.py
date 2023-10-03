import speech_recognition as sr

rec = sr.Recognizer()


with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('pode começar a falar:')
    rec.pause_threshold = 5

    audio = rec.listen(microfone)
    try:
        texto = rec.recognize_google(audio, language="pt-BR")
        print(texto)
    except:
        print('Não captei nenhum áudio')