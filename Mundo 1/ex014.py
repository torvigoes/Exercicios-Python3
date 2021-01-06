import temp2temp

graus = int(input('Digite uma temperatura em graus Celsius: ').strip().lower().replace('c', '').replace('º', ''))
print(f'Esta temperatura em Fahrenheit é: {temp2temp.Celsius.to_fahrenheit(graus)}F')
