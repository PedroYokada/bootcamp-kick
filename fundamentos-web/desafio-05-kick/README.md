# 🌐 Desafio 05 — HTML, CSS e página temática do Google

## 📌 Sobre o projeto

Esta pasta reúne exercícios introdutórios do Bootcamp Kick e o **Desafio 05**, no qual foi construída uma página temática inspirada no Google. Além da atividade principal, foram preservados exercícios anteriores de HTML e Portugol porque faziam parte do repositório original.

O Desafio 05 possui uma página inicial inspirada visualmente no buscador e uma segunda página com conteúdo sobre a história do Google e algumas de suas contribuições tecnológicas.

## 🎯 Objetivo

Praticar a separação entre estrutura e apresentação de uma página web, utilizando **HTML para organizar o conteúdo** e **CSS para controlar aparência, alinhamento, cores, tipografia e posicionamento**.

## 🧠 Conceitos praticados

### Estrutura HTML

Os arquivos utilizam elementos como `header`, `nav`, `ul`, `li`, `h1`, `h4`, `p`, `img`, `input`, `button` e `a`.

- **`header`** representa a área de cabeçalho da página.
- **`nav`** agrupa elementos relacionados à navegação.
- **`a`** cria links entre páginas.
- **`img`** carrega imagens através do atributo `src`.
- **`input`** representa um campo de entrada de dados.
- **`button`** cria um botão de interface.
- **títulos e parágrafos** organizam o conteúdo textual em diferentes níveis.

### CSS externo

O arquivo `ativgrupo.css` é ligado ao HTML através de `<link rel="stylesheet">`. Isso separa a estrutura da página das regras visuais.

O CSS trabalha com:

- **seletores de classe**, como `.imagem`, `.caixa`, `.btn` e `.p2`;
- **cores de fundo e texto**;
- **largura e altura**;
- **margens e posicionamento**;
- **`display: flex`** para alinhamento de elementos;
- **`justify-content` e `align-items`** para distribuição dos itens;
- **`border-radius`** para arredondamento;
- **`font-family` e `font-size`** para tipografia;
- **pseudo-classe `:hover`** para alterar a aparência de um link quando o mouse passa sobre ele;
- **`transition`** para suavizar a mudança visual no hover.

### Navegação entre páginas

A página sobre a história do Google contém um link de retorno para `ativgrupo.html`. Esse tipo de ligação demonstra o conceito de **caminho relativo**, no qual um arquivo HTML aponta para outro arquivo existente na mesma estrutura do projeto.

## 📂 Estrutura principal

```text
Desafio05/
├── ativgrupo.html
├── historiaG.html
├── ativgrupo.css
├── google.png
└── googlepredio.png
```

O repositório também mantém as pastas dos exercícios iniciais de HTML e Portugol, preservando a evolução original do estudo.

## ⚙️ Como funciona

`ativgrupo.html` funciona como a página inicial e apresenta elementos visuais inspirados no Google. `historiaG.html` apresenta conteúdo textual, navegação e uma imagem relacionada à empresa. Os dois arquivos utilizam o mesmo CSS para manter uma identidade visual em comum.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- Portugol nos exercícios anteriores preservados

## 💡 Aprendizados

O projeto representa a transição de uma página HTML muito simples para uma estrutura com **mais de uma página, arquivo CSS externo, navegação, classes e organização visual**. Essa separação entre HTML e CSS é um fundamento importante para os projetos de Front-End que aparecem nas etapas seguintes do Bootcamp.

## ▶️ Como executar

Abra `Desafio05/ativgrupo.html` em um navegador. Como o projeto é estático, não é necessário servidor ou instalação de dependências.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
