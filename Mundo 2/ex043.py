

p = float(input('Digite seu peso em kg: ').strip().lower().replace('kg', ''))
h = float(input('Digite sua altura em metros: ').strip().lower().replace('m', ''))

imc = p / (h ** 2)

print(f'Seu imc é: {imc:.1f}')

if imc < 18.5:
    print(f'Abaixo do peso!')

elif 18.5 <= imc <= 25:
    print('Peso ideal!')

elif 25 <= imc <= 30:
    print('Sobrepeso!')

elif 30 <= imc <= 40:
    print('Obesidade!')

elif imc > 40:
    print('Obesidade mórbida!!!')
