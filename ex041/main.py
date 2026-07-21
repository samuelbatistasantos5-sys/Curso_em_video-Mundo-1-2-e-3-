from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input('Em quye ano você nasceu? '))
idade = ano_atual - ano_nascimento


if idade <= 9:
    print(f'O atelta tem {idade} anos, e está na categoria MIRIM')

elif idade > 9 and idade <= 15:
    print(f'O atelta tem {idade} anos, e está na categoria INFANTIL')

elif idade > 15 and idade <= 19:
    print(f'O atelta tem {idade} anos, e está na categoria JUNIOR')

elif idade > 19 and idade <= 20:
    print(f'O atelta tem {idade} anos, e está na categoria SÊNIOR')

else:
    print(f'O atleta tem {idade} anos, e está na categoria MASTER')
