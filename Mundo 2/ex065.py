user_choice = 's'
n = n_max = n_min = n_sum = count = 0

while user_choice in 's':
    n = int(input('Digite um valor: '))
    if n_min == 0:
        n_min = n
    if n_max < n:
        n_max = n
    if n_min > n:
        n_min = n
    user_choice = str(input('Deseja continuar [S/N]? ').lower())
    n_sum += n
    count += 1

print(f'A média entre os valores é de {n_sum/count:.2f}\n'
      f'O maior valor digitado foi: {n_max}\n'
      f'O menor valor digitado foi: {n_min}')
