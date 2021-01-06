#  CÁLCULO FATORIAL

n = int(input('Digite um número para saber seu fatorial: '))

count = n  # Contador começará com o valor igual o de n, para que na hora de printar o fatorial saia correto
f = 1  # Fator nulo da multiplicação

while count > 0:
    print(count, end='')  # Printando o valor do contador enquanto é decrementado
    print(' x ' if count > 1 else ' = ', end='')  # Printará 'x' até chegar no 1, pois após isso vem o '=' de resultado
    f *= count  # Multiplicando o número com o próximo conforme é decrementado
    count -= 1

print(f'{f}')
