import math
from time import sleep

print('='*30)
print(' ')

ang = int(input('Digite o valor do ângulo em graus: '))
angr = math.radians(ang)

print('Calculando...')
sleep(0.5)

print(f'O seno de {ang}º é igual a: {math.sin(angr):.2f}\nO cosseno é igual a: {math.cos(angr):.2f}\nA tangente é igual a: {math.tan(angr):.2f}')

print(' ')
print('='*30)
