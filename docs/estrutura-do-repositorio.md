# 🗂️ Estrutura do repositório

Este documento explica como o repositório `bootcamp-kick` foi organizado após a consolidação dos projetos.

## Convenção de nomes

As pastas utilizadas para organizar o portfólio seguem **kebab-case**:

- letras minúsculas;
- palavras separadas por hífen;
- sem espaços na estrutura principal;
- sem mistura desnecessária de maiúsculas e minúsculas.

Exemplos:

```text
fundamentos-web
javascript-front-end
desafio-27-kick
projeto-xbox-web
```

A estrutura interna dos projetos históricos pode manter nomes antigos, espaços e outros padrões quando a mudança puder quebrar links relativos, caminhos de imagens, CSS, JavaScript ou referências originais.

## Estrutura principal

```text
bootcamp-kick/
├── fundamentos-web/
│   ├── desafios-iniciais/
│   ├── desafio-05-kick/
│   ├── desafio-07-08-kick/
│   ├── desafio-09-10-figma/
│   ├── desafio-11-kick/
│   ├── desafio-13-kick/
│   └── desafio-17-kick/
│
├── javascript-front-end/
│   ├── desafio-19-kick/
│   ├── desafio-22-kick/
│   ├── desafio-23-kick/
│   ├── desafio-25-kick/
│   ├── desafio-27-kick/
│   ├── desafio-29-kick/
│   ├── desafio-31-kick/
│   └── parada-34-kick/
│
├── projeto-xbox/
│   ├── projeto-xbox-figma/
│   └── projeto-xbox-web/
│
├── wordpress/
│   └── modulo-iv-wordpress/
│
├── python/
│   └── modulo-v-python/
│
├── docs/
│   ├── estrutura-do-repositorio.md
│   ├── github-about.md
│   ├── mapa-de-origens.md
│   ├── relatorio-de-migracao.md
│   └── revisao-manual.md
│
├── .gitignore
└── README.md
```

## Critério de organização

### `fundamentos-web/`

Reúne atividades iniciais, HTML, CSS, prototipação, UI e os primeiros trabalhos de responsividade.

### `javascript-front-end/`

Agrupa exercícios que passam a utilizar JavaScript, funções, depuração, APIs, componentes dinâmicos e Bootstrap.

### `projeto-xbox/`

Mantém juntas as duas etapas do projeto web individual: prototipação no Figma e implementação em HTML, CSS e JavaScript.

### `wordpress/`

Contém as atividades do módulo dedicado à construção de portfólio em WordPress.

### `python/`

Contém exercícios de Python, notebooks e o projeto de análise de dados.

### `docs/`

Centraliza documentação sobre a migração, origem dos projetos, convenções e decisões de manutenção.

## Preservação histórica

Os 19 repositórios originais foram consolidados utilizando `git subtree` sem `--squash`. A organização posterior alterou apenas a localização dos arquivos dentro do repositório consolidado; os repositórios antigos permanecem separados no perfil do GitHub.

Não é necessário modernizar os códigos antigos para que eles façam parte do portfólio: eles também servem como registro da evolução técnica ao longo do Bootcamp.
