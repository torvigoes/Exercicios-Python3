m = 0
name_old = ''
man_old = 0
man_count = 0
girl_count = 0

for c in range(4):
    name = str(input('Digite seu nome: ').capitalize().strip())
    age = int(input('Digite sua idade: ').strip())
    sex = str(input('Digite seu sexo [F/M]: ').strip().upper())
    m += age

    if sex == 'F':
        if age < 20:
            girl_count += 1

    if sex == 'M':
        man_count += 1
        if age > man_old:
            man_old = age
            name_old = name

print(f'A média de idade do grupo é igual a: {m / 4:.2f} anos.')

if girl_count == 0:
    pass
else:
    print(f'São {girl_count} mulheres com menos de 20 anos.')

if man_count == 0:
    pass
else:
    print(f'O nome do homem mais velho é {name_old} e ele têm {man_old} anos.')
