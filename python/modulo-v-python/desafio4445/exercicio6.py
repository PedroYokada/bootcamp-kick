#Faça um programa em que o usuário digita um número inteiro e o 
# programa exibe todos os 
# números ímpares do 1 até o valor inserido.

numero = int(input("Digite um número inteiro: "))

for a in range (1 ,numero + 1):
    if a % 2 != 0:
      print(a)



