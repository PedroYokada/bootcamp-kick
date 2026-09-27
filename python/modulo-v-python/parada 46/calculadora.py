def somar_num(n1,n2):
  return n1 + n2
def sub_num(n1,n2):
  return n1 - n2
def multi_num(n1,n2):
  return n1 * n2
def div_num(n1,n2):
  if n2 != 0:
    return n1 / n2
  else:
    print("Denominador não pode ser zero!")
    exit()

  
n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))

operacao = input("Insira 1-Soma/2-Subtração/3-Multiplicação/4-divisão:")

match operacao:

    case "1":
      resultado = somar_num(n1,n2)
    case "2":
      resultado = sub_num(n1,n2)
    case "3":
      resultado = multi_num(n1,n2)
    case "4":
      resultado = div_num(n1,n2)
    case _:
      print("Operação Inválida!")
      exit()

      
print(f"Resultado = {resultado:.2f}")
      