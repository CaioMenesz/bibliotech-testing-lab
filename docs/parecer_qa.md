# Parecer Final de QA — BiblioTech

**Equipe:** _[nome da equipe]_
**Data:** _[data]_
**Branch avaliada:** dev
**Pull Request:** _[link do PR]_

## 1. Requisitos testados
- [x] RF01 — Permissão para empréstimo
- [x] RF02 — Multa por atraso
- [x] RF03 — Classificação de atraso

## 2. Resumo da execução

| Etapa | Quantidade de testes | Resultado |
|---|---|---|
| Caixa preta | 17 | ___ passaram / ___ falharam |
| Caixa branca | ___ | ___ passaram / ___ falharam |
| **Total** | ___ | ___ |

**Cobertura obtida (linhas / branches):** _____ %

## 3. Defeitos encontrados

### Defeito 01
- **Requisito relacionado:** RF01
- **Caso de teste:** CT-05
- **Comportamento esperado:** Usuário com 3 empréstimos ativos NÃO deve poder emprestar (requisito exige "menos de 3 empréstimos ativos").
- **Comportamento observado:** _____ (preencher após rodar `pytest`)
- **Severidade:** Alta — afeta diretamente uma regra de negócio central (RF01).
- **Evidência:** anexar saída do `pytest -v` mostrando o teste `test_ct05_usuario_com_tres_emprestimos_nao_pode_emprestar`.

### Defeito 02 (se aplicável)
- **Requisito relacionado:** _____
- **Caso de teste:** _____
- **Comportamento esperado:** _____
- **Comportamento observado:** _____
- **Severidade:** _____

## 4. Cenários positivos e negativos cobertos
- [x] Cenários válidos (positivos) para os três requisitos
- [x] Cenários inválidos (negativos) para os três requisitos
- [x] Valores de fronteira (limites inferior e superior) nas três regras

## 5. Rastreabilidade
Todos os requisitos possuem cobertura de teste — ver `matriz_rastreabilidade.md`.
Nenhum teste ficou sem vínculo com um requisito.

## 6. Avaliação da equipe

**A pipeline de CI (GitHub Actions) ficou:**
[ ] Verde (todos os testes passaram)
[ ] Vermelha (há teste(s) falhando)

**Recomendação da equipe de QA:**
[ ] Recomendamos aprovação do Pull Request
[ ] **Não recomendamos aprovação** do Pull Request nesta versão

**Justificativa:**
_O defeito identificado em CT-05 indica que a regra de negócio RF01 está_
_implementada incorretamente (permite um 4º empréstimo, quando o requisito_
_estabelece um limite de 3). Recomenda-se a correção da condição em_
_`pode_emprestar` antes da liberação para produção._

_(ajustar este texto conforme o resultado real obtido pela equipe)_

## 7. Assinaturas
- QA responsável: _____________________
- Revisor (outra equipe): _____________________
