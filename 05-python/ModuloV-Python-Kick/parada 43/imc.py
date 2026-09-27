peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = float(peso/(altura * altura))
imc = round(imc, 2)


if imc < 18.5:
    print("Abaixo do peso, seu imc é de: ", imc)
elif imc >= 18.5 and imc <= 24.9:
     print("Peso normal, seu imc é de: ", imc)
elif imc >= 25.0 and imc <= 29.9:
     print("Sobrepeso, seu imc é de: ", imc)
elif imc >= 30.0 and imc <= 39.9:
     print("Obesidade, seu imc é de: ", imc)
else:
     print("Obesidade grave, seu imc é de: ", imc)