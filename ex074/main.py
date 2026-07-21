from random import randint

maior = menor = 0
a = randint(0,9)
b = randint(0,9)  
c = randint(0,9) 
d = randint(0,9)
e = randint(0, 9)
num = a, b, c, d, e

for i in range(0,5):
    if i == 0:
        maior = num[0]
        menor = num[0]
    else:
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]


print(f"Os números sorteados foi: {num}")  
print(f"O maior número sorteado foi {maior}")
print(f"O menor número sorteado foi {menor}") 



