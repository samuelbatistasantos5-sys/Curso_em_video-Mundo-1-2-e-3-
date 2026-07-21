import random

nome1 = input('Digite o nome dos primeiro aluno ')
nome2 = input('Digite o nome dos segundo aluno ')
nome3 = input('Digite o nome dos terceiro aluno ')
nome4 = input('Digite o nome dos quarto aluno ')

sorteio = random.choice((nome1, nome2, nome3, nome4))

print(sorteio)