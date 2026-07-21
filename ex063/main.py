n = int(input("Digite quantos termos da sequência de Fibonacci você quer: "))
cont = 0
a = 0
b = 1
while cont < n:
    print(a, end="-")
    fbc = a+b
    a = b
    b = fbc
    cont += 1
print("fim da sequência")