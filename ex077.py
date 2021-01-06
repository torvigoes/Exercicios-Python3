words = ('borboleta', 'aviao', 'carro', 'geladeira', 'grátis')

for word in words:  # Para cada palavra no conjunto de palavras
    print(f'\nNa palavra {word.upper()} temos: ', end='')
    for letter in word:  # Para cada letra na palavra
        if letter.lower() in 'aáàãâeéèêiou':  # Se a letra for uma vogal
            print(letter, end='')
