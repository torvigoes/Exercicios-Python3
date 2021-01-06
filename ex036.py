# EMPRÉSTIMO PARA CASA

p = float(input('Digite o valor da casa: R$').strip())
s = float(input('Digite seu salário: R$').strip())
t = int(input('Digite em quantos anos irá pagar: ').strip().lower().replace('anos', ''))

prest = p / (t * 12)  # CÁLCULO DA PRESTAÇÃO

if prest > s * 0.3:  # PRESTAÇÃO PRECISA SER MAIOR QUE 30% DO SALÁRIO
    print(f'Seu empréstimo foi \033[31mNEGADO\033[31m!'
          f'\nO valor da prestação excede 30% do valor do seu salário!')

else:
    print(f'Seu empréstimo foi \033[32mAPROVADO\033[32m!'
          f'\nO valor de cada parcela será de: R${prest:.2f}')
