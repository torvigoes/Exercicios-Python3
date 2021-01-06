from random import choice
from time import sleep

print('='*30)
print(' ')

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Do segundo: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('Do quarto: '))

print('Sorteando...')
print(' ')
sleep(0.5)

seq = choice([a1, a2, a3, a4])
print(f'O aluno escolhido(a) foi: {seq}')

print(' ')
print('='*30)
