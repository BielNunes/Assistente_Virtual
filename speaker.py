''' adiciona funcionalidade de fala à siri '''

import pyttsx3
import time
import locale
import datetime

''' Speaker de testes '''

# Exemplos de texto para teste ou uso na aplicação main

# hora e data
locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')
asd = datetime.datetime.now().strftime("%H:%M:%S %d/%B/%Y")

# frases misc
maquaigem = 'Sim, gostei da maquiagem.'

# roteiro darksouls deathless
ds_bosslist = (
    'asylum demon. '+
    'bell gargoyles. '+
    'Quelaag. '+
    'ceaseless discharge. '+
    'iron golem. '+
    'Ornstein e Smough. '+
    'Sif, o lobo. '+
    'Pinwheel. '+
    'Nito. '+
    '4 kings. '+
    'Seath, o dragão. '+
    'bed of chaos. '+
    'Gwyn. '
)
ds_fromstart = (
    'Primeiro de tudo escolha a classe do bandido. '+
    'Derrote o azailum dimom. Em firelink pegue '+
    'as firebombs, e os ossos de baixo do elevador. '+
    'Vá ao mercador comprar a clava, o arco, e as flechas. '+
    'Equipe a clava. Siga para o ferreiro. Pegue uma '+
    'alma fora do primeiro elevador. Uma alma na pata do dragão, '+
    'e outra após o segundo elevador. Na floresta pegue o escudo. '+
    'Uma alma. Um set. E o lagarto cintilante. No ferreiro, melhore '+
    'a clava. E siga para derrotar a gárgola.'
)
ds_tipsgargoyle = (
    'Não trave mira nele. E se mantenha colado na parede. Mire os ataques no rabo.'
)
ds_fromgargoyle = (
    'Volte andando e pegue o elevador para firelink. Siga pelo '+
    'atalho direto para Quelaag. Aproveite e mate o Ceaseless Discharge. '+
    'Volte com osso. Vá para o ferreiro. Compre o crest '+
    'para abrir a floresta. O weapon box. Flechas. E considere melhorar o arco.'+
    'Aumente o nível de força. E vá buscar o anel de estrela. Siga para '+
    'a fortaleza.'
)
ds_tipsquelaag = (
    'Fique em frente à ela. Espere o cuspe. E vá para a lateral. Aguarde o ataque longo.'
)
ds_tipsceaseless = (
    'Depois dele se debater. Corre para o portão. E espera ele chegar. Fique centralizado no portão.'
)

# histórias pra dormir
historia = '''ERA UMA VEZ uma mamã pata que teve 5 ovos.
    Ela esperava ansiosamente pelo dia em que os seus ovos
    quebrassem e deles nascessem os seus queridos filhos!

    Quando esse dia chegou, os ovos da mamã pata começaram
    a abrir, um a um, e ela, alegremente, começou a saudar
    os seus novos patinhos. Mas o último ovo demorou mais a
    partir, e a mamã começou a ficar nervosa…
    
    Finalmente, a casca quebrou e, para surpresa da mamã pata,
    de lá saiu um patinho muito diferente de todos os seus outros filhos.
    - Este patinho feio não pode ser meu! Exclama a mamã pata.
    - Alguém te pregou uma partida. Afirma a vizinha galinha.

    Os dias passaram e, à medida que os patinhos cresciam, o
    patinho feio tornava-se cada vez mais diferente dos outros patinhos.
    Cansado de ser gozado pelos seus irmãos e por todos os animais
    da quinta, o patinho feio decide partir.
    Mesmo longe da quinta, o patinho não conseguiu paz, pois os seus
    irmãos perseguiam-no por todo o lago, gritando:
    - És o pato mais feio que nós alguma vez vimos!
    E, para onde quer que fosse, todos os animais que encontrava faziam troça dele.
    - Que hei de eu fazer? Para onde hei de ir? O patinho sentia-se muito triste e abandonado.
    
    Com a chegada do inverno, o patinho cansado e cheio de fome encontra uma casa e pensa:
    - Talvez aqui encontre alguém que goste de mim! E assim foi.
    O patinho passou o inverno aconchegadinho, numa casa quentinha e na
    companhia de quem gostava dele. Tudo teria corrido bem se não tivesse
    chegado a primavera e com ela, um gato malvado, que enganando os donos da
    casa, correu com o patinho para fora dali!
    - Mais uma vez estou sozinho e infeliz… Suspirou o patinho feio.
    
    O patinho seguiu o seu caminho e, ao chegar a um grande lago, refugiou-se
    junto a uns juncos, e ali ficou durante vários dias.
    Um dia, muito cedo, o patinho feio foi acordado por vozes de crianças.
    - Olha! Um recém-chegado! Gritou uma das crianças. Todas as outras crianças davam gritos de alegria.
    - E é tão bonito! Dizia outra.
    Bonito?... De quem estarão a falar? Pensou o patinho feio.
    De repente, o patinho feio viu que todos olhavam para ele e, ao ver
    o seu reflexo na água, viu um grande e elegante cisne.
    - Oh!... Exclama o patinho admirado. Crianças e outros cisnes admiravam
    a sua beleza e cumprimentavam-no alegremente.

    Afinal ele não era um patinho feio mas um belo e jovem cisne!
    A partir desse dia , não houve mais tristezas, e o patinho feio
    que agora era um belo cisne, viveu feliz para sempre!'''

def text_to_speech(string2voice):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(string2voice)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":

    text_to_speech(asd)