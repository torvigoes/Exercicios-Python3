# PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING

frase = str(input('Digite uma frase: ').strip().lower())
frase = frase.replace('á', 'a').replace('â', 'a').replace('ã', 'a') # SUBSTITUINDO OS A'S COM ACENTO.
print(frase.count('a'))
print(frase.find('a')+1) # O +1 EM AMBAS SERVE PARA ANULAR O '0'.
print(frase.rfind('a')+1)