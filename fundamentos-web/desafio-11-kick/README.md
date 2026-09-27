# 👾 Desafio 11–12 — Space Invaders

## 📌 Sobre o projeto

Este exercício desenvolve uma página temática de **Space Invaders** utilizando HTML e CSS. O código reúne cabeçalho, navegação, textos, imagem, uma tabela com informações do jogo, rodapé e diferentes arquivos de favicon.

## 🎯 Objetivo

Praticar a organização de uma página com elementos HTML adequados ao tipo de conteúdo e separar a estrutura do documento da estilização visual realizada no CSS.

## 🧠 Conceitos praticados

### HTML semântico

O projeto utiliza elementos como `header`, `nav` e `footer`. Essas tags dão significado às áreas da página e tornam a estrutura mais compreensível do que utilizar apenas elementos genéricos.

### Tabelas

A página possui uma tabela construída com `table`, `tr`, `th` e `td`. Esse conjunto de elementos é apropriado quando as informações possuem relação entre linhas e colunas.

### Links e navegação

Elementos `<a>` são utilizados para representar opções de navegação. Um link é definido principalmente pelo atributo `href`, que indica o destino a ser aberto.

### Imagens e texto alternativo

O elemento `<img>` incorpora recursos visuais à página. O atributo `alt`, quando utilizado, fornece uma descrição textual da imagem e contribui para acessibilidade e situações em que o arquivo visual não pode ser carregado.

### CSS externo

O HTML importa `index.css` por meio da tag `<link>`. Dessa forma, o HTML permanece responsável pela estrutura enquanto o CSS controla a apresentação.

### Favicon

A pasta `icon/` contém versões de favicon para diferentes tamanhos e dispositivos, além de um `site.webmanifest`. O **favicon** é o pequeno ícone associado ao site que pode aparecer na aba do navegador, favoritos ou atalhos.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- favicons e Web Manifest

## 📂 Estrutura principal

```text
desafio-11-kick/
├── icon/
├── index.html
├── index.css
└── space.jpg
```

## ⚙️ Como funciona

`index.html` organiza todo o conteúdo da página e referencia `index.css` para a aparência. Os recursos presentes em `icon/` configuram a identidade visual do site no navegador, enquanto `space.jpg` é utilizado como imagem temática.

## 💡 Aprendizados

O desafio ajuda a avançar de páginas formadas apenas por elementos isolados para uma estrutura dividida em áreas com funções claras. Também reforça que **semântica HTML e aparência CSS são responsabilidades diferentes**, embora trabalhem juntas na construção da interface.

## ▶️ Como executar

Abra `index.html` em um navegador. Não existem dependências externas ou etapa de instalação.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
