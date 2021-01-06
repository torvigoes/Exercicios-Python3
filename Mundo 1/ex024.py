# VERIFICAR SE A CIDADE COMEÇA COM "SANTO"

cidade = str(input('Digite o nome de uma cidade: ').lower().replace('-', ''))
#print("santo" in cidade[0:5])
cidade = cidade.split()
print(cidade[0] == "santo")
