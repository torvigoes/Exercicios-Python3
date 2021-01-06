# ALISTAMENTO MILITAR

from datetime import date

year_actual = date.today().year  # recebe o ano atual
year_birth = int(input('Digite seu ano de nascimento: '))

age = year_actual - year_birth
time_left = 18 - age  # TEMPO QUE FALTA PARA O ALISTAMENTO
time_pass = age - 18  # TEMPO PASSADO PARA O ALISTAMENTO

if age == 18:
    print(f'Está na hora de você se alistar!')

elif age > 18:
    print(f'Já passou da hora de você se alistar!\n'
          f'Fazem {time_pass} anos.\n'
          f'Você se alistou ou deveria ter se alistado em: {year_birth + 18}')

else:
    print(f'Ainda não está na hora de se alistar!\n'
          f'Faltam {time_left} anos.\n'
          f'Você terá que se alitar em: {year_birth + 18}')
