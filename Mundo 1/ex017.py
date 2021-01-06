from time import sleep
from math import hypot

print('=' * 30)
print(' ')

b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Agora, do cateto adjacente: '))

print(' ')
print('Calculando...')
sleep(0.5)

print(f'O comprimento da hipotenusa é de: {hypot(b, c):.2f}')

print(' ')
print('=' * 30)

