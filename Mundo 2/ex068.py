from random import randint
from time import sleep

pi = ''  # Escolha de par ou ímpar
r_is = ''  # Resultado da soma se é par ou ímpar

count = r = 0
pc_choice = randint(0, 10)

print('=-' * 30)
print(f"{'VAMOS JOGAR PAR OU ÍMPAR':^55}")
print('=-' * 30)
sleep(0.5)

while True:
    user_choice = int(input('Diga o valor: '))
    pi = str(input('Par ou ímpar? [P/I] ').lower().replace('p', 'PAR').replace('i', 'ÍMPAR'))
    print('-' * 50)
    sleep(1)

    r = user_choice + pc_choice  # Soma entre as escolhas

    if r % 2 == 0:  # Se for PAR
        r_is = 'PAR'
    else:  # Se for ÍMPAR
        r_is = 'ÍMPAR'

    print(f'Você escolheu {user_choice} e eu escolhi {pc_choice}, a soma é {r} e é {r_is}.')
    print('-' * 50)

    if pi == r_is:  # Se a escolha do usuário for igual o resultado
        print('VOCÊ VENCEU!\n'
              'Vamos jogar novamente...')
        count += 1
        print('=-' * 30)
        sleep(1)

    else:  # Se não for igual
        print('GAME OVER!!!\n'
              f'Você perdeu e teve um total de {count} vitórias consecutivas!')
        print('=-' * 30)
        break
