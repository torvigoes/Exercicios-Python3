
l = float(input('Digite a largura da sua parede em metros: ').strip().lower().replace('m', ''))
h = float(input('Digite a altura da sua parede em metros: ').strip().lower().replace('m', ''))
a = l * h
print(f'As dimensões da sua parede são {l}x{h}m\n'
      f'Serão necessários {a/2:.2f}l para pintar a sua parede!')
