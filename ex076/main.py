acessorios = ('Mouse Gamer', 149.90, "Teclado Mecânico", 299.90, "Headset Gamer", 219.90, "Mousepad XXL", 79.90,
"Controle sem fio",249.90) 

print("-="*20)
print(" "*12 + "Tabela de preços")
print("-="*20)
for n in acessorios:
    ind = acessorios.index(n)
    if ind%2 == 0:
        print(f"{n:.<30}", end="")
    else:
        print(f"R$ {n}")
