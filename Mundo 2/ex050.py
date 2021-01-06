s = 0

for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:  # Caso o número seja par, será acumulado e somado abaixo
        s += n
print(f'A soma apenas dos números pares digitados é: {s}')
