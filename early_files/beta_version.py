import listener, speech_recognition as sr
import pyttsx3, speaker
import locale
import datetime
import wikipedia, requests

# defining variables
recog = sr.Recognizer()
mic = sr.Microphone()
tts = speaker.text_to_speech
stt = listener.recognize_speech_from_mic

command = {
        "success": True,        # if it captured
        "error": None,          # if mis-setup or mis-hear
        "transcription": None   # what was said
    }

firstGreet = True
callSiri = False
goSleep = False

while True:
    try:
        goSleep = 'dormir' in command["transcription"].lower()
        if goSleep:
            break
        else:
            command = 'none'
    except AttributeError:
        print('Tô no standby, sem ouvir nenhum som ainda.')
        speaker.text_to_speech('Olá, já estou ligada, pode falar.')
        command = listener.recognize_speech_from_mic(recog, mic)
        continue
    while not callSiri:
        print('Qualquer coisa me grita meu nome, campeão!')
        speaker.text_to_speech('Se precisar de mim é só chamar meu nome.')
        command = listener.recognize_speech_from_mic(recog, mic)
        try:
            callSiri = 'siri' in command["transcription"].lower()
            goSleep = 'dormir' in command["transcription"].lower()
        except AttributeError:
            continue
        if not command["success"]:
            break
        if goSleep:
            break
        print("Num deu pra entender, consagrado, repete ae.\n")
        speaker.text_to_speech('Não entendi, pode repetir, por favor?')

    # if there was an error, stop the game
    if command["error"]:
        print("ERROR: {}".format(command["error"]))
        break
    if goSleep:
        break

    print('Tô te ouvindo, segura ae.')
    for i in range(5):
        try:
            makeAdventure = 'aventureiros' in command["transcription"].lower()
            orderMonsters = 'monstros' in command["transcription"].lower()
            goSleep = 'dormir' in command["transcription"].lower()
        except AttributeError:
            print('Fala meu patrão, seu desejo é minha ordem.')
            speaker.text_to_speech('Me chamou? Gostaria de ouvir uma história dos aventureiros ou dos monstros?')
            command = listener.recognize_speech_from_mic(recog, mic)
            continue
        
        if goSleep:
            break
        if not (makeAdventure or orderMonsters):
            print('Fala meu patrão, seu desejo é minha ordem.')
            command = listener.recognize_speech_from_mic(recog, mic)
            continue
        elif makeAdventure:
            speaker.text_to_speech('Os aventureiros estão na cidade! E eles vão até aí brincar com você Rafa!')
            break
        elif orderMonsters:
            speaker.text_to_speech('Cuidado! Os monstros estão à espreita, a Cuca está de baixo da cama.')
            break
        else:
            print('Malz pai, não peguei visão.')
    else:
        print('Tendi mesmo não meu rei eterno, tenta de novo.')

speaker.text_to_speech('Vou dormir, boa noite.')
