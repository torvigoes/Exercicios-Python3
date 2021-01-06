from time import sleep
from random import randint

user_choice = ''
pc_choice = randint(0, 10)
count_t = 0

name = str(input('Qual seu nome? ').strip().capitalize())
print()
sleep(0.5)
print('-=-' * 40)
print(f'Olá {name}! seja bem vindo(a) ao jogo da adivinhação!!')
print()
sleep(1.5)
print('Tente adivinhar o número entre 0 a 10 que eu estou pensando!!!')
sleep(2)

while user_choice != pc_choice:
    print()
    user_choice = int(input('Qual número você acha que eu pensei? '))
    count_t += 1
    sleep(1)

    if user_choice < pc_choice:
        print('Mais... Tente novamente!')
        sleep(0.5)
    if user_choice > pc_choice:
        print('Menos... Tente novamente!')
        sleep(0.5)

print()
print('=-='*40)
if user_choice == pc_choice:
    print(f'Parabéns {name}!!\n'
          f'Você acertou após {count_t} tentativas!\n'
          f'O número que eu pensei foi {pc_choice}.'
          )
print('=-='*40)
