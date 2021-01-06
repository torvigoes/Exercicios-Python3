# SEPARADOR DE CASAS DE NÚMEROS

"""num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print(f'O milhar vale: {num[0]}')
print(f'A centena vale: {num[1]}')
print(f'A dezena vale: {num[2]}')
print(f'A unidade vale: {num[3]}')"""

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
print(f'Unidade: {u}')

d = num // 10 % 10
print(f'Dezena: {d}')

c = num // 100 % 10
print(f'Centena: {c}')

m = num // 1000 % 10
print(f'Milhar: {m}')
