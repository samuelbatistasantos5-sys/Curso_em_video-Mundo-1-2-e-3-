n = int(input('Digite um número para saber sua tabuada até 10: '))

contador = 1

while contador <= 10:
    tabuada = n*contador
    print(f'{n} x {contador} = {n*contador}')
    contador = contador+1