# 📊 Desafio 07–08 — Tabela de produtos com HTML e CSS

## 📌 Sobre o projeto

Este exercício apresenta uma **tabela de produtos** contendo código, nome e preço. O foco é praticar a estrutura de tabelas no HTML e aplicar estilização com um arquivo CSS externo.

## 🎯 Objetivo

Organizar dados tabulares de forma visualmente compreensível e praticar a relação entre **HTML**, responsável pela estrutura, e **CSS**, responsável pela apresentação.

## 🧠 Conceitos praticados

### Tabelas em HTML

A tabela utiliza:

- **`<table>`**: elemento principal da tabela;
- **`<tr>`**: representa uma linha;
- **`<th>`**: cria células de cabeçalho;
- **`<td>`**: cria células comuns de dados;
- **`colspan`**: permite que uma célula ocupe mais de uma coluna.

No projeto, `colspan="3"` é utilizado no título “Tabela de produtos”, fazendo com que esse cabeçalho ocupe as três colunas existentes.

### Classes CSS

As classes `.green` e `.white` são utilizadas para aplicar estilos diferentes às células. Isso demonstra que uma mesma regra CSS pode ser reutilizada em vários elementos sem repetir toda a estilização.

### Centralização com Flexbox

A classe `.centralizar3` utiliza:

```css
display: flex;
justify-content: center;
align-items: center;
```

O **Flexbox** é um modelo de layout do CSS. Aqui ele é utilizado para centralizar a tabela no espaço disponível.

### Aparência da tabela

A classe `.table4` controla largura, altura, alinhamento do texto e bordas. `border-collapse: collapse` faz com que as bordas das células sejam apresentadas de maneira unificada, evitando o espaço padrão entre elas.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- Flexbox

## 📂 Estrutura

```text
desafio-07-08-kick/
├── desafio0708.html
└── desafio0708.css
```

## ⚙️ Como funciona

O HTML contém todos os produtos de forma estática. Não há JavaScript nem banco de dados neste exercício: os valores são escritos diretamente nas células da tabela. O CSS define a identidade visual, centralização e diferenciação entre cabeçalhos e dados.

## 💡 Aprendizados

O exercício introduz uma ideia importante para desenvolvimento web: **escolher a estrutura HTML adequada para o tipo de informação**. Quando os dados possuem linhas e colunas relacionadas, uma tabela é mais apropriada do que posicionar textos manualmente pela página.

## ▶️ Como executar

Abra `desafio0708.html` em qualquer navegador moderno. O arquivo carregará automaticamente `desafio0708.css`.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
