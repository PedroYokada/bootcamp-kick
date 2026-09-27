import os

if os.path.exists("exemplo3.txt"):
  os.remove("exemplo3.txt")
  print("Arquivo removido.")
else:
  print("O arquivo não existe!")
  

""" 
print(arquivo.readline(10))
print(arquivo.read(10)) """
""" arquivo = open('exemplo3.txt','r') """
""" arquivo = open('exemplo3.txt','x') """
""" arquivo = open('exemplo3.txt','a') """
""" arquivo = open('exemplo3.txt','w')

arquivo.write("Novas mensagens para o novo arquivo!") """








