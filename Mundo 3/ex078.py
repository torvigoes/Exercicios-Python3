#  MAIOR E MENOR VALORES NA LISTA

values = []

for cont in range(5):
    values.append(int(input("Digite um valor: ")))

maior = max(values)
menor = min(values)

for i, v in enumerate(values):  # I -> posição / V -> valor
    if v == maior:
        print(f'\nO maior número é {maior} e está na posição: {i+1}')
for i, v in enumerate(values):  # I -> posição / V -> valor
    if v == menor:
        print(f"\nO menor número é {menor} e está na posição: {i+1}")
