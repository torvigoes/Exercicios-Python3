age_list = []

name_man_old = ''
age_man_old = 0
girl_count = 0
man_count = 0

for c in range(1, 5):
    print(f'------ {c}ª PESSOA ------')
    name = str(input('Digite seu primeiro nome: ').strip().capitalize())
    age = int(input('Digite sua idade: ').strip().replace('anos', ''))
    sex = str(input('Digite seu sexo [M/F]: ').strip().lower().replace('masculino', 'm').replace('feminino', 'f'))
    age_list.append(age)  # Adicionando todas as idades do grupo em uma lista

    if sex == 'm':
        man_count += 1
        if age > age_man_old:
            age_man_old = age
            name_man_old = name
            man_count += 1

    if sex == 'f' and age < 20:
        girl_count += 1

print(f'A média de idade do grupo é de {sum(age_list)/4:.1f} anos.')

if man_count == 0:
    pass
else:
    print(f'O nome do homem mais velho é {name_man_old}, e tem {age_man_old} anos.')

if girl_count == 0:
    pass
else:
    print(f'{girl_count} mulheres tem menos de 20 anos')
