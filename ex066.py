count = n = s = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break  # Importante vir antes para não entrar na soma e na contagem
    s += n
    count += 1
print(f'A soma dos números é de: {s}\n'
      f'Você digitou {count} números.')
