dia = int(input('Por quantos dias o carro foi alugado? ').strip())
km = int(input('Quantos kilometros foram percorridos com ele? ').strip().lower()
         .replace('km', '')
         .replace('/', '')
         .replace('h', '')
         )

preco = (dia * 60) + (km * 0.15)

print(f'O preço a pagar será de: R${preco:.2f}.')
