from time import sleep

loop = False
while not loop:

    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))

    m = (n1 + n2) / 2

    if n1 <= 10 and n2 <= 10:
        print(f'Sua média foi de: {m}')

        if m < 5:
            print(f'\033[31mREPROVADO!!\033[31m\n')

        elif m >= 7:
            print(f'\033[32mAPROVADO!!\033[32m\n')

        else:
            print(f'\033[33mRECUPERAÇÃO!!\033[33m\n')

        loop = True
    elif (n1 > 10 or n2 > 10) or (n1 > 10 and n2 > 10):
        print('Valores não permitidos!!! RENICIANDO...')
        sleep(1)
