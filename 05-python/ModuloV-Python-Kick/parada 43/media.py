nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = float((nota1+nota2+nota3)/3)
media = round(media, 2)

if media < 6:
  print("Está reprovado, sua média é: ", media )
else:
  print("Está aprovado sua média é: ", media) 

