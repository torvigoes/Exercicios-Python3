nome = str(input('Digite seu nome completo: ').strip().upper())

nome = nome.split()

print(f'Seu primeiro nome é: {nome[0]}')

print(f'Seu último nome é : {nome[-1]}')

# f'\nSeu ultimo nome é: {nome.rsplit(" ", 1)[1]}')
