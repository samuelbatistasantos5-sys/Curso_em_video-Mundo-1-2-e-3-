numero = int(input('Digite um número: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'unidades {unidade} ')
print(f'dezenas {dezena} ')
print(f'centena {centena}')
print(f'milhar {milhar} ')