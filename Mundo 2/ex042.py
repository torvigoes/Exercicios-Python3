from time import sleep

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if abs(b - c) < a < (b + c) and abs(a - c) < b < (a + c) and abs(a - b) < c < (a + b):
    print('É possível formar um triângulo com essas retas!')

    sleep(0.5)
    print()

    if a == b == c:
        print('Este é um triângulo equilátero!')

    elif a == b or a == c or b == c:
        print('Este é um triângulo isósceles!')

    else:
        print('Este é um triângulo escaleno!')

else:
    print('Não é possível formar um triângulo com essas retas!')
