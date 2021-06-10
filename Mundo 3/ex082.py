#  DIVIDINDO VALORES EM VÁRIAS LISTAS

pairs = []
imp = []
values = []

resp = 'S'
while resp == 'S':
    val = int(input("\nDigite um valor: "))
    values.append(val)
    resp = input("Deseja continuar [S/N]: ").upper()

    if val % 2 == 0:
        pairs.append(val)
    else:
        imp.append(val)

print(f"\nNúmeros: {values}"
      f"\nNúmeros pares: {pairs}\n"
      f"Números ímpares: {imp}")
