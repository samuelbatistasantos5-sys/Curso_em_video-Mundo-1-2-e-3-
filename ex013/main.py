salario = float(input('Informe o salário do funcionário: '))
reajuste = (salario/100)*15
salario_final = salario+reajuste

print(f'O salário do funcionário vai de R$ {salario}, para R$ {salario_final}')