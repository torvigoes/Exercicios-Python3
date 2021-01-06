# MAIOR E MENOR PESO

"""p_max = 0
p_min = 0"

for c in range(5):
    p = float(input('Digite o seu peso: '))
    if c == 1:  # Para que ambos abaixo recebam valores.
        p_max = p
        p_min = p
    else:
        if p > maior:
            p_max = p
        if p < menor:
            p_min = p

print(f'O maior peso é {p_max}kg\n'
      f'O menor peso é {p_min}kg')"""

lista = []

for c in range(5):
    p = int(input('Digite o seu peso: ').upper().replace('KG', ''))
    lista.append(p)  # Adicionando os pesos a lista, também é possível usar lista += [p]

print(f'O maior peso é {max(lista)}kg\n'
      f'O menor peso é {min(lista)}kg')
