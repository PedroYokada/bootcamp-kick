# Função de Verificação de Paridade Crie uma função chamada eh_par 
# que recebe um número como parâmetro 
# e retorna True se o número for par e False se for ímpar.

def eh_par(numero):
  if numero % 2 != 0:
    return False
  else:
    return True
    
print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False
