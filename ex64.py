from time import sleep

user_choice = count = s = 0

while user_choice != 999:
    user_choice = int(input('Digite um valor (999 para parar): '))
    if user_choice != 999:
        count += 1
        s += user_choice
print(f'\nVocê digitou {count} valores!\n'
      f'A soma entre eles é de: {s}\n')
sleep(0.5)
print('ENCERRADO')