print('='*30)
print()

print('Informe o valor de 3 retas para saber se essas podem formar um triângulo!')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

if (b - c) < a < (b + c):
    if (a - c) < b < (a + c):
        if (a - b) < c < (a + b):
            print('É possível formar um triângulo com essas retas!')

else:
    print('Não é possível formar um triângulo com essas retas!')

print()
print('='*30)
