from datetime import datetime

ano = int(input('Em que ano você nasceu '))
ano_atual = datetime.now().year

idade = ano_atual-ano

if idade == 18:
    print('Você deve se alistar esse ano')

elif idade < 18:
    print(f'Você deve se alistar daqui a {18-idade} anos')

elif idade > 18:
    print(f'Você deveria ter se alistado a {idade - 18} anos atrás')




