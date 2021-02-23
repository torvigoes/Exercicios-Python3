# ANÁLISE DE DOIS VALORES

from time import sleep

user_choice = ' '
lista = []

print('=-='*40)
n1 = float(input('1º valor: '))
n2 = float(input('2º valor: '))
print('=-='*40)

sleep(1.5)

while user_choice != 5:
    user_choice = int(input('[ 1 ] SOMAR\n'
                            '[ 2 ] MULTIPLICAR\n'
                            '[ 3 ] MAIOR NÚMERO\n'
                            '[ 4 ] NOVOS NÚMEROS\n'
                            '[ 5 ] SAIR DO PROGRAMA\n'
                            'Opção desejada: ').strip()
                      )
    print()

    if user_choice == 1:
        print(f'A soma entre {n1} e {n2} é igual a: {n1+n2:.2f}')
        print()
        sleep(0.5)

    elif user_choice == 2:
        print(f'O produto entre {n1} e {n2} é de: {n1*n2:.2f}')
        print()
        sleep(0.5)

    elif user_choice == 3:
        lista.append(n1 and n2)
        print(f'O maior número entre {n1} e {n2} é: {max(lista)}')
        print()
        sleep(0.5)

    elif user_choice == 4:
        n1 = float(input('1º valor: ').strip())
        n2 = float(input('2º valor: ').strip())
        print()
        sleep(0.5)

    elif user_choice == 5:
        print('Finalizando em...')
        for c in range(3, 0, -1):
            print(c)
            sleep(1)
        print('ENCERRADO')

    else:
        print('Opção invalida!\n'
              'Tente novamente.\n')
        sleep(1.5)
