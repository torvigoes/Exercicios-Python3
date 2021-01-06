count = 0

for c in range(0, 51, 2):  # Usar o passo '2' economiza carga do processador, ao invés de usar um if.
    count += 1
    print(c, end='->')
print(f'\nSão {count} números pares')