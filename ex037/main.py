numero = int(input('Escolha um número: '))

conversao = int(input('Escolha para qual sitema deseja converter o número escolhido\n[1]Binário \n[2]Octal \n[3]Hexadecimal\n'))

if conversao == 1:
    print('Binário')

elif conversao == 2:
    print('Octal')

elif conversao == 3:
    print('Hexadecimal')

else:
    print('Sua escolha é inválida')