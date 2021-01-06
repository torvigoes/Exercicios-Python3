from random import sample
from time import sleep

print('='*30)
print('')

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Do segundo: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('Do quinto: '))

print(' ')
print('Sorteando...')
print(' ')
sleep(0.5)
seq = [a1, a2, a3, a4]

print(f'A sequência de apresentação do trabalho será: {sample(seq, k=4)}')
print(' ')
print('='*30)
