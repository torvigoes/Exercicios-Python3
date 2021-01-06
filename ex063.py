# CÁLCULO SEQUENCIA DE FIBONACCI

t = int(input('Quantos termos você quer mostrar? '))

count_t = 2  # Contador de termos iniciado
next = 0  # Definindo próximo número na sequência
prev = 0  # Número anterior definido

print('0', end=' -> ')
while count_t <= t:
    count_t += 1  # Contador de termos acionado até que chegue a quantidade de termos designada pelo usuário
    next += prev  # O próximo número será igual a ele mesmo + o número anterior
    prev = next - prev  # O número anterior será igual ao próximo número - o anterior
    if next == 0:
        next += 1  # Iniciando os primeiros termos
    print(f'{next}', end=' -> ')
print('FIM')