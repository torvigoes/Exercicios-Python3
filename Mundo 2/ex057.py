 #  LEITOR DE SEXO ACEITANDO APENAS M OU F.


user_choice = str(input('Digite seu sexo [M/F]: ').upper().strip()[0])

while user_choice not in 'MF':  # Para evitar que o usuário digite uma opção inexistente.
    user_choice = str(input('\nOpção inválida!\nDigita uma opção válida [M/F]: ').strip().upper()[0])

if user_choice == 'M':
    print('Sexo masculino registrado!')
elif user_choice == 'F':
    print('Sexo feminino registrado!')
