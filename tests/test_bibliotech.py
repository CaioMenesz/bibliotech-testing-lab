"""
Testes de caixa preta — BiblioTech
Elaborados a partir de requisitos.md (RF01, RF02, RF03), sem análise do código-fonte.
"""

from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso


# ---------------------------------------------------------------------------
# RF01 — Permissão para empréstimo
# ---------------------------------------------------------------------------

def test_ct01_usuario_ativo_sem_pendencia_sem_emprestimos_pode_emprestar():
    # CT-01 | cenário válido
    assert pode_emprestar(True, False, 0) is True


def test_ct02_usuario_inativo_nao_pode_emprestar():
    # CT-02 | cenário inválido — usuário inativo
    assert pode_emprestar(False, False, 0) is False


def test_ct03_usuario_com_pendencia_nao_pode_emprestar():
    # CT-03 | cenário inválido — pendência
    assert pode_emprestar(True, True, 0) is False


def test_ct04_usuario_com_dois_emprestimos_pode_emprestar():
    # CT-04 | limite inferior — abaixo do limite (deve poder)
    assert pode_emprestar(True, False, 2) is True


def test_ct05_usuario_com_tres_emprestimos_nao_pode_emprestar():
    # CT-05 | limite de fronteira — requisito diz "menos de 3 empréstimos ativos"
    # Este teste tende a REVELAR O DEFEITO da implementação atual.
    assert pode_emprestar(True, False, 3) is False


# ---------------------------------------------------------------------------
# RF02 — Multa por atraso
# ---------------------------------------------------------------------------

def test_ct06_sem_atraso_multa_zero():
    # CT-06 | cenário válido — sem atraso
    assert calcular_multa(0) == 0.0


def test_ct07_atraso_negativo_multa_zero():
    # CT-07 | valor fora do domínio esperado (defensivo)
    assert calcular_multa(-1) == 0.0


def test_ct08_atraso_dentro_da_primeira_faixa():
    # CT-08 | cenário válido — 3 dias de atraso
    assert calcular_multa(3) == 6.0


def test_ct09_atraso_fronteira_sete_dias():
    # CT-09 | limite superior da primeira faixa
    assert calcular_multa(7) == 14.0


def test_ct10_atraso_fronteira_oito_dias():
    # CT-10 | limite inferior da segunda faixa
    assert calcular_multa(8) == 17.0


def test_ct11_atraso_dez_dias():
    # CT-11 | cenário válido — segunda faixa
    assert calcular_multa(10) == 23.0


# ---------------------------------------------------------------------------
# RF03 — Classificação de atraso
# ---------------------------------------------------------------------------

def test_ct12_sem_atraso():
    # CT-12 | cenário válido
    assert classificar_atraso(0) == "sem atraso"


def test_ct13_atraso_leve_fronteira_inferior():
    # CT-13 | limite inferior — atraso leve
    assert classificar_atraso(1) == "atraso leve"


def test_ct14_atraso_leve_fronteira_superior():
    # CT-14 | limite superior — atraso leve
    assert classificar_atraso(7) == "atraso leve"


def test_ct15_atraso_moderado_fronteira_inferior():
    # CT-15 | limite inferior — atraso moderado
    assert classificar_atraso(8) == "atraso moderado"


def test_ct16_atraso_moderado_fronteira_superior():
    # CT-16 | limite superior — atraso moderado
    assert classificar_atraso(30) == "atraso moderado"


def test_ct17_atraso_grave():
    # CT-17 | cenário válido — atraso grave
    assert classificar_atraso(31) == "atraso grave"
