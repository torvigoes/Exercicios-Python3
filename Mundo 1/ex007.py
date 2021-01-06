from time import sleep

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
print('Calculando...')
sleep(0.5)
print(f'A sua média é igual a : {(n1+n2)/2:.2f}')
