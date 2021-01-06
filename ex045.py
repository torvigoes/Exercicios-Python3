from random import choice

pc = choice(['Pedra', 'Papel', 'Tesoura'])  # ESCOLHA DO PC

user = str(input('Pedra, papel ou tesoura? ').strip().capitalize())

if user == pc:
    print(f'Parece que empatamos, eu também escolhi {pc}!')

elif user == 'Pedra' and pc == 'Papel':
    print(f'Eu ganhei!!! Escolhi {pc}')

elif user == 'Pedra' and pc == 'Tesoura':
    print(f'Você ganhou!!! Escolhi {pc}')

elif user == 'Papel' and pc == 'Tesoura':
    print(f'Eu ganhei!!! Escolhi {pc}')

elif user == 'Papel' and pc == 'Pedra':
    print(f'Você ganhou!!! Escolhi {pc}')

elif user == 'Tesoura' and pc == 'Pedra':
    print(f'Eu ganhei!!! Escolhi {pc}')

elif user == 'Tesoura' and pc == 'Papel':
    print(f'Você ganhou!!! Escolhi {pc}')
