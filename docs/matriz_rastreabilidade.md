# Matriz de Rastreabilidade — BiblioTech

Relaciona cada requisito aos casos de teste que o verificam.

| Requisito | Descrição | CT-01 | CT-02 | CT-03 | CT-04 | CT-05 | CT-06 | CT-07 | CT-08 | CT-09 | CT-10 | CT-11 | CT-12 | CT-13 | CT-14 | CT-15 | CT-16 | CT-17 |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| RF01 — Permissão para empréstimo | X | X | X | X | X | | | | | | | | | | | | | |
| RF02 — Multa por atraso | | | | | | X | X | X | X | X | X | | | | | | |
| RF03 — Classificação de atraso | | | | | | | | | | | | X | X | X | X | X | X |

## Perguntas de verificação

**Existe requisito sem teste?**
Não. RF01, RF02 e RF03 possuem ao menos um caso de teste associado.

**Existe teste que não sabemos qual requisito verifica?**
Não. Todos os CTs (CT-01 a CT-17) estão vinculados a exatamente um requisito.

**Observação**
CT-05 (`pode_emprestar(True, False, 3)`) é o caso crítico: segundo RF01, um usuário com
3 empréstimos ativos **não** deveria conseguir emprestar. Se este teste falhar na
execução, é evidência de defeito e deve ser registrado no Pull Request.
