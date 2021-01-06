product_cheap = ''  # Nome do produto mais barato
s = count_price = price_cheap = 0  # Soma dos preços, contador dos preços acima de 1000, preço mais barato

while True:
    name = str(input('Nome do produto: ').capitalize())
    price = float(input('Preço: R$'))
    s += price  # Somando os preços

    if price_cheap == 0 or price_cheap > price:  # Para retirar o valor de zero, depois o menor valor sendo adicionado
        price_cheap = price
        product_cheap = name

    if price > 1000:
        count_price += 1

    op = ' '  # É importante estar com o espaço dentro, pois se não, não será contabilizada
    while op not in 'SN':  # Para que não tenham respostas fora disso
        op = str(input('Deseja continuar [S/N]? ').upper().replace('SIM', 'S').replace('NAO', 'N').replace('NÃO', 'N'))

    if op == 'N':
        break

print(f'O total gasto na compra foi de R${s:.2f}\n'
      f'Temos {count_price} produtos custando mais de R$1000\n'
      f'O produto mais barato foi {product_cheap} custando R${price_cheap:.2f}')
