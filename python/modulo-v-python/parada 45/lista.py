
lista = ['Pedro' , 'Ana' , 'Sara', 'Maria']
print(lista)

lista2 = ['1234-1111','1234-1234','3333-3333']
print(lista2)

for x in range(4):
  print(lista[x])
for x in range(3):
  print(lista2[x])
  
meu_dicionario = {
  "nome": "Pedro",
  "idade": "28",
  "cidade": "Barueri",
}

idade = meu_dicionario.get("idade")
print(idade)

pais = meu_dicionario.get("pais" , "Brasil")
print(pais)
