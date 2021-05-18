#  CÁLCULO FATORIAL


n = int(input('Digite um número para o cálculo fatorial: ').strip())

count = n  # Para que o cálculo seja a partir do número determinado pelo fatorial
f = 1  # Fator nulo da multiplicação

while count > 0:  # Enquanto o número não for decrementado até 0
    print(count, end='')  # Fatorial sendo decrementado
    print(' x ' if count > 1 else ' = ', end='')  # Printar multiplicação caso seja maior que 0, e igual caso termine.
    f *= count
    count -= 1

print(f'{f}')
