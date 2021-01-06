products = ('Lápis', 1.50, 'Borracha', 2.00, 'Caderno', 9.50, 'Apontador', 3.50)

print('-'*50)
print(f"{'LISTAGEM DE PREÇOS':^47}")
print('-'*50)

for c in products:
    if type(c) is str:  # Testando se é o nome do produto
        print(f'{c:.<32}', end='')  # Printando o nome do produto alinhado
    else:  # Se não for o nome do produto, será o preço
        print(f'R${c:>5.2f}')  # Printando o preço do produto alinhado

print('-'*50)
