print('=' * 30)
print()

vel = str(input('Qual a velocidade atual do seu carro? ')).strip().lower() \
    .replace('km', '') \
    .replace('/', '') \
    .replace('h', '')

vel = float(vel)  # TRANSFORMAÇÃO DE STR PARA FLOAT

if vel <= 80:
    print('Tudo certo! Continue andando dentro dos limites.')

else:
    print('Você ultrapassou o llimite de velocidade!!!')
    multa = (vel - 80) * 7
    print(f'A multa será R$7,00 por cada km acima do limite, resultando em: R${multa:.2f}')

print()
print('=' * 30)
