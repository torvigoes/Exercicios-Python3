count_man = count_maior = count_woman = 0

while True:
    age = int(input('Qual sua idade? '))
    sex = ' '  # Importante estar com o espaço dentro, se não, não será contabilizada
    while sex not in 'MF':
        sex = str(input('Qual seu sexo? [M/F]: ').upper().replace('MASCULINO', 'M').replace('FEMININO', 'F'))

    if age > 18:
        count_maior += 1
    if sex == 'M':
        count_man += 1
    if sex == 'F' and age < 20:
        count_woman += 1

    op = ' '  # Importante estar com o espaço dentro, se não, não será contabilizada
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]: ').upper().replace('SIM', 'S').replace('NAO', 'N').replace('NÃO', 'N'))

    if op == 'N':
        break

print(f'\n{count_maior} pessoas tem mais de 18 anos.\n'
      f'{count_man} homens foram cadastrados.\n'
      f'{count_woman} mulheres tem menos de 20 anos.')
