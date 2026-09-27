# 🌱 Desafios iniciais — HTML e Lógica

## 📌 Sobre esta etapa

Esta pasta preserva alguns dos primeiros exercícios realizados no Bootcamp Kick. Os arquivos registram dois momentos importantes do início da aprendizagem: o primeiro contato com a estrutura de uma página HTML e um exercício de lógica desenvolvido em Portugol.

O objetivo desta documentação é explicar o que cada exercício pratica sem modernizar ou reescrever os códigos originais.

## 🎯 Objetivos praticados

- compreender a estrutura básica de um documento HTML;
- utilizar elementos simples de conteúdo e interação;
- começar a organizar informações em uma página web;
- trabalhar entrada e saída de dados em lógica de programação;
- utilizar variáveis, condições, repetição e seleção de opções.

## 📂 Exercícios

### Atividade 21-03 — Primeiro exercício de HTML

O arquivo `index.html` contém uma página simples com texto, link, lista, campo de entrada, botão e imagem. É um exercício introdutório para reconhecer como diferentes elementos são escritos dentro do `<body>`.

#### Conceitos técnicos

**`<!DOCTYPE html>`** informa ao navegador que o documento utiliza HTML5.

**`<head>`** reúne configurações da página, como codificação de caracteres, viewport e título exibido na aba do navegador.

**`<body>`** contém aquilo que aparece na página. Neste exercício aparecem elementos como `<p>`, `<a>`, `<ul>`, `<li>`, `<input>`, `<button>` e `<img>`.

**Atributos HTML** acrescentam informações às tags. O `href`, por exemplo, indica o destino de um link, enquanto `src` informa o caminho da imagem.

O exercício também utiliza estilos diretamente no HTML por meio do atributo `style`. Essa técnica é chamada de **CSS inline** e foi usada aqui para alterar cores de forma simples durante o primeiro contato com estilização.

### Desafio 3-4 — Calculadora em Portugol

O arquivo `.por` implementa uma calculadora textual. O programa solicita dois números e permite escolher entre soma, subtração, multiplicação, divisão ou saída.

#### Conceitos técnicos

**Variáveis** armazenam valores que serão usados durante a execução. O exercício utiliza `v1`, `v2` e `res` como valores numéricos e `opcao` para representar a escolha do usuário.

**Entrada e saída** são realizadas com `leia()` e `escreva()`. O primeiro recebe dados do usuário e o segundo apresenta mensagens e resultados.

**Estrutura de repetição `enquanto`** mantém o programa em execução até que a opção de saída seja escolhida.

**Estrutura `escolha/caso`** direciona a execução para uma operação diferente de acordo com a opção informada. O conceito é semelhante ao `switch/case` encontrado em várias linguagens de programação.

**Estrutura condicional `se/senao`** é utilizada na parte da divisão para tratar o caso em que não deve ser realizada uma divisão inválida.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS inline
- Portugol

## 💡 Aprendizados

Estes arquivos representam uma etapa inicial da jornada: primeiro entender como uma página é estruturada e, paralelamente, desenvolver raciocínio lógico com variáveis, decisões e repetição. Esses fundamentos aparecem novamente nos exercícios posteriores do Bootcamp em HTML, CSS, JavaScript e Python.

## ▶️ Como visualizar

O exercício HTML pode ser aberto diretamente no navegador pelo arquivo `index.html`. O arquivo `.por` precisa de um ambiente compatível com Portugol para ser executado.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de fundamentos](../)
