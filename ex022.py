# VERIFICADOR DE NOMES

nome = str(input('Digite seu nome completo: ').strip().capitalize())

print(f'{nome.upper()}')
print(f'{nome.lower()}')

print(f'{len(nome.replace(" ", ""))}')  # replace está retirando os espaços entre as palavras.
print(f'{len(nome.split()[0])}')  # separando o nome com o split, e lendo apenas o primeiro nome (item da lista).
