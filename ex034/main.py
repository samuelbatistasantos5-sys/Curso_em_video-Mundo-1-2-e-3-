salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250.00:
    aumento = salario+(salario/100*15)
else:
     aumento = salario+(salario/100*10)

print(f'O salário do funcionário vai para {aumento}')