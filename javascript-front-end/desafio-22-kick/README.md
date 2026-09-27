# 🧠 Desafio 21–22 — Quiz com Funções em JavaScript

## 📌 Sobre o projeto

Este desafio implementa um **quiz executado no terminal** com quatro temas: Geologia, Química, Física e Mineralogia. O usuário informa seu nome, escolhe qual tema deseja responder e acumula pontos de acordo com as respostas corretas.

O exercício foi proposto para praticar principalmente o uso de **funções**, mas também reúne condições, repetição, `switch`, retorno de valores e entrada de dados.

## 🎯 Objetivo

Dividir um programa maior em partes menores e reutilizáveis, utilizando uma função para cada tema do quiz.

## 🧠 Conceitos praticados

### Funções

O código possui `Geologia()`, `Quimica()`, `Fisica()` e `Mineralogia()`. Cada função é responsável por um conjunto específico de perguntas.

Uma função ajuda a evitar que todo o programa fique concentrado em um único bloco. Ela também torna mais clara a responsabilidade de cada parte do código.

### `return`

Cada função mantém seu próprio contador de pontos e, ao terminar, executa:

```javascript
return pontosProva;
```

O **`return`** devolve um resultado para o trecho que chamou a função. O programa principal soma esse valor à pontuação total.

### Variáveis e escopo

Existe um `pontosProva` geral e também uma variável com o mesmo nome dentro de cada função. As variáveis declaradas dentro das funções pertencem ao **escopo local** da função e são utilizadas para contar os acertos daquele tema.

### `while`

O laço `while` mantém o menu em execução enquanto `ProvaGeociencias` for verdadeiro. Quando o usuário escolhe `0`, a variável recebe `false` e a repetição termina.

### `switch/case`

O `switch` direciona a execução de acordo com a opção numérica selecionada. Cada `case` chama uma função diferente e `default` trata escolhas que não pertencem ao menu.

### `if/else`

As respostas são verificadas com estruturas condicionais. `toLowerCase()` transforma o texto digitado em minúsculas, reduzindo diferenças causadas pelo uso de letras maiúsculas.

### Acumulador

A expressão `pontosProva += Geologia()` é um exemplo de **acumulação**. O valor retornado pela função é somado ao total já existente.

### Entrada pelo terminal

O programa utiliza o pacote `prompt-sync` para receber dados de forma síncrona no Node.js. `parseInt()` é empregado para converter a opção do menu de texto para número inteiro.

## 🛠️ Tecnologias utilizadas

- JavaScript
- Node.js
- `prompt-sync`

## 📂 Arquivo principal

```text
desafio22.js
```

## ⚙️ Fluxo do programa

```text
Nome do aluno
      ↓
Escolha do tema
      ↓
Função correspondente
      ↓
Perguntas + if/else
      ↓
return da pontuação
      ↓
Acúmulo dos pontos
      ↓
Nova escolha ou saída
```

## ▶️ Como executar

É necessário ter Node.js e `prompt-sync` disponíveis no ambiente. Depois, execute `desafio22.js` pelo terminal.

## 💡 Aprendizados

O desafio demonstra por que funções são importantes para **decompor problemas**. Em vez de um quiz inteiro escrito como um único bloco, cada tema passa a ser uma unidade independente com uma responsabilidade clara.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
