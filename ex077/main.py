palavras = ("COMPUTADOR", "TECLADO","MOUSE","MONITOR","PYTHON","PROGRAMACAO","INTERNET","DESENVOLVIMENTO","ALGORITMO","SOFTWARE"
)

for palavra in palavras:
    print(f'Na palavra {palavra} temos as vogais ',end=" ")
    for n in palavra:
        if n in 'AEIOU':
            print(n, end=" ")
    print()
    