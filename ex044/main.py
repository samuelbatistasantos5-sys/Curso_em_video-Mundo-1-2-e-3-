
preco_do_produto = float(input("Qual o preço do produto: "))
pagamento = int(input("Qual será a forma de pagamento: \n[1]A Vista(Debíto/Dinheiro/Cheque) \n[2]Cartão de crédito\n"))

if pagamento == 1:
    desconto = preco_do_produto-(preco_do_produto/100*10)
    print(f"O valor final do produto ficou R$ {desconto} reais")
else:
    parcelas = int(input("Você quer: \n[1]A vista \n[2]2x no cartão \n[3]3x ou mais\n"))
    if parcelas == 1:
        desconto = preco_do_produto-(preco_do_produto/100*5)
        print(f"O valor final do produto ficou R$ {desconto} reais")
    elif parcelas == 2:
        print(f"O valor final do produto ficou R$ {preco_do_produto} reais")
    else:
        juros = preco_do_produto+(preco_do_produto/100*20)
        print(f"O valor final do produto ficou R$ {juros} reais")
         


