t1 = (int(input('Digite um  número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o último número: ')))

print(f'O valor 9 apareceu {t1.count(9)} vezes.')
print(f'O valor 3 está na {t1.index(3) + 1}ª posição') if 3 in t1 else print('O valor 3 não foi digitado em nenhuma '
                                                                             'posição')

print(f'Os valores pares digitados foram:', end=' ')
for c in t1:
    if c % 2 == 0:
        print(c, end=' ')
