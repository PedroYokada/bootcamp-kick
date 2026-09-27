# 🎮 Desafio 13–14 — Mega Man X e Responsividade

## 📌 Sobre o projeto

Este desafio apresenta uma página temática de **Mega Man X** criada com HTML e CSS. O principal avanço técnico em relação aos exercícios anteriores é a preocupação com **responsividade**, adaptando parte da interface para diferentes larguras de tela.

A página possui imagem principal, conteúdo textual, galeria de personagens, tabela e rodapé, além de arquivos de favicon.

## 🎯 Objetivo

Praticar construção de layout responsivo utilizando **Flexbox, CSS Grid e media queries**, mantendo o conteúdo organizado em telas maiores e menores.

## 🧠 Conceitos praticados

### Responsividade

Um site responsivo modifica sua apresentação de acordo com o espaço disponível. O projeto utiliza a meta tag `viewport` no HTML e regras `@media` no CSS para alterar estilos quando a largura da tela chega a determinados limites.

Existem ajustes para larguras de **768px** e **480px**. Esses pontos são chamados de **breakpoints**.

### Media queries

Uma regra como:

```css
@media screen and (max-width: 480px) {
    /* estilos aplicados em telas menores */
}
```

permite substituir ou adaptar propriedades apenas quando a condição definida é atendida.

### CSS Grid

A galeria utiliza:

```css
display: grid;
grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
```

O **CSS Grid** organiza elementos em linhas e colunas. `auto-fill` tenta criar a quantidade de colunas que cabe no espaço e `minmax()` estabelece limites de tamanho. Isso ajuda as imagens a se reorganizarem conforme a largura disponível.

### Flexbox

Algumas áreas usam `display: flex`, `justify-content` e `align-items`. O **Flexbox** é útil para alinhar e distribuir elementos em uma direção principal, como linha ou coluna.

### Box model

Propriedades como `margin`, `padding`, `width`, `height` e `box-sizing` participam do chamado **box model**, o modelo usado pelo navegador para calcular o espaço ocupado por cada elemento.

### Tipografia e identidade visual

O projeto utiliza a família **Segoe UI** em diferentes áreas, além de uma paleta de cores e imagens temáticas. Tipografia, cores e espaçamento ajudam a manter unidade visual entre os elementos.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- Flexbox
- CSS Grid
- media queries
- favicons

## 📂 Estrutura principal

```text
desafio-13-kick/
├── icons/
├── desafio13.html
├── desafio13.css
├── paleta de cores.png
└── imagens dos personagens
```

## ⚙️ Como funciona

`desafio13.html` contém o conteúdo e referencia `desafio13.css`. O CSS define o layout padrão e, nas media queries, muda dimensões, tamanho de texto e organização da galeria para telas menores.

## 💡 Aprendizados

Este exercício registra uma mudança importante na jornada de Front-End: a interface deixa de ser pensada apenas para uma largura fixa e passa a considerar diferentes dispositivos. Flexbox e Grid resolvem problemas de layout de maneiras diferentes e podem ser utilizados em conjunto.

## ▶️ Como executar

Abra `desafio13.html` no navegador. Para observar a responsividade, altere a largura da janela ou utilize o modo de dispositivos das ferramentas de desenvolvedor do navegador.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
