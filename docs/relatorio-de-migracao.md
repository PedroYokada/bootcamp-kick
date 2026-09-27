# ✅ Relatório de migração — Bootcamp Kick

A consolidação dos repositórios do Bootcamp Kick foi concluída com sucesso em **27/09/2026**.

## Resumo

- Repositórios importados: **19**
- Arquivos versionados importados: **355**
- Estrutura principal criada: fundamentos web, JavaScript/front-end, projeto Xbox, WordPress e Python
- Estratégia utilizada: **`git subtree` sem `--squash`**, preservando o histórico Git dos repositórios de origem dentro da consolidação
- Repositórios originais: **não foram excluídos nem alterados**

## Validação por projeto

| Destino | Arquivos versionados |
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

## Arquivo grande identificado

O arquivo:

```text
python/modulo-v-python/Projeto Python/lista_de_espera_sisu_2022_2.csv
```

possui aproximadamente **88,99 MB**. O GitHub aceitou o arquivo normalmente, mas emitiu um aviso por ele ultrapassar o tamanho recomendado de 50 MB. Ele permanece abaixo do limite máximo convencional de 100 MB por arquivo.

Caso este projeto continue recebendo arquivos grandes no futuro, vale considerar **Git LFS**.

## Preservação de histórico

A migração utilizou `git subtree` sem compactar os históricos. Isso significa que os commits dos repositórios de origem continuam acessíveis no histórico do repositório consolidado por meio dos commits de merge criados durante cada importação.

## Próximo passo opcional

Depois de conferir visualmente todos os projetos no novo repositório, os repositórios antigos podem ser **arquivados** no GitHub para deixar o perfil mais organizado sem apagar o histórico original.

A exclusão dos repositórios antigos não é necessária para obter a organização desejada e deve ser feita somente se houver certeza de que não serão mais necessários individualmente.
