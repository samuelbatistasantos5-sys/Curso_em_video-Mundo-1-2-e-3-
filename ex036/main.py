valor_casa = float(input('Qual o preço da casa? '))
salario = float(input('Quanto você ganha de sálario? '))
tempo = int(input('Em quantos anos você deseja pagar? '))

prestacao_mensal = int(valor_casa/(tempo*12))

if prestacao_mensal <= (salario*0.30):
    print(f'Você pode pegar o emprestimo.\nO valor da prestação vai ser de R$ {prestacao_mensal} mensalmente')

else:
    print('Você não pode pegar o empréstimo, porque a prestação mensal é maior que trinta porcentos do seu sálario.')