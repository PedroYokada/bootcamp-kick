# 📮 Desafio 27 — Formulário com API ViaCEP

## 📌 Sobre o projeto

Este desafio implementa um formulário de cadastro com os campos nome, sobrenome, e-mail, CEP, rua, bairro, cidade e estado. Ao sair do campo de CEP, o JavaScript consulta a **API ViaCEP** e preenche automaticamente os campos de endereço quando o CEP é encontrado.

A interface utiliza uma identidade visual inspirada nas cores clássicas do PlayStation.

## 🎯 Objetivo

Praticar formulários HTML, eventos, validação, consumo de API e manipulação do DOM em uma situação próxima de formulários reais de cadastro.

## 🧠 Conceitos praticados

### Formulários HTML

O projeto utiliza `<form>`, `<label>`, `<input>` e `<button>`. O atributo `required` sinaliza campos obrigatórios e `readonly` impede edição manual nos campos preenchidos pela consulta de CEP.

### Eventos

O JavaScript registra um evento `blur` no campo `#cep`. O evento ocorre quando o elemento perde o foco. Assim, a consulta é iniciada depois que o usuário termina de preencher o CEP e segue para outro campo.

### Limpeza do CEP com expressão regular

```javascript
this.value.replace(/\D/g, "")
```

A expressão `/\D/g` localiza caracteres que não são dígitos. `replace()` remove esses caracteres antes de montar a URL da API.

### `fetch()` e requisição HTTP

```javascript
fetch(`https://viacep.com.br/ws/${cep}/json/`)
```

`fetch()` realiza uma requisição HTTP. O CEP é inserido dinamicamente na URL usando template literal. A resposta é convertida para JSON com `response.json()`.

### JSON

**JSON** é um formato textual muito utilizado para troca de dados entre aplicações. A resposta da ViaCEP contém propriedades como `logradouro`, `bairro`, `localidade` e `uf`, que são utilizadas para preencher o formulário.

### Promises e `.then()`

`fetch()` trabalha de forma assíncrona e devolve uma Promise. Os `.then()` definem o que fazer quando a resposta chega e quando o JSON fica disponível.

### Tratamento de erro com `.catch()`

Se a requisição falhar, `.catch()` apresenta uma mensagem, registra o erro no console e limpa os campos de endereço. O código também trata a propriedade `data.erro`, utilizada quando o serviço não encontra o CEP informado.

### Manipulação do DOM

`document.getElementById()` é usado para localizar inputs e atribuir valores retornados pela API diretamente aos campos da página.

### Validação de e-mail com RegExp

`validacaoEmail()` utiliza uma **expressão regular (RegExp)** para verificar se o texto digitado segue um padrão básico de e-mail. A mensagem “E-mail inválido” é inserida no elemento `#erro-email` quando o padrão não é atendido.

### jQuery Mask

O HTML importa jQuery e o plugin **jQuery Mask** por CDN. O código aplica a máscara `00000-000` ao CEP para auxiliar a digitação no formato esperado.

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

## ⚙️ Fluxo da consulta

```text
Usuário informa o CEP
        ↓
evento blur
        ↓
remove caracteres não numéricos
        ↓
fetch para ViaCEP
        ↓
resposta convertida em JSON
        ↓
preenchimento de rua, bairro, cidade e UF
```

## ▶️ Como executar

Abra `desafio27.html` em um navegador com acesso à internet. A internet é necessária para carregar jQuery/jQuery Mask e consultar a ViaCEP.

## 💡 Aprendizados

O exercício demonstra uma integração importante: a página deixa de trabalhar apenas com dados definidos localmente e passa a **consumir informações de um serviço externo**. Isso introduz conceitos fundamentais para aplicações web que se comunicam com APIs.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
- [Ver os demais projetos de JavaScript e Front-End](../)
