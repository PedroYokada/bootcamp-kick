# 🐍 Módulo V — Python | Bootcamp Kick

## 📌 Sobre o módulo

Esta pasta reúne exercícios, desafios e materiais do módulo de **Python** realizado durante o Bootcamp Kick. Os arquivos mostram uma progressão desde os primeiros testes da linguagem até estruturas de decisão, repetição, coleções, funções, manipulação de arquivos, Jupyter Notebook e um projeto com dados educacionais.

A documentação preserva o caráter de estudo dos arquivos: alguns são exercícios autorais, enquanto outros foram utilizados em aula como exemplos de conceitos. Quando um próprio arquivo registra que não é de autoria do aluno, essa observação deve ser mantida como parte do contexto de aprendizagem.

## 🧭 Jornada de aprendizado

```text
Primeiros códigos
        ↓
Variáveis e tipos de dados
        ↓
Entrada, saída e operadores
        ↓
Condicionais
        ↓
Estruturas de repetição
        ↓
Listas, tuplas, conjuntos e dicionários
        ↓
Funções e retorno
        ↓
Arquivos
        ↓
Jupyter Notebook
        ↓
Exploração de dados
```

## 📚 Conteúdos por etapa

### Parada 42 — Fundamentos da linguagem

Os arquivos desta pasta introduzem conceitos como variáveis, `input()`, operadores e funções simples.

Um dos exemplos de variáveis registra diferentes tipos de dados:

- **`int`** — números inteiros;
- **`float`** — números com parte decimal;
- **`str`** — textos;
- **`bool`** — valores `True` ou `False`;
- **lista** — coleção ordenada e mutável;
- **tupla** — coleção ordenada normalmente utilizada como estrutura imutável;
- **dicionário** — estrutura de chave e valor;
- **set/conjunto** — coleção sem duplicação de elementos.

O próprio arquivo `variaveis.py` informa que foi utilizado como código de explicação e não como produção autoral, o que faz parte do registro pedagógico do módulo.

### Parada 43 — Estruturas de decisão

Nesta etapa aparecem `if`, `elif`, `else` e operadores lógicos. O exercício `imc.py`, por exemplo:

1. recebe peso e altura com `input()`;
2. converte os valores para `float`;
3. calcula `peso / (altura * altura)`;
4. utiliza `round()` para limitar casas decimais;
5. usa uma sequência de condições para classificar o resultado.

O ponto técnico central é que **condicionais controlam qual bloco será executado de acordo com uma expressão booleana**.

### Parada 44 — Estruturas de repetição

Os exemplos trabalham `for`, `range()` e `while`.

**`for`** é utilizado para percorrer sequências ou repetições conhecidas. `range()` produz uma sequência numérica que pode definir início, limite e intervalo.

**`while`** repete um bloco enquanto uma condição continuar verdadeira. O exemplo de senha repete a solicitação enquanto o valor informado for diferente do valor esperado.

A pasta também inclui exemplo de `for` aninhado, demonstrando uma repetição dentro de outra repetição.

### Parada 45 — Coleções

Nesta etapa aparecem listas, tuplas, conjuntos, dicionários e métodos relacionados.

#### Lista

Uma **lista** armazena vários valores e permite acesso por índice. O arquivo `lista.py` percorre listas através de `range()` e também apresenta um dicionário.

#### Dicionário

Um **dicionário** associa chaves a valores. O método `.get()` é utilizado para consultar uma chave e pode receber um valor padrão quando a chave procurada não existe.

#### Tupla

O exemplo `tuplas.py` armazena coordenadas e cores. A sintaxe utiliza parênteses, como `(10, 25)`.

#### Set

O arquivo `set.py` combina uma lista de tarefas com um conjunto de tarefas concluídas. `set()` é útil quando interessa armazenar itens únicos e realizar verificações de pertencimento com expressões como `tarefa in concluidas`.

### Parada 46 — Funções

A calculadora registrada nesta etapa separa as operações em funções como:

```python
def somar_num(n1, n2):
    return n1 + n2
```

Os conceitos principais são:

- **parâmetros**: valores recebidos pela função;
- **`return`**: valor devolvido pela função;
- **decomposição**: divisão do problema em funções menores;
- **validação**: a divisão verifica se o denominador é diferente de zero;
- **`match/case`**: seleciona a operação a ser realizada de acordo com a escolha do usuário.

### Paradas 47 e 48 — Jupyter Notebook e dados

O repositório passa a incluir arquivos `.ipynb`, formato utilizado pelo **Jupyter Notebook**. Notebooks permitem combinar células de código, resultados e documentação em um mesmo documento, o que é especialmente útil para exploração de dados e experimentação.

Há materiais relacionados a SISU e ProUni, além de referências de estudo para dados educacionais.

### Parada 49 — Manipulação de arquivos

`parada49.py` registra exemplos de modos de abertura de arquivo e uso do módulo `os`.

O trecho ativo verifica se um arquivo existe com `os.path.exists()` e, caso exista, utiliza `os.remove()` para removê-lo. Os exemplos comentados também registram os modos:

- `r` — leitura;
- `x` — criação exclusiva;
- `a` — acrescentar conteúdo;
- `w` — escrita.

Isso introduz o conceito de **persistência em arquivos**, no qual dados podem permanecer fora da memória do programa.

## 🧪 Desafios

As pastas `desafio4243`, `desafio4445` e `desafio4647` reúnem exercícios associados às etapas estudadas. Elas preservam diferentes aplicações dos fundamentos apresentados nas aulas.

## 📊 Projeto Python — dados educacionais

A pasta `Projeto Python/` reúne:

- `projeto.ipynb`;
- um arquivo CSV de lista de espera do SISU 2022/2;
- gráficos exportados como imagens (`cidades.png`, `corte.png`, `grau.png`, `sexo.png` e `turno.png`);
- relatório em PDF;
- arquivos de referências e materiais de apoio.

Os arquivos de referência apontam para fontes como **Kaggle**, **dados abertos do MEC**, documentação do **Pandas** e documentação do **Seaborn**. Isso registra o contexto de estudo de análise e visualização de dados utilizado no projeto.

> O CSV preservado possui aproximadamente 89 MB. Ele foi mantido porque faz parte do projeto original, embora o GitHub recomende atenção especial a arquivos desse tamanho.

### Conceitos associados à etapa de dados

**CSV** é um formato textual comum para dados tabulares, em que valores são organizados em linhas e colunas.

**DataFrame**, conceito referenciado na documentação do Pandas presente nos materiais, representa dados em uma estrutura tabular com linhas e colunas e é muito utilizado em análise de dados com Python.

**Visualização de dados** transforma resultados em gráficos para facilitar a identificação de padrões, comparações e distribuições. Os PNGs preservados mostram que o projeto também documentou resultados graficamente.

## 🛠️ Tecnologias e recursos registrados

- Python
- Jupyter Notebook
- arquivos CSV e TXT
- módulo `os`
- referências de Pandas
- referências de Seaborn
- dados educacionais / dados abertos

## 📂 Estrutura resumida

```text
modulo-v-python/
├── parada 42/
├── parada 43/
├── parada 44/
├── parada 45/
├── parada 46/
├── parada 47/
├── parada 48/
├── parada 49/
├── desafio4243/
├── desafio4445/
├── desafio4647/
├── teste python/
└── Projeto Python/
```

## ▶️ Como executar

Arquivos `.py` podem ser executados com uma instalação compatível do Python. Notebooks `.ipynb` podem ser abertos em ambientes compatíveis com Jupyter Notebook. Dependências específicas de cada notebook devem ser verificadas no próprio material antes da execução.

## 💡 Aprendizados

Este módulo registra uma progressão clara: primeiro dominar os blocos fundamentais da linguagem, depois organizar dados em coleções e funções e, por fim, aplicar Python em arquivos e notebooks. A estrutura preservada permite visualizar essa evolução sem transformar exercícios antigos em algo diferente do que eram originalmente.

## 🔗 Navegação

- [Voltar ao repositório principal](../../README.md)
