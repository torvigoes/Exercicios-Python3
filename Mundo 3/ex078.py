#  MAIOR E MENOR VALORES NA LISTA

values = []

for cont in range(5):
    values.append(int(input("Digite um valor: ")))

print(f"\nO maior valor digitado foi: {max(values)}")
print(f"O menor valor digitado foi: {min(values)}")
