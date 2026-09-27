# 🗳️ Desafio 19–20 — Interação com JavaScript

## 📌 Sobre o projeto

Este exercício cria uma página de **votação fictícia** com quatro opções de candidatos, voto nulo e voto em branco. Ao selecionar uma opção, a página informa a escolha através de um `alert`. Também existem botões que alteram a cor de fundo da página.

O foco técnico está na introdução do JavaScript como camada de comportamento de uma página que já possui HTML e CSS.

## 🎯 Objetivo

Praticar eventos, funções e manipulação do DOM, permitindo que ações realizadas pelo usuário produzam mudanças imediatas na interface.

## 🧠 Conceitos praticados

### Funções JavaScript

O código declara funções como `AlterarFundo()`, `AlterarFundo2()` e `votacao()`. Uma **função** agrupa instruções que podem ser executadas quando necessário.

### Eventos

Os elementos utilizam `onclick` para chamar funções quando o usuário clica. Eventos são a base da interação no navegador: clique, digitação, envio de formulário e movimento do mouse são exemplos de acontecimentos aos quais o JavaScript pode reagir.

### Radio buttons

Os inputs de votação usam `type="radio"` e compartilham o mesmo atributo `name="candidato"`. Isso faz com que apenas uma alternativa do grupo possa ficar selecionada por vez.

### DOM

**DOM (Document Object Model)** é a representação da página que o JavaScript consegue consultar e modificar.

O projeto utiliza:

```javascript
document.querySelector('input[name="candidato"]:checked')
```

para localizar a opção marcada e `document.body` para acessar o corpo da página.

### Alteração de estilos pelo JavaScript

As funções de fundo modificam `background.style.background`. Isso mostra que o JavaScript pode alterar propriedades visuais durante a execução sem recarregar a página.

### Condicional

Em `votacao()`, um `if` verifica se alguma opção foi encontrada antes de mostrar a mensagem. A condicional permite executar uma instrução somente quando uma condição é satisfeita.

### Responsividade com CSS

O arquivo `index.css` possui media queries para **768px** e **480px**, reduzindo fontes e dimensões em telas menores.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- manipulação do DOM
- eventos
- media queries

## ⚙️ Como funciona

1. O usuário seleciona uma opção de voto.
2. O evento `onclick` executa `votacao()`.
3. O JavaScript procura o radio button marcado.
4. O valor escolhido é exibido em um `alert`.
5. Os botões adicionais chamam funções que modificam a cor de fundo do `body`.

## 💡 Aprendizados

Este exercício marca a passagem de uma página apenas visual para uma página **interativa**. HTML descreve os controles, CSS define a aparência e JavaScript reage às ações do usuário e modifica o estado da interface.

## ▶️ Como executar

Abra `index.html` em um navegador. Não há dependências externas.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
