
import random
import playsound
import emoji
from time import sleep


pc = random.randint(0, 5)

print('=' * 40)
print()

nome = str(input('Qual seu nome? ').strip().capitalize())

if nome == 'Julia':
    print(emoji.emojize(f'Nossa! {nome} é o nome da minha namorada, que coincidência... '
                        f':two_hearts: '
                        f':heart: '
                        f':cupid:',
                        use_aliases=True)
          )

    playsound.playsound('love.mp3')

    sleep(0.5)

print(f'Olá {nome}, Seja bem vindo ao jogo de adivinhação!')

sleep(0.5)

num = int(input('Tente adivinhar qual número entre 0 e 5 eu estou pensando: '))

print('Huuummmm.....')

sleep(0.5)

if num == pc:
    print(emoji.emojize(f'Parabéns {nome}!! Você adivinhou :smile:',
                        use_aliases=True)
          )

    playsound.playsound('acertou.mp3')

else:
    print(emoji.emojize(f'Opa {nome}! Você errou, eu pensei no número {pc} :sob:',
                        use_aliases=True)
          )

    playsound.playsound('errou.mp3')

print()
print('=' * 40)
