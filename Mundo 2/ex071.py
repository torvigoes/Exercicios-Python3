#  CONTADOR DE CÉDULAS


value = int(input('Digite o valor a ser sacado: '))

total = value  # Pegando o valor a ser sacado
ced = 50  # Começando na cedula de 50
totced = 0  # Total de cedula por valor

while True:
    if total >= ced:  # Enquanto puder retirar o valor da cedula do valor total
        total -= ced  # Retirando o valor da cedula do valor total
        totced += 1  # Contando o número de cédulas por valor
    else:  # Quando não puder mais tirar do valor até então usado
        if totced > 0:  # Printar apenas as cédulas usadas, se usar 0 de algum valor, não printará
            print(f'{totced} cédulas de R${ced:.2f}')
        if ced == 50:  # Quando não puder mais decrementar 50
            ced = 20
        elif ced == 20:  # Quando não puder mais decrementar 20
            ced = 10
        elif ced == 10:  # Quando não puder mais decrementar 10
            ced = 1
        totced = 0  # Reiniciando a contagem de cédulas 

        if total == 0:
            break
