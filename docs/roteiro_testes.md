# Roteiro de Testes — BiblioTech

---

## CT-01
**Requisito:** RF01

**Título:** Usuário ativo, sem pendência e sem empréstimos pode realizar empréstimo.

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=0

**Passos:** Executar `pode_emprestar(True, False, 0)`.

**Resultado esperado:** True

**Resultado obtido:** ____________________

**Status:** 
- [ ] Passou
- [x] Falhou

---

## CT-02
**Requisito:** RF01

**Título:** Usuário inativo não pode realizar empréstimo.

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** usuario_ativo=False, possui_pendencia=False, emprestimos_ativos=0

**Passos:** Executar `pode_emprestar(False, False, 0)`.

**Resultado esperado:** False

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-03
**Requisito:** RF01

**Título:** Usuário com pendência não pode realizar empréstimo.

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível e usuário ativo.

**Dados de teste:** usuario_ativo=True, possui_pendencia=True, emprestimos_ativos=0

**Passos:** Executar `pode_emprestar(True, True, 0)`.

**Resultado esperado:** False

**Resultado obtido:** ____________________

**Status:**
- [x] Passou
- [ ] Falhou

---

## CT-04
**Requisito:** RF01

**Título:** Usuário com dois empréstimos ativos ainda pode emprestar (limite inferior).

**Tipo:** Caixa preta

**Prioridade:** Média

**Pré-condição:** Sistema disponível, usuário ativo e sem pendência.

**Dados de teste:** usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=2

**Passos:** Executar `pode_emprestar(True, False, 2)`.

**Resultado esperado:** True

**Resultado obtido:** ____________________

**Status:** 
- [ ] Passou 
- [x] Falhou

---

## CT-05
**Requisito:** RF01

**Título:** Usuário com três empréstimos não pode realizar outro empréstimo (valor de fronteira).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível e usuário ativo.

**Dados de teste:** usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=3

**Passos:** Executar `pode_emprestar(True, False, 3)`.

**Resultado esperado:** False

**Resultado obtido:** ____________________

**Status:** 
- [ ] Passou 
- [x] Falhou

**Observação:** requisito diz "menos de 3 empréstimos ativos" — este é o caso crítico que tende a revelar defeito na implementação.

---

## CT-06
**Requisito:** RF02

**Título:** Sem atraso, multa deve ser zero.

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=0

**Passos:** Executar `calcular_multa(0)`.

**Resultado esperado:** 0.00

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou
---

## CT-07
**Requisito:** RF02

**Título:** Atraso negativo (fora do domínio) não gera multa.

**Tipo:** Caixa preta

**Prioridade:** Baixa

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=-1

**Passos:** Executar `calcular_multa(-1)`.

**Resultado esperado:** 0.00

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-08
**Requisito:** RF02

**Título:** Multa dentro da primeira faixa (1 a 7 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=3

**Passos:** Executar `calcular_multa(3)`.

**Resultado esperado:** 6.00

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou
---

## CT-09
**Requisito:** RF02

**Título:** Multa no limite superior da primeira faixa (7 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=7

**Passos:** Executar `calcular_multa(7)`.

**Resultado esperado:** 14.00

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou
---

## CT-10
**Requisito:** RF02

**Título:** Multa no limite inferior da segunda faixa (8 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=8

**Passos:** Executar `calcular_multa(8)`.

**Resultado esperado:** 17.00

**Resultado obtido:** ____________________

**Status:** 
- [ ] Passou 
- [x] Falhou

---

## CT-11
**Requisito:** RF02

**Título:** Multa dentro da segunda faixa (10 dias).

**Tipo:** Caixa preta

**Prioridade:** Média

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=10

**Passos:** Executar `calcular_multa(10)`.

**Resultado esperado:** 23.00

**Resultado obtido:** ____________________

**Status:** 
- [ ] Passou 
- [x] Falhou

---

## CT-12
**Requisito:** RF03

**Título:** Sem atraso é classificado como "sem atraso".

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=0

**Passos:** Executar `classificar_atraso(0)`.

**Resultado esperado:** "sem atraso"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou
- [ ] Falhou

---

## CT-13
**Requisito:** RF03

**Título:** Atraso leve no limite inferior (1 dia).

**Tipo:** Caixa preta

**Prioridade:** Média

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=1

**Passos:** Executar `classificar_atraso(1)`.

**Resultado esperado:** "atraso leve"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-14
**Requisito:** RF03

**Título:** Atraso leve no limite superior (7 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=7

**Passos:** Executar `classificar_atraso(7)`.

**Resultado esperado:** "atraso leve"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-15
**Requisito:** RF03

**Título:** Atraso moderado no limite inferior (8 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=8

**Passos:** Executar `classificar_atraso(8)`.

**Resultado esperado:** "atraso moderado"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-16
**Requisito:** RF03

**Título:** Atraso moderado no limite superior (30 dias).

**Tipo:** Caixa preta

**Prioridade:** Alta

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=30

**Passos:** Executar `classificar_atraso(30)`.

**Resultado esperado:** "atraso moderado"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## CT-17
**Requisito:** RF03

**Título:** Atraso grave acima de 30 dias.

**Tipo:** Caixa preta

**Prioridade:** Média

**Pré-condição:** Sistema disponível.

**Dados de teste:** dias_atraso=31

**Passos:** Executar `classificar_atraso(31)`.

**Resultado esperado:** "atraso grave"

**Resultado obtido:** ____________________

**Status:** 
- [x] Passou 
- [ ] Falhou

---

## Casos de caixa branca

## CT-18
**Requisito:** RF01

**Título:** Usuário com quatro empréstimos ativos é bloqueado (cobre o branch verdadeiro da condição de limite — linha 11).

**Tipo:** Caixa branca

**Prioridade:** Alta

**Pré-condição:** Sistema disponível, usuário ativo e sem pendência.

**Dados de teste:** usuario_ativo=True, possui_pendencia=False, emprestimos_ativos=4

**Passos:** Executar `pode_emprestar(True, False, 4)`.

**Resultado esperado:** False

**Resultado obtido:** False

**Status:** 
- [x] Passou 
- [ ] Falhou
