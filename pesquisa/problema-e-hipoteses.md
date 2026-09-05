# Problema, Perguntas de Pesquisa e Hipóteses — Consolidado

> **Status: CONSOLIDADO (v0.2)** — validado em 2026-09-05 com base no **mapa da literatura** (`mapa-da-literatura.md`) e na **análise quantitativa** da matriz (`analise-quantitativa.md`). As RQs e hipóteses abaixo estão ancoradas nas lacunas G1–G5; revisões futuras são possíveis, mas exigem justificativa contra as evidências P1–P18.

---

## 1. Problema (fundamentado na lacuna final)

A literatura provou os fragmentos de forma isolada:

- LLMs geram código com **defeitos de perfil próprio** (P3, P4) e **vulnerabilidades frequentes** (P14, P15).
- Testes de IA **não são oráculo confiável** (P8) e **coverage/mutation enganam** na presença de bugs (P9, P10).
- Qualidade **não é só funcional** — segurança, manutenção e dívida técnica importam (P12, P13).
- Agentes executam tarefas reais com **confiabilidade desigual** e **não-determinismo** (P6, P16, P18).

**Porém (lacuna final, G1–G5):** nenhum estudo revisado (0/25) une esses fragmentos em um experimento controlado e reprodutível com a mesma especificação → diferentes agentes → sistemas completos → ≥3 execuções → oráculo independente → defeitos + segurança + manutenibilidade + reprodutibilidade → análise estatística.

**Problema de pesquisa (redação):**

> Embora a literatura demonstre que código gerado por IA apresenta defeitos característicos, vulnerabilidades frequentes e testes com baixa capacidade de detecção, **não há evidência empírica controlada sobre como diferentes agentes de IA se comparam quando produzem sistemas completos a partir dos mesmos requisitos**, avaliados por um **oráculo independente**, sob **múltiplas execuções**, cobrindo simultaneamente **qualidade funcional, defeitos, segurança, manutenibilidade e reprodutibilidade**.

---

## 2. Objetivo geral

Avaliar empiricamente a qualidade e os defeitos presentes em sistemas de software produzidos por diferentes agentes/modelos de IA sob condições experimentais controladas (mesmo requisito, mesmo prompt, múltiplas execuções, oráculo independente).

## 3. Objetivos específicos

| # | Objetivo | Fecha lacuna |
|---|---|---|
| 1 | Comparar diferentes IAs/agentes na produção de software a partir do mesmo requisito | G4 |
| 2 | Identificar defeitos nos artefatos gerados | G3 |
| 3 | Classificar os defeitos (taxonomia Tambon [B01], + severidade) | G3 |
| 4 | Avaliar a severidade dos defeitos | G3 |
| 5 | Medir cobertura e efetividade de testes (sem confiar isoladamente em coverage/mutation) | G5 |
| 6 | Avaliar qualidade estrutural (ISO/IEC 25010 como referência [D04]) | G1 |
| 7 | Avaliar segurança (CWE/OWASP [E01]–[E03]) | G1×E |
| 8 | Investigar a capacidade da própria IA de detectar seus defeitos | G2/G5 |
| 9 | Comparar os resultados estatisticamente entre agentes | G4 |

---

## 4. Pergunta principal

> Como diferentes agentes de Inteligência Artificial generativa influenciam a qualidade, a densidade e a natureza dos defeitos, a testabilidade e a reprodutibilidade de sistemas de software desenvolvidos sob requisitos controlados?

---

## 5. Perguntas de pesquisa (RQ1–RQ8) — consolidadas

| RQ | Pergunta | Lacuna/evidência que sustenta | Decisão que informa |
|---|---|---|---|
| RQ1 | Existem diferenças na qualidade funcional entre sistemas produzidos por diferentes agentes? | G1/G4; P1, P11, D02/D03 | Comparações entre agentes |
| RQ2 | Existem diferenças na densidade de defeitos? | G3; P4 (H1) | Teste estatístico de H1 |
| RQ3 | Quais categorias de defeitos são predominantes em cada agente? | G3; P3, P4 (H2) | Perfis de defeitos |
| RQ4 | Existem diferenças na severidade dos defeitos? | G3; P15 | Distribuição por severidade |
| RQ5 | Existem diferenças de segurança e manutenibilidade? | G1; P12–P15 (H4) | ISO/IEC 25010 + CWE |
| RQ6 | Os testes gerados pelo próprio agente conseguem detectar seus defeitos? | G2/G5; P8–P10 (H3) | Definição do oráculo |
| RQ7 | Quão reprodutíveis são os sistemas gerados? | G1; P6, P17 | Executabilidade |
| RQ8 | Quanto os resultados variam entre execuções do mesmo agente? | G4; P6 (B04) | Variância entre execuções |

---

## 6. Hipóteses — consolidadas

| H | Afirmação | Base na literatura | Falsificável? |
|---|---|---|---|
| H1 | Há diferenças estatisticamente significativas na **densidade de defeitos** entre softwares produzidos por diferentes agentes/modelos a partir dos mesmos requisitos. | P4 (B03: perfis ≠ quantidade), P18 (agentes desiguais) | Sim — comparação de densidades com teste estatístico |
| H2 | Diferentes modelos produzem **distribuições diferentes de categorias de defeitos** (perfil de defeitos). | P3 (B01), P4 (B03) | Sim — distribuições comparadas |
| H3 | A utilização de IA para geração de testes **não garante a detecção** dos defeitos introduzidos pela própria IA. | P8–P10 (C03, C04, C05), G5 | Sim — taxa de detecção dos testes da IA vs oráculo |
| H4 | A qualidade funcional do software **não é suficiente** para representar sua qualidade global (é preciso avaliar vulnerabilidades, performance, manutenibilidade, edge cases, dívida técnica). | P12 (D04), P13 (D05), P14–P15 (E01–E03) | Sim — qualidade total > funcional |

> Nota: H2 deriva-se de B01/B03 para a escala de **sistemas completos**; H3 foca o diferencial da pesquisa (G2/G5); manter H1–H4 sem aumentar o número excessivo de comparações estatísticas (correção por múltiplas comparações).

---

## 7. Princípios metodológicos (reafirmados)

- **Mesmo requisito** para todas as IAs.
- **Mesmo prompt/especificação** (sem melhorar prompt para "corrigir" uma IA).
- **Mesma quantidade de oportunidades**: ≥3 execuções independentes por modelo (não-determinismo, P6/B04); análise de variabilidade (RQ8).
- **Oráculo independente** da IA geradora:
  - testes funcionais (unitários, integração, API, E2E);
  - testes negativos (invalid input, extremos, ausência de dados, permissões, autenticação);
  - segurança (OWASP, vulnerabilidades, dependências);
  - qualidade estrutural (complexidade, duplicação, code smells, manutenibilidade) — ISO/IEC 25010 (P12).
- **Matriz de defeitos**: `ID · IA · Categoria · Severidade · Detectado automaticamente?` (taxonomia Tambon, P3).
- **Análise estatística** sobre os resultados (comparações entre modelos).
- **Neutralidade experimental:** a pesquisa não parte de "IA é ruim"; os dados devem decidir (C1; D02, D03).

## 8. Dimensões do experimento (inalteradas)

- **A — Qualidade:** quanto software funcional a IA consegue produzir?
- **B — Defeitos:** quais defeitos são produzidos (taxonomia + severidade)?
- **C — Testabilidade:** os testes conseguem encontrar esses defeitos? (diferencial da pesquisa)

---

## 9. Decisões em aberto (deixadas para a fase de metodologia)

- Título final (provisório: "Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados").
- Stack do experimento: Python + FastAPI + PostgreSQL **ou** Node.js + TypeScript + PostgreSQL.
- Definição prática do "requisito controlado" (escopo do sistema completo a ser gerado).
- Critérios de seleção dos agentes (cobertura de modelos vs. acessibilidade, orçamento).
- Inclusão (ou não) de variável "revisão pela própria IA" (self-correction [B02]) na primeira versão — **provável exclusão** para manter o estudo controlado.

---

## 10. Fonte das evidências citadas

- Mapa da literatura: provado P1–P18, controvérsias C1–C6, lacunas G1–G5 e lacuna final (`mapa-da-literatura.md`).
- Análise quantitativa: frequências e cruzamentos que sustentam a originalidade do desenho (`analise-quantitativa.md`).
- Fichas completas com DOI dos 25 artigos (`matriz-de-artigos.md`).

---

*Documento consolidado. Próxima etapa: metodologia experimental (requisito controlado, oráculo independente, protocolo de execução).*