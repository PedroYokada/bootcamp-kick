# 🅱️ Desafio 30–31 — Interface com Bootstrap

## 📌 Sobre o projeto

Este desafio utiliza **Bootstrap 5.3.3** para montar uma página temática do Xbox sem criar um arquivo CSS próprio. A interface usa componentes e classes utilitárias do framework para implementar navegação, carrossel, cards, grid, botão de busca, tipografia e rodapé visual.

A atividade também registra uma etapa de preparação para o Projeto Web Xbox desenvolvido posteriormente no Bootcamp.

## 🎯 Objetivo

Conhecer como um framework CSS pode acelerar a construção de interfaces reutilizando componentes e estilos previamente definidos.

## 🧠 Conceitos praticados

### O que é Bootstrap?

**Bootstrap** é um framework de Front-End que disponibiliza CSS e JavaScript prontos para componentes comuns de interface. Em vez de criar do zero todas as regras de uma navbar, card ou carrossel, o desenvolvedor aplica classes previstas pelo framework.

Neste projeto, Bootstrap é carregado através de **CDN**, ou seja, os arquivos do framework são obtidos de servidores externos quando a página é aberta.

### Navbar responsiva

A navegação utiliza classes como:

```text
navbar
navbar-expand-lg
navbar-toggler
collapse
navbar-collapse
```

O componente consegue recolher e expandir partes da navegação em diferentes larguras. A funcionalidade de abrir/fechar depende do `bootstrap.bundle.min.js` carregado no HTML.

### Data attributes

Atributos como `data-bs-toggle`, `data-bs-target` e `data-bs-slide` configuram comportamentos dos componentes Bootstrap diretamente no HTML.

### Carousel

O componente `carousel` organiza várias imagens em uma área de destaque. As classes e atributos do framework cuidam do estado ativo e dos controles anterior/próximo.

Esse exercício é interessante porque acontece depois de um desafio em que um carrossel foi construído manualmente com JavaScript. Aqui, o Bootstrap encapsula grande parte dessa lógica.

### Cards

Os quatro jogos são apresentados através do componente `card`. Um card agrupa conteúdo relacionado — imagem, título e outras informações — dentro de uma unidade visual reutilizável.

### Sistema de Grid

A estrutura:

```text
container → row → col-sm-3
```

faz parte do **Grid System** do Bootstrap. `container` limita e organiza a área, `row` cria uma linha e as classes `col-*` definem como o espaço é dividido entre colunas.

### Utility classes

Classes como `bg-secondary`, `text-light`, `text-center`, `d-flex`, `justify-content-center`, `mt-5` e `w-100` são **classes utilitárias**. Cada uma resolve uma necessidade pequena sem exigir uma regra CSS personalizada.

### Componentes x personalização

O material original registra uma percepção importante do exercício: componentes prontos aceleram desenvolvimento e oferecem comportamento responsivo, enquanto CSS próprio oferece maior liberdade de personalização. As duas abordagens podem ser utilizadas de forma complementar em outros projetos.

## 🛠️ Tecnologias utilizadas

- HTML5
- Bootstrap 5.3.3
- Bootstrap JavaScript Bundle
- CDN

## 📂 Estrutura

```text
desafio-31-kick/
├── imagens/
├── desafio31.html
└── README.md
```

Não existe CSS próprio neste desafio, respeitando a proposta da atividade.

## ▶️ Como executar

Abra `desafio31.html` em um navegador com acesso à internet. A conexão é necessária para carregar os arquivos do Bootstrap disponibilizados pela CDN.

## 💡 Aprendizados

O desafio mostra a diferença entre **construir um componente manualmente** e **utilizar uma implementação fornecida por um framework**. Também introduz uma forma de desenvolvimento baseada em composição de classes e componentes reutilizáveis.

## 🔗 Relação com o Projeto Xbox

Esta página se inspira visualmente na ideia que posteriormente aparece no projeto Xbox consolidado neste repositório.

- [Ver protótipo do Projeto Xbox](../../projeto-xbox/projeto-xbox-figma/)
- [Ver implementação Web do Projeto Xbox](../../projeto-xbox/projeto-xbox-web/)
- [Voltar ao repositório principal](../../README.md)
