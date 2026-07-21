import random

nome1 = input('Digite o nome dos primeiro aluno ')
nome2 = input('Digite o nome dos primeiro aluno ')
nome3 = input('Digite o nome dos primeiro aluno ')
nome4 = input('Digite o nome dos primeiro aluno ')

sorteio = list((nome1, nome2, nome3, nome4))
random.shuffle(sorteio)
print(sorteio)
