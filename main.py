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

# functions to command actions
def horaData():
    locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')
    horadata = datetime.datetime.now().strftime("%H:%M:%S %d/%B/%Y")
    tts(horadata)

def wikiPesquisa(subject):
    try:
        wikipedia.API_URL = 'https://'
        wikipedia.set_lang('pt_BR')
        resposta = str(wikipedia.summary(subject))
        tts(resposta)
    except requests.exceptions.ConnectionError:
        tts('Desculpe, houve um problema de conexão, tente novamente mais tarde.')

# starting assistant
print('Serviço online.')
tts('Já acordei. Qualquer coisa é só me chamar.')
while True:
    # loop starts in standby, waiting to be called by name
    print('Em standby...')
    command = stt(recog, mic)
    if not command["success"]:
        break
    order = command['transcription']
    try:
        order = order.lower()
    except AttributeError:
        continue
    try:
        # initializer and terminator from standby
        callSiri = False
        goSleep = False
        callSiri = ('siri' in order)
        goSleep = ('dormir' in order or 'desligar siri' in order or 'boa noite siri' in order)
    except TypeError:
        continue
    if goSleep:
        print('Boa, noite.')
        tts('Vou dormir, boa noite.')
        quit()
    elif callSiri:
        # main section, after assistant wakes up
        tts('Oi, me chamou? O que deseja mestre?')
        for _ in range(7):
            # you got 7 tries to place your order
            command = stt(recog, mic)
            order = command['transcription']
            try:
                order = order.lower()
            except AttributeError:
                continue
            try:
                # check if command was called, command naming list
                Story = False
                Makeup = False
                timeDate = False
                goSleep = False
                wikiSearch = False
                darkSouls = False
                Story = 'história' in order
                Makeup = ('gostou' in order and 'maquiagem' in order)
                timeDate = ('hora' in order or 'horas' in order or 'dia' in order or 'mês' in order or 'ano' in order or 'data' in order)
                goSleep = ('dormir' in order or 'desligar siri' in order or 'boa noite siri' in order)
                wikiSearch = ('pesquisa' in order or 'pesquise' in order or 'pesquisar' in order)
                darkSouls = ('sem morte' in order or 'sem morrer' in order or 'zero morte' in order or 'zero mortes' in order)
            except TypeError:
                # if there was no command, dont verify command action list
                continue
            if goSleep:
                print('Boa, noite.')
                tts('Vou dormir, boa noite.')
                quit()
            elif timeDate:
                horaData()
                break
            elif wikiSearch:
                tts('O que você quer que eu pesquise?')
                for _ in range(7):
                    # you got 7 tries to place your order
                    command = stt(recog, mic)
                    order = command['transcription']
                    try:
                        order = order.lower()
                        wikiPesquisa(order)
                        break
                    except AttributeError:
                        tts('Não entendi, repete por favor.')
                        continue
            elif Makeup:
                tts(speaker.maquaigem)
                break
            elif Story:
                tts(speaker.historia)
                break
            elif darkSouls:
                tts('De onde quer que eu comece a narrar o roteiro?')
                for _ in range(7):
                    command = stt(recog, mic)
                    order = command['transcription']
                    try:
                        order = order.lower()
                    except AttributeError:
                        tts('Não entendi, repete por favor.')
                        continue
                    try:
                        # check if command was called, command naming list
                        bossList = False
                        fromStart = False
                        tipsGargoyle = False
                        fromGargoyle = False
                        tipsQuelaag = False
                        tipsCeaseless = False
                        fromSensFort = False
                        goBack = False
                        goSleep = False
                        options = False
                        bossList = (('chefão' in order or 'chefões' in order) and 'lista' in order)
                        fromStart = ('início' in order or 'começo' in order)
                        tipsGargoyle = (('dica' in order or 'dicas' in order) and 'gárgola' in order)
                        fromGargoyle = (('gárgola' in order or 'sino' in order) and 'depois' in order)
                        tipsQuelaag = (('dica' in order or 'dicas' in order) and 'aranha' in order)
                        tipsCeaseless = (('dica' in order or 'dicas' in order) and 'monstro' in order and 'lava' in order)
                        fromSensFort = ('portão' in order or 'fortaleza' in order)
                        goBack = ('volta' in order or 'voltar' in order or 'esquece' in order)
                        goSleep = ('dormir' in order or 'desligar siri' in order or 'boa noite siri' in order)
                        options = ('opções'in order or 'opção' in order)
                    except TypeError:
                        # if there was no command, dont verify command action list
                        continue
                    if goSleep:
                        print('Boa, noite.')
                        tts('Vou dormir, boa noite.')
                        quit()
                    elif goBack:
                        tts('Ok, se precisar é só chamar.')
                        break
                    elif bossList:
                        tts(speaker.ds_bosslist)
                        break
                    elif tipsGargoyle:
                        tts(speaker.ds_tipsgargoyle)
                        break
                    elif tipsQuelaag:
                        tts(speaker.ds_tipsquelaag)
                        break
                    elif tipsCeaseless:
                        tts(speaker.ds_tipsceaseless)
                        break
                    elif fromStart:
                        tts(speaker.ds_fromstart)
                        break
                    elif fromGargoyle:
                        tts(speaker.ds_fromgargoyle)
                        break
                    elif fromSensFort:
                        tts('você ainda não fez essa parte.')
                        break
                    elif options:
                        tts(
                            'Dicas de cada chefão. '+
                            'Lista dos chefões. '+
                            'Começar o roteiro do início. '+
                            'Começar da gárgola. '+
                            'Começar do portão da fortaleza.'
                        )
                        tts('Qual opção você deseja ouvir?')
                    else:
                        tts('Não entendi, repete por favor.')
                break
            else:
                tts('Desculpe, não entendi.')

# if there was an error, report it
if command["error"]:
    print("ERROR: {}".format(command["error"]))
    tts('Ops, parece que algo deu errado...')
else:
    print('Boa, noite.')
    tts('Vou dormir, boa noite.')
