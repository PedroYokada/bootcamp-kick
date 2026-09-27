# 🎮 Projeto Individual Web — Xbox | HTML, CSS e JavaScript

## 📌 Sobre o projeto

Esta pasta contém a **implementação Web** do Projeto Individual desenvolvido durante o Bootcamp Kick. A interface foi planejada anteriormente no Figma e depois transformada em páginas utilizando HTML, CSS e JavaScript.

O projeto cresceu por etapas. O README original registrava uma primeira entrega com tela principal e login e, posteriormente, atualizações em páginas como assinatura e “sobre nós”. Na versão preservada atualmente também existem cadastro, acessórios, Game Pass e diferentes interações em JavaScript.

## 🎯 Objetivo

Aplicar em um projeto maior os conhecimentos acumulados durante o Bootcamp: estruturação de páginas, estilização, responsividade, manipulação do DOM, navegação entre telas, carrossel, formulários e consumo de API.

## 📂 Principais telas

```text
projeto-xbox-web/
├── index.html                  # login
├── index.css
├── login.js
└── telainicial/
    ├── index.html              # página principal
    ├── index.css
    ├── index.js
    ├── acessorios/
    ├── assinatura-gamepass/
    ├── cadastro/
    ├── sobre-nos/
    └── tela-gamepass/
```

Cada área mantém seus próprios arquivos e assets, refletindo a separação da aplicação em diferentes páginas.

## 🧠 Conceitos técnicos praticados

### HTML e organização em múltiplas páginas

O HTML define a estrutura das telas. Como o projeto não utiliza um framework de aplicação de página única, cada área é representada por um arquivo HTML próprio e a navegação ocorre através de caminhos entre esses arquivos.

### CSS e responsividade

Os arquivos CSS controlam cores, tipografia, dimensões, posicionamento e adaptação das telas. O projeto preserva o processo de aprendizagem original, inclusive as observações registradas durante a primeira entrega sobre dificuldades de responsividade em resoluções menores.

### Navegação com `window.location.href`

Funções como:

```javascript
function acessorios() {
  window.location.href = "acessorios/index.html";
}
```

mudam a página atual do navegador. A mesma estratégia é utilizada para acessar jogos, cadastro, voltar para outras telas e realizar logout visual.

### Eventos e DOM

Na tela principal, o código espera `DOMContentLoaded` para registrar um evento de clique no botão do menu. Depois utiliza:

```javascript
navInicial.classList.toggle("show");
```

`classList.toggle()` adiciona uma classe quando ela não existe e remove quando já existe. Isso permite abrir e fechar partes da interface modificando o estado visual pelo CSS.

### Carrossel manual

A página principal e a tela Game Pass possuem lógica de carrossel semelhante ao Desafio 29. O JavaScript:

- mantém um índice do slide atual;
- obtém os elementos por classe;
- esconde os slides;
- controla os limites da navegação;
- adiciona e remove a classe `active`;
- exibe apenas o item selecionado.

Esse reaproveitamento mostra como um conceito praticado em um exercício menor pode ser incorporado a um projeto maior.

### Validação da tela de login

`login.js` verifica se os dois campos possuem conteúdo após `trim()`. Se ambos estiverem preenchidos, a página redireciona para a tela inicial; caso contrário, apresenta um alerta.

> Esta lógica é uma **validação no Front-End** e não corresponde a um sistema real de autenticação: o código preservado não consulta banco de dados, servidor ou credenciais armazenadas.

### Formulário de cadastro e ViaCEP

A tela de cadastro consulta a API ViaCEP com `fetch()` quando o campo CEP perde o foco. A resposta JSON é utilizada para preencher rua, bairro, cidade e UF.

Essa parte envolve:

- evento `blur`;
- requisição HTTP com `fetch()`;
- Promises com `.then()`;
- conversão de resposta para JSON;
- manipulação do DOM;
- tratamento de falhas com `.catch()`;
- limpeza de campos;
- expressão regular para validar e-mail.

### jQuery Mask

O cadastro também usa jQuery Mask para formatar CEP e telefone durante a digitação. Para telefone, o script escolhe a máscara de acordo com a quantidade de dígitos encontrada.

### Caminhos relativos

Como o projeto possui várias subpastas, referências como:

```javascript
window.location.href = "../../telainicial/index.html";
```

demonstram o uso de **caminhos relativos**. `../` significa subir um nível na estrutura de diretórios.

## 🛠️ Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- DOM
- Fetch API
- ViaCEP
- JSON
- RegExp
- jQuery
- jQuery Mask
- Figma na etapa de prototipação

## ⚙️ Fluxo geral

```text
Protótipo no Figma
        ↓
Tela de login
        ↓
Tela inicial
  ┌─────┼───────────────┐
  ↓     ↓               ↓
Cadastro  Acessórios   Game Pass
  ↓                     ↓
ViaCEP                Carrosséis
```

## ▶️ Como executar

Abra o `index.html` localizado na raiz desta pasta. A navegação é feita pelos próprios arquivos HTML. Algumas funcionalidades, especialmente a consulta de CEP e bibliotecas carregadas externamente, precisam de conexão com a internet.

Por se tratar de um projeto educacional preservado, a execução direta por arquivo pode depender das permissões e políticas atuais do navegador. Um servidor local simples também pode ser utilizado para testar as páginas.

## 💡 Aprendizados

Este projeto reúne conteúdos que anteriormente apareciam separados em exercícios menores. É possível observar a progressão de **layout → responsividade → JavaScript → eventos → carrossel → formulário → API** dentro de uma única aplicação com múltiplas telas.

## 🔗 Navegação

- [Ver a etapa de prototipação no Figma](../projeto-xbox-figma/)
- [Voltar ao repositório principal](../../README.md)
