# 📰 Desafio 17 — Layout inspirado na IGN

## 📌 Sobre o projeto

O Desafio 17 reproduz uma página temática inspirada na IGN para praticar **Flexbox, menu dropdown e responsividade**. O layout possui cabeçalho, navegação para consoles, botão de entrada, área de categorias, dropdown e uma galeria de imagens.

## 🎯 Objetivo

Concluir uma interface iniciada em aula utilizando Flexbox e implementar pelo menos um menu dropdown que continuasse utilizável em diferentes tamanhos de tela.

## 🧠 Conceitos praticados

### Flexbox

Diversas áreas utilizam `display: flex`. O Flexbox organiza os elementos de um contêiner e oferece propriedades como:

- **`justify-content`**: distribui os itens no eixo principal;
- **`align-items`**: controla o alinhamento no eixo transversal;
- **`flex-grow`**: permite que um item ocupe espaço disponível;
- **`flex-wrap`**: permite que os itens quebrem para outra linha quando necessário.

No projeto, Flexbox é utilizado no cabeçalho, na área de categorias, no menu e na distribuição das imagens.

### Menu dropdown

O dropdown é construído somente com HTML e CSS. A lista interna começa com:

```css
display: none;
```

Quando o mouse passa sobre `.dropdown-ign`, a regra:

```css
.dropdown-ign:hover .dropdown-lista-ign {
  display: block;
}
```

torna o menu visível. Isso demonstra o uso da pseudo-classe **`:hover`** para criar comportamento visual sem JavaScript.

### Posicionamento

O contêiner do dropdown utiliza `position: relative` e sua lista usa `position: absolute`. Essa relação permite posicionar a lista em relação ao componente que a contém. `z-index` ajuda a garantir que o menu apareça acima de outros elementos.

### Responsividade

O CSS contém uma media query para telas de até **480px**. Nessa condição, a galeria passa a utilizar **CSS Grid**, a navegação recebe `flex-wrap` e alguns tamanhos são ajustados.

### CSS Grid

Na versão de tela menor, as imagens são reorganizadas com `display: grid` e `grid-template-columns`. O Grid é adequado para estruturas bidimensionais em que os itens precisam ocupar linhas e colunas de maneira adaptável.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- Flexbox
- CSS Grid
- media queries
- dropdown com CSS

## 📂 Estrutura

```text
desafio-17-kick/
├── IMAGENS/
├── desafio17.html
├── desafio17.css
└── README.md
```

## ⚙️ Como funciona

O HTML define as áreas da página e as imagens. O CSS distribui os elementos com Flexbox, controla o dropdown e adiciona uma adaptação para telas pequenas. Não existe JavaScript neste desafio; a interação do dropdown é obtida com CSS.

## 💡 Aprendizados

O exercício combina três conceitos importantes de Front-End: **layout flexível, interação por estados do CSS e adaptação por breakpoint**. É uma etapa intermediária entre páginas estáticas simples e interfaces mais dinâmicas que posteriormente passam a usar JavaScript.

## ▶️ Como executar

Abra `desafio17.html` no navegador. Para testar o dropdown, passe o mouse sobre o item indicado no menu. Para observar a media query, reduza a largura da janela.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
