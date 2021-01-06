#  LEITOR DE SEXO ACEITANDO APENAS M OU F.

s = str(input('Digite seu sexo [M/F]: ').strip().lower()[0])

while s not in 'mf':
    s = str(input('\nOpção inválida!\nDigite uma opção válida: '))

if s == 'm':
    print('Sexo masculino registrado!')
elif s == 'f':
    print('Sexo feminino registrado!')
