"""s = 0  # Acumulador iniciado
count = 0  # Contador iniciado

n = int(input('Digite um número para saber sua tabuada: '))

for c in range(0, n*10, n):  # "n*10" é o limite da tabuada
    s += n  # Acumulando e somando os valores de n para ter o resultado das multiplicações
    count += 1  # Contador para ser o multiplicador
    print(f"{n}x{count}= {s}")"""

n = int(input('Diigite um número para saber sua tabuada: '))

for c in range(1, 11):
    print(f'{n}x{c}={n*c}')
