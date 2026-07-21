ano = int(input('Digite o ano: '))
calculo = ano%100


if calculo == 0:
    verificaco = ano%400

    if verificaco == 0:
        print(f'O ano {ano} é um ano bissexto')
    else:
         print(f'O ano {ano} não é um ano bissexto')

else:
    verificaco = ano%4

    if verificaco == 0:
        print(f'O ano {ano} é um ano bissexto')
    else:
         print(f'O ano {ano} não é um ano bissexto')
