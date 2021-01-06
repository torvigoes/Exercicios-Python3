mytuple = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    user_choice = ' '
    op = ' '
    while op not in range(0, 11):
        op = int(input('Digite um número entre 0 e 10: '))
    print(f'Você digitou o número {mytuple[op]}')
    user_choice = str(input('Deseja continuar? [S/N] ').upper().replace('SIM', 'S').replace('NÃO', 'N'))
    if user_choice == 'N':
        break
