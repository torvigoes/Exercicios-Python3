from time import sleep
from random import randint

player_choice = ' '
count_t = 0
pc_choice = randint(0, 10)

name = str(input('Qual seu nome? ').capitalize().strip())
sleep(1)
print()

print(f'Olá {name}! Seja bem vindo ao jogo de adivinhação!\n'
      f'Tente adivinhar qual número entre 0 e 10 que eu estou pensando!')
sleep(0.75)

while player_choice != pc_choice:
    print()
    player_choice = int(input('Qual número você acha que eu pensei: ').strip())
    count_t += 1
    sleep(0.5)

    if player_choice < pc_choice:
        print('\nMais... tente novamente!')

    elif player_choice > pc_choice:
        print('\nMenos... tente novamente!')

print()
print('=-='*40)
if player_choice == player_choice:
    print(f'Parabéns {name}!!!\n'
          f'Você acertou após {count_t} tentativas!\n'
          f'O número que eu pensei foi {pc_choice}!'
          )
print('=-='*40)
