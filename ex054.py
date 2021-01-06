# VERIFICADOR DE MAIORIDADE

from datetime import date

count = 0  # Contador iniciado

for c in range(6):
    year_born = int(input('Digite seu ano de nascimento: '))
    if date.today().year - year_born >= 18:  # Fazendo o cálculo para ver quem é maior de idade
        count += 1  # Contador acionado a cada maior de idade encontrado

print(f'{count} pessoas atingiram a maioridade. \n'
      f'{6 - count} pessoas ainda não atingiram a maioridade.')  # Número de pessoas menores
