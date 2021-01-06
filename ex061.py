#  CÁLCULO DE PA

nt = 0  # Iniciando contador de número de termos da PA

n1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão da PA: '))

while nt < 10:
    print(n1, end=' -> ')
    nt += 1  # Contador até 10
    n1 += r  # Fazendo o cálculo da PA acumulando a razão com base no primeiro termo

print('FIM')
