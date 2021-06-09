values = []
count = 0

resp = 'S'
while resp == 'S':
    values.append(int(input("\nDigite um valor: ")))
    count += 1  # Contador para quantos números foram digidtados
    resp = input("Deseja continuar [S/N]: ").upper()

values = sorted(values, reverse=True)  # Inverte a ordem da lista
print(f"\nForam digitados {count} números.\n"
      f"Decrescente: {values}")

if 5 in values:
    print("O valor 5 está na lista.")
else:
    print("O valor 5 não está na lista.")
