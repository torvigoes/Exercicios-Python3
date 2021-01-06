print('=' * 30)
print()

viagem = float(input('Qual será a distância da sua viagem em Km? '))

if viagem <= 200:  # preço = viagem * 0.50 if distancia <= 200 else distancia * 0.45
    print('Sua viagem está dentre as mais curtas, portanto será cobrado o preço de R$0,50 por Km!')
    print(f'O preço da sua viagem será de: R${viagem * 0.50:.2f}')

else:
    print('Sua viagem está dentre as mais longas, portanto será cobrado o preço de R$0,45 por Km!')
    print(f'O preço da sua viagem será de: R${viagem * 0.45:.2f}')

print()
print('=' * 30)
