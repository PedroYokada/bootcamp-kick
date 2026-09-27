""" https://www.w3schools.com/python/python_lists.asp
https://www.w3schools.com/python/python_tuples.asp
https://www.w3schools.com/python/python_sets.asp
https://www.w3schools.com/python/python_dictionaries.asp
  """

# Crie um dicionário onde as chaves são os nomes dos 
# contatos e os valores são tuplas
# contendo o número de telefone e o e-mail do contato. 
# Permita que o usuário adicione novos
# contatos, visualize todos os contatos e procure por 
# um contato específico.

dicionario_pedro = {
  "Pedro" : ('1234-1234','pedro@gmail.com'),
  "Jack" : ('1111-1111','jack@gmail.com'),
  "Leila" : ('2222-2222','leila@gmail.com'),
}

nome = input("Cadastre um nome: ")
tel = input("Cadastre um telefone: ")
email = input("Cadastre um email: ")

dicionario_pedro[nome] = (tel,email)
print(dicionario_pedro)

nome = input("Pesquise um nome: ")

if nome in dicionario_pedro:
  pesquisar = dicionario_pedro[nome]
  tel = pesquisar[0]
  email = pesquisar[1]
  print(f"Os dados da pessoa é, NOME: {nome}, TELEFONE: {tel} , EMAIL: {email}")
else:
  print("Nome não encontrado!")







 
  
