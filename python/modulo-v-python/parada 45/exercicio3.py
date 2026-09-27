# # Crie uma lista de compras onde cada item é um dicionário com o nome do produto,
# # a quantidade e o preço. O usuário deve ser capaz de adicionar novos produtos, visualizar
# # a lista de compras e calcular o valor total.
  
  

compras_pedro = {
  "Biscoito" : 1.90,
  "Batata" : 2.50,
  "Coca Cola" : 10.90
}

nome_produto = input("Adicione um produto: ")
valor_produto = float(input("Informe o preço: "))

compras_pedro[nome_produto] = (valor_produto)

for nome_produto, valor_produto in compras_pedro.items():
  print(f"Nome do produto: {nome_produto}, Valor do produto: {valor_produto:.2f}")
  
preco_final = sum(compras_pedro.values())

print(f"A soma da compra é de: {preco_final:.2f}")


