# Mapa da Literatura — Provado, Controverso, Inexplorado e Lacuna Final

**Projeto de pesquisa:** Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial
**Versão:** v0.1 · **Data:** 2026-09-05 · **Base:** matriz de 25 artigos (`matriz-de-artigos.md`), análise quantitativa (`analise-quantitativa.md`) e revisão (v0.3)

> Este documento converte a matriz em conhecimento: o que a literatura **já provou**, o que é **controverso**, o que está **inexplorado** e **qual é a lacuna final** que nosso experimento preencherá. Cada afirmação é ancorada em IDs da matriz (fichas completas com DOI em `matriz-de-artigos.md`).

---

## 1. O que a literatura já provou

### 1.1 Aplicabilidade (A)

- **P1.** LLMs são aplicáveis a praticamente **todo o ciclo de Engenharia de Software** — requisitos, design, desenvolvimento, QA, manutenção, gerenciamento — mapeados em **85 tarefas** de SE a partir de 395 artigos (A01).
- **P2.** A geração de código por LLMs apresenta limitações recorrentes e ainda não resolvidas: **alucinações, vulnerabilidades, baixa generalização e problemas de interpretabilidade** (A02).

### 1.2 Defeitos (B)

- **P3.** Código gerado por LLM contém defeitos com **padrões característicos e classificáveis**: taxonomia de **10 padrões** (ex.: misinterpretation, missing corner case, hallucinated object, incomplete generation), validada com **34 pesquisadores/profissionais** (B01).
- **P4.** IA e humanos têm **perfis de defeitos diferentes** — não apenas "mais ou menos bugs" (ODC, >500 mil amostras): IA apresenta mais constructs não utilizados, debugging hardcoded e vulnerabilidades de alto risco (B03).
- **P5.** Benchmarks acadêmicos e situações reais **não produzem os mesmos tipos de bug** para o mesmo código gerado (B02).
- **P6.** Resultados de LLMs são **não-deterministas**: mesmo prompt → saídas diferentes, afetando correção e reprodutibilidade científica (B04).

### 1.3 Testes (C)

- **P7.** Geração de casos de teste, código de teste e reparo de programas são as aplicações-chave de LLMs em testes (C01).
- **P8.** Testes gerados por IA têm **efetividade limitada para detectar bugs** (detecção de defeitos baixa em Defects4J, C04) e podem conter **test smells mesmo quando válidos** (C03).
- **P9.** **Coverage e mutation score deixam de ser indicadores confiáveis** quando o código sob teste contém bugs (C05).
- **P10.** Testes de LLMs **omitem sistematicamente casos especiais** (None, inf, NaN) mesmo com branch coverage alto (96,3%) (C06).

### 1.4 Qualidade (D)

- **P11.** Software gerado por IA **exige supervisão de especialistas** para atingir qualidade executável (D01).
- **P12.** A literatura **privilegia a correção funcional** e subestima características não funcionais (segurança, manutenção, performance) (D04, ISO/IEC 25010).
- **P13.** Código de IA **acumula dívida técnica**: 89,1% dos problemas detectados em 304.362 commits eram code smells; ~24% persistem na revisão mais recente (D05).

### 1.5 Segurança (E)

- **P14.** Vulnerabilidades de segurança ocorrem com **frequência significativa** em código de IA: 29,5% (Python) e 24,2% (JS) em 733 snippets reais; 43 categorias CWE (E01).
- **P15.** **Todos os LLMs avaliados** produzem código com vulnerabilidades, muitas de severidade alta/crítica (995 vulns; 65% high, 33% critical) (E02).

### 1.6 Agentes de programação (F)

- **P16.** Agentes de IA (Codex, Claude Code, Cursor) executam tarefas reais de desenvolvimento, mas com comportamento **diferente do humano**: mudanças locais/de consistência vs. mudanças de design amplas (F01).
- **P17.** Projetos gerados por agentes têm **reprodutibilidade/executabilidade limitada**: apenas 68,3% executam imediatamente em ambiente limpo (44% em Java); expansão média de 13,5× nas dependências (F02).
- **P18.** **Agentes não são equivalentes em confiabilidade**: em 33.580 PRs, 2,66% tiveram commit de reversão, variando de Codex 0,7% a Copilot 7,6% (F05).

---

## 2. O que é controvertido / não concluído

| # | Controvérsia | Evidências opostas | Consequência para a pesquisa |
|---|---|---|---|
| C1 | IA gera código **pior** que humanos? | Favorável à IA: Copilot em experimento com 202 devs (D03); SonarQube com menos bugs e menor esforço de correção em alguns cenários (D02). Desfavorável: perfis de defeitos diferentes com mais riscos (B03); vulnerabilidades frequentes (E01, E02); dívida técnica (D05). | Não há conclusão fechada → a pesquisa não parte de "IA é ruim"; os dados devem decidir (neutralidade experimental). |
| C2 | Prompting orientado a segurança reduz vulnerabilidades? | E03 mostrou que o prompt **muda a distribuição** (χ²) mas **não reduz significativamente** a frequência/densidade geral. | Aborda-se o resultado como variável, sem promessa de mitigação. |
| C3 | Dificuldade/contexto da tarefa muda a qualidade gerada? | D02: IA às vezes melhor, mas problemas estruturais em tarefas complexas. D01: supervisão especializada necessária. | Requisitos devem cobrir complexidade variada; reportar por tarefa, não só agregado. |
| C4 | Coverage/mutation são evidência de qualidade de testes? | C05 contesta; C06 mostra cobertura alta com omissão de corner cases; C04 mostra detecção de bugs baixa. | Oráculo deve **combinar** métricas e medir detecção real de defeitos, não só cobertura. |
| C5 | Testes da própria IA detectam os defeitos que ela introduz? | C03/C04 sugerem que não (test smells, baixa detecção); não há estudo em sistemas completos. | Ponto central de investigação (RQ6, H3). |
| C6 | Modelo = agente? | F01/F02 mostram que agentes (com loop de ferramentas/arquivos) diferem de respostas de modelo único. | Desenho deve separar a categoria "agente" (G4). |

---

## 3. O que está inexplorado — lacunas G1–G5

Base quantitativa em `analise-quantitativa.md` (N=25):

- **G1 — Sistemas completos.** Só **8%** (2/25) geram um sistema/projeto completo sob especificação; **48%** usam snippets/funções e **16%** dados retrospectivos. O estudo de sistema completo existente (F02) foca apenas em reprodutibilidade/executabilidade.
- **G2 — QA/oráculo independente.** Apenas **12%** (3/25) avaliam com critérios/suítes **não produzidos pelo próprio gerador** (C02, D01, D03); só 1 com sistema completo (D03). Grande parte da literatura valida o código com os próprios testes da IA.
- **G3 — Código + testes + defeitos na mesma cadeia.** **0%** combina sistema completo + caracterização de defeitos. Estudos de defeitos não avaliam sistemas; estudos de testes não avaliam os defeitos dos sistemas que deveriam cobrir (C03, C04, C06).
- **G4 — Comparação controlada entre agentes.** 20% investigam agentes, mas apenas **1 (4%)** com sistema completo (F02) e **0%** com o desenho integral (mesmo requisito/prompt + múltiplas execuções + oráculo independente + defeitos + segurança). Os estudos retrospectivos (D05, F04, F05) observam dados reais, mas não são experimentos controlados.
- **G5 — Métricas de teste contestadas.** Apenas 2–3 estudos (C05, C06) problematizam coverage/mutation como evidência; nenhum combina **métricas múltiplas + detecção real de defeitos** em sistemas completos.

**Cruzamentos críticos da análise quantitativa:**

| Cruzamento | % |
|---|---|
| Sistema completo **+** oráculo independente | 4% (1/25 = D03) |
| Sistema completo **+** defeitos | 0% |
| Sistema completo **+** segurança | 0% |
| Agente **+** sistema completo | 4% (1/25 = F02) |
| **Desenho integral** (agente + sistema completo + oráculo indep. + múltiplas execuções + segurança + defeitos) | **0%** |

---

## 4. Lacuna final

A literatura provou os **fragmentos** de forma isolada:

1. LLMs geram código com **defeitos de perfil próprio** (B01, B03) e **vulnerabilidades frequentes** (E01, E02).
2. Testes de IA **não são oráculo confiável** (C03, C04) e **coverage/mutation enganam** na presença de bugs (C05, C06).
3. Qualidade **não é só funcional** — segurança, manutenção e dívida técnica importam (D04, D05).
4. Agentes executam tarefas reais com **confiabilidade desigual** (F01, F02, F05) e **não-determinismo** (B04).

Mas **nenhum estudo** une esses fragmentos em um **experimento controlado e reprodutível** com:

> **a mesma especificação** → **diferentes agentes de IA** → **sistemas completos** → **≥3 execuções** → **oráculo/Q independente** → **defeitos + segurança + manutenibilidade + reprodutibilidade** → **análise estatística**.

**Enunciado da lacuna (redação candidata):**

> Embora a literatura demonstre que código gerado por IA apresenta defeitos característicos, vulnerabilidades frequentes e testes com baixa capacidade de detecção, não há evidência empírica controlada sobre como **diferentes agentes de IA se comparam quando produzem sistemas completos a partir dos mesmos requisitos**, avaliados por um **oráculo independente**, sob **múltiplas execuções**, cobrindo simultaneamente **qualidade funcional, defeitos, segurança, manutenibilidade e reprodutibilidade**.

---

## 5. Como o experimento fecha a lacuna (mapeamento L → RQ/H)

| Componente da lacuna | Fecha com | Origem na literatura |
|---|---|---|
| Sistemas completos (G1) | Requisito único (ex.: API de tarefas) entregue a cada agente | G1; D03 (único sistema completo controlado) |
| Mesma especificação (G4) | Prompt/especificação idêntica para todos os agentes, sem ajuste por agente | G4; P5/B02 |
| Múltiplas execuções (G4) | ≥3 execuções independentes por agente | P6/B04; 4% da literatura trata variabilidade |
| Oráculo independente (G2) | Suíte de testes funcional/negativo/segurança escrita à parte, desconhecida pelo gerador | G2; P8/C04 |
| Defeitos como objeto (G3) | Classificação com taxonomia Tambon (10 padrões) + severidade | P3/B01 |
| Segurança (G1×E) | OWASP/CWE nas entradas, saídas e dependências | P14/P15 |
| Manutenibilidade (G1×D) | Code smells/dívida técnica (referência ISO/IEC 25010) | P12/P13; D04 |
| Repro-dutibilidade (executabilidade) | Executabilidade em ambiente limpo; variância entre execuções | P17/F02 |
| Testabilidade (G3×C) | Testes da própria IA contra oráculo; detecção real de defeitos | P8–P10; RQ6 |
| Neutralidade (C1) | Permitir IA melhor/igual/pior conforme o resultado | D02, D03 |

### RQs e hipóteses que a lacuna sustenta

| RQ | Pergunta | Lacuna/evidência que sustenta |
|---|---|---|
| RQ1 | Diferenças de qualidade funcional entre agentes? | G1/G4; D03, D02 |
| RQ2 | Diferenças de densidade de defeitos? | G3; B03, B01 → H1 |
| RQ3 | Categorias de defeitos predominantes por agente? | G3; B01, B03 → H2 |
| RQ4 | Diferenças de severidade? | G3; E02 |
| RQ5 | Segurança e manutenibilidade? | G1; D04, D05, E01–E03 → H4 |
| RQ6 | Testes do próprio agente detectam seus defeitos? | G2/G5; C03–C06 → H3 |
| RQ7 | Reprodutibilidade dos sistemas? | G1; F02, B04 |
| RQ8 | Variabilidade entre execuções? | G4; B04 |

| Hipótese | Afirmação | Base |
|---|---|---|
| H1 | Diferenças significativas na densidade de defeitos entre agentes | B03 (perfis diferentes), B01 |
| H2 | Distribuições diferentes de categorias de defeitos (perfil) | B01, B03 |
| H3 | Testes da própria IA não garantem detecção dos seus defeitos | C03, C04, C05 |
| H4 | Qualidade funcional não representa a qualidade global | D04, D05, E01–E03 |

---

## 6. O que NÃO é o nosso estudo (para evitar promessas excessivas)

- Não é uma SLR formal (matriz de conveniência de 25 estudos; extensível para 30+ em SLR futura).
- Não mede "superioridade" absoluta de uma IA — compara **perfis e densidades** sob condições idênticas.
- Não inclui self-correction/revisão pela própria IA na primeira versão (B02 é variável futura).
- Não é estudo retrospectivo de commits/PRs reais (esses existem: D05, F04, F05); é **experimento controlado prospectivo**.

---

## 7. Status e próximos passos

- ✅ Matriz 25/25 com DOIs/metadados consolidados.
- ✅ Análise quantitativa v1 (frequências e cruzamentos).
- ✅ Mapa da literatura + lacuna final (este documento).
- ⏳ Consolidar problema/RQs/hipóteses com base neste mapa (transformar `problema-e-hipoteses.md` de rascunho em consolidado).
- ⏳ Definir metodologia experimental e construir o oráculo independente.

---

*Documento de trabalho. Revisar ao consolidar RQs/H no arquivo `problema-e-hipoteses.md`.*