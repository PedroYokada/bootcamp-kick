# 🐞 Desafio 25 — Debugging: correção de erros em JavaScript

## 📌 Sobre o projeto

Este desafio parte de um código propositalmente problemático e propõe uma tarefa comum no desenvolvimento de software: **identificar erros, entender suas causas e corrigi-los sem alterar a finalidade do programa**.

A aplicação mantém uma lista de desenhos animados, mostra os itens no HTML e permite substituir valores da lista através de um campo de texto.

## 🎯 Objetivo

Praticar **debugging**, leitura de código e identificação de erros de sintaxe, chamadas de métodos, manipulação do DOM, arrays e execução de funções.

## 🧠 Conceitos praticados

### Debugging

**Debugging** é o processo de investigar por que um programa não está funcionando como esperado. Normalmente envolve:

1. observar o erro ou comportamento incorreto;
2. localizar o trecho responsável;
3. compreender o que aquele trecho deveria fazer;
4. corrigir uma causa por vez;
5. testar novamente.

Este exercício registra no próprio JavaScript várias correções encontradas durante essa investigação.

### Arrays

`desenhosAnimados` é um array contendo nomes de desenhos. Arrays armazenam vários valores em uma sequência e cada posição possui um índice iniciado em `0`.

O programa substitui um item por meio de:

```javascript
desenhosAnimados[indiceSubstituicao] = novoDesenho.value;
```

### Percurso com `forEach()`

`forEach()` percorre os elementos do array. Para cada desenho, o programa cria um novo `<li>` e o adiciona à lista exibida na página.

### Manipulação do DOM

O exercício utiliza diferentes operações do DOM:

- `getElementsByClassName()` para localizar a lista;
- `getElementById()` para localizar o campo de entrada;
- `document.createElement('li')` para criar elementos;
- `textContent` para definir texto;
- `appendChild()` para inserir o item no HTML;
- `innerHTML = ''` para limpar a lista antes de reconstruí-la.

### Validação de entrada

```javascript
novoDesenho.value.trim() !== ''
```

`trim()` remove espaços nas extremidades. A comparação impede que uma entrada vazia seja utilizada na lista.

### Operador módulo `%`

```javascript
indiceSubstituicao = (indiceSubstituicao + 1) % desenhosAnimados.length;
```

O operador `%` retorna o resto de uma divisão. Aqui ele cria um índice circular: ao ultrapassar a última posição do array, a próxima substituição retorna ao início.

### `window.onload`

`window.onload = exibirLista` registra a função para ser executada depois que a página terminar de carregar, garantindo que a lista inicial seja montada.

## 🔎 Tipos de erros trabalhados

O material registra correções relacionadas a:

- sintaxe de array;
- strings sem aspas;
- nome incorreto de método do DOM;
- criação de elementos;
- condição do `if`;
- diferença entre referenciar e executar uma função;
- uso de `.value` em inputs;
- associação correta da função ao carregamento da página;
- diferença entre `id` e `class` para localizar elementos.

## 🛠️ Tecnologias utilizadas

- HTML5
- JavaScript
- DOM
- debugging

## ▶️ Como executar

Abra `desafio25.html` em um navegador. O arquivo carrega `desafio25.js` e monta a lista automaticamente.

## 💡 Aprendizados

O principal aprendizado não é apenas “fazer funcionar”, mas desenvolver a capacidade de **ler mensagens, comparar intenção e implementação e testar hipóteses de correção**. Essa habilidade é utilizada continuamente em qualquer área de programação.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
