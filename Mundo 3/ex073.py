mytuple = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Internacional', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos',
           'Corinthians', 'Ceará SC', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Fortaleza', 'Sport Recife'
           'Bahia', 'Vasco da Gama', 'Goiás', 'Botafogo', 'Coritiba')

print('Os primeiros cinco colocados são: ')
for c in mytuple[0:5]:
    print(c)

print()

print('Os últimos quatro colocados são: ')
for c in mytuple[-1:-5:-1]:
    print(c)

print()
print(f'Os times em ordem alfabética: {sorted(mytuple)}')
print()

print(f'O time do Bragantino está na {mytuple.index("Bragantino")+1}ª posição')
