#  VALORES ÚNICOS EM UMA LISTA

values = []

resp = 'S'
while resp == 'S':
    val = int(input("\nDigite um valor: "))
    if val not in values:
        values.append(val)
    else:
        print("Este número já está na lista!")
    resp = input("Deseja continuar [S/N]: ").upper()
values.sort()
print(values)
