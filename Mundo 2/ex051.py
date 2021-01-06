print(f'{"CÁLCULO DE PROGRESSÃO ARITMÉTICA":=^60}')
print()

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = a1 + 10 * r  # Cálculo termo geral da PA, para saber qual o último termo da PA, "10" são a quantidade de termos
# da PA

for c in range(a1, an, r):
    print(f"{c} -> ", end='')
print('FIM')
