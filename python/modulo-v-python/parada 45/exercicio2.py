# #Descrição: Crie um programa que solicite ao usuário para 
# digitar uma frase e,
# #  em seguida, identifique e exiba todas as palavras únicas 
# na frase. Utilize um set
# # para garantir que as palavras não sejam repetidas.

# usuario insere a frase
frase_user = input("Digite uma frase: ")

#o metodo split separa as palavras de forma individual.
palavra_individual = frase_user.split()

#o set é criado para nao ter palavras repetidas.
palavras_nao_repetidas = set(palavra_individual)


# o for vai mostrar as palavras que sao unicas
for palavra_individual in palavras_nao_repetidas:
  print(palavra_individual)