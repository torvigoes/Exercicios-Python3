#  ANÁLISE DE DOIS VALORES

from time import sleep

user_choice = ''
lista = []

print('=-='*40)
n1 = float(input('1º valor: '))
n2 = float(input('2º valor: '))
print('=-='*40)

sleep(1.5)

while user_choice != 5:
    print()
    print('[ 1 ] SOMA\n'
          '[ 2 ] MULTIPLICAÇÃO\n'
          '[ 3 ] MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR DO PROGRAMA\n')
    print('=-=' * 40)
    sleep(1)
    print()
    user_choice = int(input('Opção desejada: ').strip())
    print()

    if user_choice == 1:
        print(f'A soma entre {n1} e {n2} é igual a: {n1+n2:.2f}')
        sleep(0.5)

    if user_choice == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a: {n1*n2:.2f}')
        sleep(0.5)
    if user_choice == 3:
        lista.append(n1)
        lista.append(n2)
        print(f'O maior número entre {n1} e {n2} é: {max(lista)}')
        sleep(0.5)

    if user_choice == 4:
        n1 = float(input('1º valor: '))
        n2 = float(input('2º valor: '))
        sleep(0.5)

    if user_choice == 5:
        print('FINALIZANDO...')
        sleep(0.5)

    else:
        print('Opção inválida!!\n'
              'Tente novamente')
        sleep(1.5)
sleep(2)
print('Encerrado')
