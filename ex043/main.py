altura = float(input('Digite sua altura '))
peso = float(input('Digite seu peso '))
imc = peso/(altura*altura)


if imc < 18.5:
    print("Você está abaixo do peso!")
elif imc >= 18.5 and imc < 24.9:
    print("Você está no peso normal!")
elif imc >= 25.0 and imc < 29.9:
    print("Você está com sobrepeso!")
elif imc >= 30.0 and imc < 39.9:
    print("Você está com obesidade!")
else:
    print("Você está com obesidade mórbida")