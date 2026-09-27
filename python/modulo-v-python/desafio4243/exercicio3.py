codigo = int(input("Informe o código do produto: "))
nome_produto = input("Digite o nome do produto: ")
qntd_produto = int(input("Informe a quantidade do produto: "))
preco_produto = float(input("Informe o preço do produto: "))

preco_total = qntd_produto * preco_produto
preco_total = round(preco_total, 2)

print("O código do produto é: ", codigo)
print("O nome do produto é: ", nome_produto)
print("O preço da compra é de: ", preco_total)