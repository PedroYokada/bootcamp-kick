# 🎞️ Desafio 29 — Carrossel com JavaScript puro

## 📌 Sobre o projeto

Este exercício implementa um **carrossel de imagens utilizando JavaScript puro**, sem framework ou biblioteca específica para o componente. O carrossel possui três jogos, controles de anterior/próximo e indicadores que permitem acessar diretamente uma posição.

## 🎯 Objetivo

Praticar manipulação do DOM, funções, índices, laços de repetição e mudança dinâmica de classes e estilos.

## 🧠 Conceitos praticados

### Estado do carrossel

A variável:

```javascript
var index_fotos = 1;
```

armazena qual slide deve estar ativo. Esse valor funciona como parte do **estado da interface**, isto é, uma informação que determina o que deve ser exibido naquele momento.

### Funções com parâmetros

`plus_fotos(n)` recebe um deslocamento. Quando `n` vale `1`, avança; quando vale `-1`, retorna.

`current_fotos(n)` recebe diretamente o número do slide que deve ser exibido.

As duas funções encaminham o resultado para `mostrar_fotos()`.

### Manipulação do DOM por classe

O código utiliza:

```javascript
document.getElementsByClassName("games")
document.getElementsByClassName("ponto")
```

para obter coleções dos slides e indicadores. O JavaScript então percorre esses elementos e altera sua apresentação.

### Laços `for`

Os laços escondem todas as imagens e removem a classe `active` dos indicadores antes de selecionar o item correto. Esse padrão — limpar estados anteriores e ativar um novo estado — é comum em componentes de interface.

### Alteração dinâmica de CSS

A propriedade:

```javascript
fotos[i].style.display = "none";
```

esconde os slides. Em seguida, somente o slide selecionado recebe `display = "block"`.

A classe `active` também é adicionada ao indicador atual para permitir uma diferenciação visual definida no CSS.

### Índices e diferença entre posição visual e índice do array

O carrossel trabalha visualmente com posições `1`, `2` e `3`, mas as coleções obtidas pelo DOM são indexadas a partir de `0`. Por isso aparece:

```javascript
fotos[index_fotos - 1]
```

O `- 1` converte a numeração visual para o índice real da coleção.

### Navegação circular

Quando o índice ultrapassa a quantidade de slides, ele retorna para `1`. Quando fica abaixo de `1`, recebe `fotos.length`. Assim, o carrossel continua funcionando em ciclo.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript puro
- DOM

## 📂 Estrutura

```text
desafio-29-kick/
├── imagens/
├── desafio29.html
├── desafio29.css
└── desafio29.js
```

## ⚙️ Fluxo do componente

```text
Clique no controle
      ↓
index_fotos é alterado
      ↓
mostrar_fotos()
      ↓
esconde todos os slides
      ↓
remove estados ativos
      ↓
exibe o slide selecionado
```

## ▶️ Como executar

Abra `desafio29.html` no navegador e utilize as setas ou os indicadores abaixo do carrossel.

## 💡 Aprendizados

Ao construir o componente manualmente, o exercício ajuda a compreender o que bibliotecas e frameworks normalmente abstraem: controle de índice, seleção de elementos, visibilidade, classes e eventos de navegação.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
