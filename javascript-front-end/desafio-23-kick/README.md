# 🍍 Desafio 23–24 — Funções, `return` e seleção de produtos

## 📌 Sobre o projeto

Este exercício cria um pequeno menu de produtos no terminal. O usuário escolhe entre quatro itens — abacaxi, beterraba, coco e damasco — e o programa apresenta o preço correspondente. A opção `5` encerra a execução.

O foco principal é compreender como uma **função recebe um valor e devolve outro valor através de `return`**.

## 🎯 Objetivo

Criar uma função capaz de receber o item escolhido pelo usuário e retornar o preço associado a esse item.

## 🧠 Conceitos praticados

### Objeto como tabela de valores

Os preços são armazenados em:

```javascript
let compra = {
  1: 5.54,
  2: 8.55,
  3: 10.78,
  4: 15.66,
};
```

Esse objeto funciona como uma relação entre **chave e valor**: a chave representa a opção do produto e o valor representa o preço.

### Função com parâmetro

```javascript
function venda(fruta) {
  return compra[fruta];
}
```

`fruta` é um **parâmetro**. Ele recebe a opção fornecida quando a função é chamada. A expressão `compra[fruta]` utiliza a chave recebida para acessar o preço correspondente.

### `return`

O `return` encerra a função e envia um resultado para quem a chamou. Por exemplo, `venda(1)` devolve o valor associado à chave `1`.

Esse conceito é diferente de simplesmente usar `console.log()` dentro da função: `console.log()` apenas exibe algo, enquanto `return` entrega um valor que pode ser armazenado, calculado ou exibido em outro ponto do programa.

### `while`

O `while` mantém o menu ativo enquanto a opção for diferente de `5`. Isso permite realizar várias consultas sem reiniciar o programa manualmente.

### `switch/case`

Cada produto é tratado em um `case`. O `switch` é adequado quando uma variável pode assumir várias opções conhecidas e cada uma precisa executar um bloco diferente.

### Template literals

Expressões como:

```javascript
`O valor do abacaxi é: R$${venda(1)}`
```

utilizam **template literals**, delimitadas por crases. `${...}` permite inserir valores ou resultados de funções dentro de uma string.

### Conversão com `parseInt()`

A entrada recebida pelo `prompt-sync` começa como texto. `parseInt()` converte a opção para um número inteiro antes do `switch`.

## 🛠️ Tecnologias utilizadas

- JavaScript
- Node.js
- `prompt-sync`

## ⚙️ Fluxo

```text
Usuário escolhe produto
        ↓
parseInt converte a opção
        ↓
switch identifica o produto
        ↓
venda(opção)
        ↓
return recupera o preço
        ↓
console.log exibe o resultado
```

## 💡 Aprendizados

O ponto central deste exercício é perceber que uma função pode funcionar como uma pequena unidade de processamento: ela **recebe uma informação, executa uma tarefa e devolve um resultado**. Essa lógica será reutilizada em aplicações muito maiores.

## ▶️ Como executar

Tenha Node.js e `prompt-sync` disponíveis e execute `desafio23.js` pelo terminal.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
