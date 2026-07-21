from datetime import date
maiores = 0
menores = 0
anoatual = date.today().year
for c in range(0, 7):
    ano = int(input("Digite seu ano de nascimento: "))
    if anoatual - ano >= 21:
        maiores = maiores+1
    else:
        menores = menores + 1
        
print(f"De todas essas pessoas, {maiores} já são de maiores, e {menores} são de menores")