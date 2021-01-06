from time import sleep


print(f'{"LOJAS GOES":=^30}')

price = float(input('Preço do produto: R$').strip())
print()
sleep(0.5)

print('''MÉTODOS DE PAGAMENTO:
       [ 1 ]  À VISTA DINHEIRO/CHEQUE (10% DESCONTO)
       [ 2 ]  À VISTA NO CARTÃO (5% DESCONTO)
       [ 3 ]  EM ATÉ 2x NO CARTÃO (PREÇO NORMAL)
       [ 4 ]  3x OU MAIS NO CARTÃO (20% JUROS)''')
print()

loop = False
while not loop:

    choice = int(input('Digite sua opção: '))

    print()
    print('CALCULANDO...')
    sleep(0.5)
    print()

    if choice in range(1, 5):
        if choice == 1:
            print(f'O preço do produto é de: R${price:.2f}\n'
                  f'Com 10% de desconto você pagará: R${price * 0.9:.2f}')

        elif choice == 2:
            print(f'O preço do produto é de: R${price:.2f}\n'
                  f'Com 5% de desconto você pagará: R${price * 0.95:.2f}')
        elif choice == 3:
            print(f'O preço do produto é de: R${price:.2f}\n'
                  f'Em 2x sem juros você pagará 2 parcelas de: R${price / 2:.2f}')
        elif choice == 4:
            print(f'O preço do produto é de: R${price:.2f}')
            v = int(input('Em quantas vezes você deseja fazer? '))
            print(f'Em {v}x com 20% de juros você pagará {v} parcelas de: R${(price * 1.20) / v:.2f}')

        loop = True
    else:
        print('Opção não disponível. REINICIANDO!!!')
        sleep(1.5)
        print()