### 4. Função de Fatorial

""" **Enunciado:**

Implemente uma função chamada `calcular_fatorial` que recebe um número inteiro 
positivo como parâmetro e retorna o fatorial desse número. """


def calcular_fatorial(num):
  resultado = 1
  for a in range(1, num + 1):
    resultado *= a
  return resultado
      

resultado = calcular_fatorial(5)
print(resultado)  # Saída: 120
