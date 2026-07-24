expressao = input("Digite a expressão: ")

for l in expressao:
    parentese = expressao.count('(')
if parentese%2 == 0:
    print("Sua expressão está correta")
else:
    print("sua expressão está incorreta")
     