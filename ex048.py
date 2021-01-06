s = 0
count = 0

for c in range(1, 501, 2):
    if c % 3 == 0:  # Caso o resto da divisão entre o número 'c' e 3 seja 0
        s += c  # Acumulando os números ímpares múltiplos de 3 e somando-os
        count += 1
print(f'A soma dos {count} valores citados é de: {s}')
