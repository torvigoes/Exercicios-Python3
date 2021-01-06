
"""num_t = 0  # Número de termos iniciado
max_t = 10  # Número máximo de termos iniciado
count_t = 0  # Contador de termos iniciado

n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

while max_t != 0:  # Enquanto o número máximo de termos for diferente de 0
    num_t += max_t  # Limitando a PA em 10 para o primeiro laço
    while count_t <= num_t:  # Enquanto o contador de termos não chegar no número desejado o laço irá rodar para o calculo
        print(n1, end=' -> ')
        n1 += r  # Acumulando a razao e fazendo o calculo a partir do n1
        count_t += 1  # Contando os termos para que chegue ate o numero recebido antes
    print('PAUSA')
    max_t = int(input('Deseja mostrar mais quantos termos? 0 para parar: '))
print('FIM')"""


n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

count = 10  # Contador iniciado em 10 para a PA mostrar 10 termos

while count > 0:  # Enquanto o contador não zerar o laço será executado
    print(n1, end=' -> ')
    n1 += r  # Calculo da PA acumulando a razão a partir do n1
    count -= 1  # Decrementando do contador para que chegue em zero

    if count == 0:  # Quando o contador zerar
        count = int(input('\nQuantos termos a mais você quer mostrar? '))  # Acrescentando termos na PA

print('FIM')
