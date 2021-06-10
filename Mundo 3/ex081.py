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

print(f'O valor 5{" " if  5 in values else " não"}está na lista')  # printa um espaço caso 5 esteja na lista, se não 'não'
