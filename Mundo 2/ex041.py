from datetime import date

year = int(input('Digite seu ano de nascimento: '))
age = date.today().year - year  # CALCULA A IDADE A PARTIR DO DATE.TODAY RECEBENDO O ANO ATUAL.

if age <= 9:
    print('Categoria: MIRIM')

elif age <= 14:
    print('Categoria: INFANTIL')

elif age <= 19:
    print('Categoria: JUNIOR')

elif age <= 20:
    print('Categoria SÊNIOR')

else:
    print('Categoria: MASTER')
