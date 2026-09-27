a = 50
b = 20
c = 30

if a < b and b < c:
  print("a é menor que b e b é menor que c")
else:
  print("Uma das condições não é verdadeira")

  #and, as duas condições devem ser verdadeira, se uma for falsa, não atende a condição

  a = 1
  b = 2
  c = 5

  if a < b or b < c:
    print("Pelo menos uam das condições é verdadeira")
  else:
    print("Nenhuma das condições são verdadeiras")
#OR

a = 10
b = 20
if not a > b:
  print("Vermelho")
else:
  print("Azul")
