# Mini Plano de Testes — BiblioTech

## Identificação
- **Projeto:** BiblioTech — Módulo de Empréstimos
- **Data:** _09/09/2026_
- **Branch testada:** dev

## Escopo
Testar as regras de negócio implementadas em `src/bibliotech.py`:
- RF01 — Permissão para empréstimo
- RF02 — Multa por atraso
- RF03 — Classificação de atraso

## Fora do escopo
- Interface gráfica
- Banco de dados / persistência
- Autenticação e segurança
- Desempenho e carga

## Estratégia
- **Caixa preta:** elaboração de casos de teste a partir de `requisitos.md`, sem consulta ao código-fonte, cobrindo cenários válidos, inválidos e valores de fronteira.
- **Caixa branca:** após liberação do código, análise das condições internas (`if`s) de cada função para identificar caminhos e branches ainda não exercitados.
- **Automação:** implementação de todos os casos como testes unitários em `pytest`, com medição de cobertura via `pytest-cov`.

## Ambiente
- Python 3.12
- pytest
- pytest-cov
- GitHub + GitHub Actions (CI)

## Critério de entrada
- Código-fonte disponível na branch `dev`.
- `requisitos.md` definido e acessível à equipe.
- Ambiente Python configurado e dependências instaladas.

## Critérios de saída
- [ ] Todos os requisitos (RF01, RF02, RF03) possuem pelo menos um caso de teste.
- [ ] Testes de caixa preta e caixa branca executados.
- [ ] Cobertura de linhas e branches ≥ 90%.
- [ ] Defeitos encontrados registrados com evidência (esperado vs. obtido).
- [ ] Pull Request criado com todas as evidências.

## Riscos
| Risco | Impacto | Mitigação |
|---|---|---|
| Tempo limitado (90 min) | Cobertura incompleta | Priorizar valores de fronteira e condições críticas |
| Equipe pouco familiarizada com pytest | Atraso na automação | Reutilizar exemplos do roteiro de testes |
| Foco excessivo em aumentar % de cobertura | Testes sem propósito real | Validar cada teste contra um requisito, não contra o número de cobertura |

## Entregáveis
1. Mini Plano de Testes (este documento)
2. Roteiros/casos de teste (caixa preta e caixa branca)
3. Matriz de rastreabilidade (requisito × caso de teste)
4. Testes automatizados em pytest + relatório de cobertura
5. Parecer final da equipe sobre a liberação da versão
