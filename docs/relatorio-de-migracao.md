# ✅ Relatório de migração — Bootcamp Kick

A consolidação dos repositórios do Bootcamp Kick foi concluída com sucesso em **27/09/2026** e, na sequência, a estrutura organizacional foi padronizada em **kebab-case**.

## Resumo

- Repositórios importados: **19**
- Arquivos versionados importados: **355**
- Estrutura principal: fundamentos web, JavaScript/front-end, projeto Xbox, WordPress, Python e documentação
- Estratégia de migração: **`git subtree` sem `--squash`**
- Padronização posterior: nomes das pastas organizacionais convertidos para kebab-case
- Repositórios originais: **não foram excluídos nem alterados**

## Validação por projeto

| Destino atual | Arquivos versionados na importação |
|---|---:|
| `fundamentos-web/desafios-iniciais` | 4 |
| `fundamentos-web/desafio-05-kick` | 9 |
| `fundamentos-web/desafio-07-08-kick` | 2 |
| `fundamentos-web/desafio-09-10-figma` | 49 |
| `fundamentos-web/desafio-11-kick` | 13 |
| `fundamentos-web/desafio-13-kick` | 23 |
| `fundamentos-web/desafio-17-kick` | 9 |
| `javascript-front-end/desafio-19-kick` | 3 |
| `javascript-front-end/desafio-22-kick` | 2 |
| `javascript-front-end/desafio-23-kick` | 2 |
| `javascript-front-end/desafio-25-kick` | 3 |
| `javascript-front-end/desafio-27-kick` | 10 |
| `javascript-front-end/desafio-29-kick` | 7 |
| `javascript-front-end/desafio-31-kick` | 6 |
| `javascript-front-end/parada-34-kick` | 2 |
| `projeto-xbox/projeto-xbox-figma` | 46 |
| `projeto-xbox/projeto-xbox-web` | 87 |
| `wordpress/modulo-iv-wordpress` | 9 |
| `python/modulo-v-python` | 69 |
| **Total** | **355** |

## Padronização de nomes

As pastas de agrupamento e as pastas que representam cada projeto passaram a seguir kebab-case. Exemplos:

```text
01-fundamentos-web/Desafio-05-Kick
        ↓
fundamentos-web/desafio-05-kick
```

```text
03-projeto-xbox/desafiowebkick
        ↓
projeto-xbox/projeto-xbox-web
```

As estruturas internas dos projetos foram preservadas quando uma mudança poderia quebrar caminhos relativos ou alterar o funcionamento original.

## Arquivo grande identificado

O arquivo:

```text
python/modulo-v-python/Projeto Python/lista_de_espera_sisu_2022_2.csv
```

possui aproximadamente **88,99 MB**. O GitHub aceitou o arquivo, mas emitiu aviso por ele ultrapassar o tamanho recomendado de 50 MB. Ele permanece abaixo do limite máximo convencional de 100 MB por arquivo.

Caso o projeto passe a receber novos arquivos grandes, vale considerar Git LFS.

## Preservação de histórico

A migração utilizou `git subtree` sem compactar os históricos. Os commits dos repositórios de origem permanecem incorporados ao histórico do repositório consolidado por meio dos commits de merge criados durante cada importação.

A reorganização posterior foi feita com movimentação de arquivos dentro do próprio repositório, sem apagar os projetos.

## Documentação adicionada

- `docs/mapa-de-origens.md`
- `docs/estrutura-do-repositorio.md`
- `docs/github-about.md`
- `docs/revisao-manual.md`
- `.gitignore`

## Repositórios antigos

Depois da conferência visual dos projetos consolidados, os repositórios antigos podem ser **arquivados** para deixar o perfil mais organizado sem apagar o histórico individual.

A exclusão não é necessária para obter essa organização.
