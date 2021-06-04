#  LISTA ORDENADA SEM USAR O MÉTODO SORT()

values = []

for cont in range(5):
    val = int(input("Digite um valor: "))
    if len(values) == 0 or val > values[-1]:  # O append sempre adiciona no fim da lista
        values.append(val)
    else:
        pos = 0  # Posição dentro da lista
        while pos < len(values):
            if val <= values[pos]:
                values.insert(pos, val)
                break
            pos += 1
    print(values)
print(f"\nA lista ficou assim: {values}")
