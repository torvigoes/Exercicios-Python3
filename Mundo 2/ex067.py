n = count = s = 0

while True:
    print('-' * 38)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 38)
    if n < 0:  # Condição de parada do laço
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
print('FIM')
