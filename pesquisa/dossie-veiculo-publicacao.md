# Dossiê Comparativo — Veículo de Publicação (decisão com orientadores)

> **Finalidade:** subsidiar a decisão de **onde submeter** o artigo do experimento controlado. Elaborado em 2026-09-06 com dados de busca web (atualizados na data). **Decisão final é dos orientadores.**
> **Nota de data:** hoje é 06/09/2026. Alguns prazos de 2026 já passaram; o comparativo prioriza janelas viáveis (2027).
> **Nota de honestidade:** nada aqui resolve a decisão do *formato* — o dossiê apenas organiza as alternativas reais e seus prós/contras para a reunião com o orientador.

---

## 1. Critérios que devem pesar na escolha

| Critério | Peso sugerido | Observação p/ nosso caso |
|---|---|---|
| Adequação ao conteúdo (estudo empírico controlado de QA de software) | Alto | Nosso artigo é **empírico** (experimento controlado), o que favorece EMSE/ICSE/MSR |
| Evidência e poder estatístico (n=12, células <5) | Alto | Revisores de Q1 A* podem exigir amostra maior; SBES/QA são menos rigorosos nisso |
| Qualis/estratificação para o curso/PPG | Médio | Depende do PPG (Ciência da Computação vs Sistemas/Educação) |
| Prazo de submissão vs. tempo do artigo | Alto | Janelas de 2027 são as realistas para artigo completo |
| Custo/inscrição e apresentação exigida | Baixo–médio | Conferências exigem presença; periódicos não |
| Open access / Ciência aberta | Médio | Todos valorizam artefato/replicabilidade (nosso ponto forte) |

---

## 2. Opções de veículo (ordenadas por encaixe + viabilidade)

### A) Periódicos (recomendado como principal caminho)

| Veículo | Tipo | JIF (2025) | Qualis (SE) | Encaixe | Prazo tip. | Veredito |
|---|---|---|---|---|---|---|
| **Empirical Software Engineering (EMSE)** – Springer | Periódico | ~3,4–3,6 (Q1) | A1/A2 em ES | **Excelente** — escopo explícito "empirical software engineering"; incentiva replicação; aceita estudos com limitações honestas; registra `registered reports` | Rolling / ~2-4 m. | **Principal recomendação**: escopo e cultura ideais p/ experimento controlado + sólida seção de limitações |
| **IEEE TSE** | Periódico | ~6,0 (Q1) | A1 | Bom, porém muito seletivo; pode exigir poder estatístico maior | Rolling | Desafiador com n=12; usar se extender amostra (χ²/células ≥5) |
| **JSS (J. of Systems and Software)** | Periódico | ~3,5 (Q1) | A1/A2 | Bom — publica estudos empíricos de qualidade e agentes | Rolling | Alternativa sólida e mais acessível que TSE |
| **Software Quality Journal (SQJ)** | Periódico | ~2,5 | B1 | Bom — foco em qualidade/testes | Rolling | Boa opção de menor exigência estatística |
| **IST (Information and Software Technology)** | Periódico | ~3,9 (Q1) | A1/A2 | Bom — escopo amplo de ES empírica | Rolling | Alternativa equilibrada |

> **Periódicos em geral:** não exigem presença, aceitam revisão iterativa (major/minor revision), e são culturalmente mais tolerantes a estudos com limitações explícitas desde que o método seja sólido e a discussão honesta — compatível com o perfil do nosso artigo. **Principal via recomendada: EMSE.**

### B) Conferências internacionais

| Veículo | Nível | Encaixe | Prazo (próxima janela) | Veredito |
|---|---|---|---|---|
| **ICSE (Intl. Conf. Software Engineering)** | A* (CORE) | Bom — estuda agentes e qualidade | ICSE 2027: abstract 23-jun-2026, submission 30-jun-2026 (**já passou**); considerar ICSE 2028 | Muito seletivo; com n=12 e células <5, risco alto de rejeição. Manter para versão ampliada. |
| **MSR (Mining Software Repositories)** | A | Bom — inclui agentes/PRs (F02/F05 são MSR) | MSR 2027 (janela ~set-out/2026 p/ paper track) | Encaixe forte (agentes), porém MSR valoriza *mundança em larga escala*; nosso n=12 é pequeno. Usar se ampliar com mineração real. |
| **ASE (Automated Software Engineering)** | A | Médio — foco em automação/testes | ASE 2027 | Encaixe médio; melhor se ênfase = testabilidade (RQ6/H3) |

### C) Conferência nacional (muito relevante para o contexto brasileiro)

| Veículo | Qualis | Encaixe | Prazo | Veredito |
|---|---|---|---|---|
| **SBES (Trilha de Pesquisa)** + CBSoft | B2 (Qualis SE) | **Muito bom** — principal evento de ES no Brasil/LA; publica estudos empíricos de testes e qualidade; aceita papers curtos (4-10 pág.) | SBES 2027 (prazo tipicamente ~abril/2027, próximo ciclo) | **Recomendação nacional** — custo acessível, comunidade brasileira, e aceita estudos com amostra pequena; excelente para primeira publicação do experimento |

> **Observação prática:** SBES valoriza **Ciência Aberta e reprodutibilidade** — exatamente nosso ponto forte (oráculo + matriz + manifests). Verificar a data-limite do próximo SBES na chamada oficial (ciclo 2027).

---

## 3. Estratégia recomendada (para levar ao orientador)

1. **Publicar primeiro no SBES 2027** (nacional, aceita n=12, divulga o experimento já maduro) → carimbo de versão peer-reviewed e feedback da comunidade QA/ES brasileira.
2. **Depois, ampliar a amostra** (mais execuções e/ou execução em Docker na máquina de produção) para elevar células esperadas ≥5 → submeter versão **estendida/replicada** a **EMSE** (escopo ideal) com o incremento de robustez estatística.
3. **TSE/ICSE** ficam como meta de longo prazo, **apenas após** a extensão da amostra e reforço estatístico, por causa da alta exigência.

> **Pré-requisito transversal:** formalizar o **pré-registro** (hipóteses H1–H4, RQs, plano de análise, datas, neutralidade C1) antes de submeter — reforça aderência a Ciência Aberta e à cultura dos veículos-alvo.

---

## 4. O que decidir com o orientador (itens concretos da reunião)

| # | Decisão | Opções | Quem decide |
|---|---|---|---|
| 1 | **Veículo principal** | SBES 2027 / EMSE / JSS / SQJ / IST | Orientador + autor |
| 2 | **Ampliar amostra antes de submeter?** | Sim (n=24/36) / Não (n=12) | Orientador (implica custo/tempo de execução Docker em produção) |
| 3 | **Idioma** | Português (SBES aceita pt/en) / Inglês (periódicos internacionais) | Orientador |
| 4 | **Formato do paper** | Longo (EMSE ~20p) / Curto (SBES 10p) | Veículo |
| 5 | **Pré-registro formal** | Criar já no repo privado (recomendado) | Autor (posso criar) |

---

## 5. Links e fontes (verificados 2026-09-06)

- EMSE aims/scope e métricas JIF: link.springer.com/journal/10664 · emsejournal.github.io/metrics.html
- IEEE TSE métricas: ieeexplore.ieee.org; JCR Q1
- SBES 2026 call (Trilha de Pesquisa, prazo 4-mai-2026) e política de Ciência Aberta: cbsoft.sbc.org.br/2026 · SBES partner journals list (TOSEM, ASE, EMSE, IEEE SW, TSE, IST, JSERD, JSEP, JSS, SQJ)
- ICSE 2027 (Ciência Aberta, SCRE, prazos; CORE A*): conf.researchr.org/track/icse-2027
- MSR 2026 (pp. 847-851; DOI 10.1145/3793302.3793587): dl.acm.org
- Qualis SBES B2 (fonte verlab/UEMG, pode estar desatualizada — confirmar na plataforma Sucupira atual): verlab.dcc.ufmg.br

> **Ação imediata sugerida:** confirmar na **Plataforma Sucupira (versão atualizada do Qualis)** a classificação vigente de SBES, EMSE, JSS, SQJ, IST no *quadriênio* do seu PPG, pois o Qualis muda por edição e por área. Isso precisa ser feito com o orientador (acesso institucional).

---

*Dossiê v0.1 — 2026-09-06. Elaborado para orientar a reunião; não substitui a decisão dos orientadores nem a consulta à Plataforma Sucupira.*