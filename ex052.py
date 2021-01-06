# VERIFICADOR DE NUMEROS PRIMOS

n = int(input('Digite um número para saber se ele é primo: '))

d = 0  # Iniciando o contador de divisores

for c in range(1, n+1):
    if n % c == 0:  # Cada vez que o número "n" tiver o resto da divisão por "c" igual a 0, a condição será ativada
        d += 1  # Contador do número de divisores de "n"

if d == 2:  # Caso 'n' tenha 2 divisores, que seria 1 e o próprio número
    print('PRIMO!')

else:
    print('NÃO PRIMO!')
