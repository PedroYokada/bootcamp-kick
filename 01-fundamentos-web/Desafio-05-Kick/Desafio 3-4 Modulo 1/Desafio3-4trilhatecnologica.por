programa {
  funcao inicio() {
    
    real v1
    real v2
    real res
    caracter opcao

      enquanto (opcao != 'e')
		{
	      escreva ("Insira o primeiro numero: \n")
      leia (v1)

      escreva ("Insira o segundo numero: \n")
      leia(v2)

      escreva ("Digite a operação desejada, sendo a = soma, b = subtração, c = multiplicação, d = divisão, e = sair: \n")
      leia(opcao)

      escolha(opcao) {

        caso 'a' :
          res = v1 + v2
          escreva("O valor da soma é de: " ,res ,"\n")
          pare

        caso 'b' :
          res = v1 - v2
          escreva("O valor da subtração é de: " ,res, "\n")
          pare

        caso 'c' :
          res = v1 * v2
          escreva("O valor da multiplicação é de: ",res, "\n")
          pare

        caso 'd' :
          se (v2 e v1 != 0) {
            res = v1 / v2
            escreva("O valor da divisão é de: ", res, "\n")
          } senao {
            escreva("Não é possível dividir por zero.\n")
          }
          pare

        caso 'e' :
          pare

        caso contrario :
          escreva("Opção inválida. Tente novamente.\n")
      }
		}
      


  }
}



    

  

