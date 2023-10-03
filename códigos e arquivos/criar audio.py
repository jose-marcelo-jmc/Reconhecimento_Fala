import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print('pode começar a falar:')
    audio = rec.listen(microfone)

with open("audio.wav", "wb") as arquivo:
    arquivo.write(audio.get_wav_data())