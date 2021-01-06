print('='*30)
print()

salario = float(input('Digite seu salário: R$ '))

if salario > 1250:
    print(f'Seu salário recebeu um aumento de 10%, totalizando: R${salario * 1.10:.2f}')

else:
    print(f'Seu salário recebeu um aumento de 15%, totalizando: R${salario * 1.15:.2f}')

print()
print('='*30)
