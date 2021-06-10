exp = str(input("Digite a expressão: "))
prnt = []

for simb in exp:
    if simb == '(':
        prnt.append('(')
    elif simb == ')':
        if len(prnt) > 0:
            prnt.pop()
        else:
            prnt.append(')')
            break
if len(prnt) == 0:
    print("Sua expressão está válida!")
else:
    print("Expressão inválida!")
