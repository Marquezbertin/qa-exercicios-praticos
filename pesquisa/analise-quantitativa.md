# Análise Quantitativa da Matriz de Literatura

**Data:** 2026-09-05 · **Amostra:** 25 artigos (matriz A–F) · **Status:** preliminar, revisável

> Este documento quantifica os estudos revisados para fundamentar a originalidade do experimento. A codificação é **explícita** (cada artigo é classificado linha a linha), permitindo revisão, auditoria e ajuste. Campos *a confirmar* na matriz não alteram as dimensões aqui classificadas, mas recomenda-se revalidar a codificação quando DOIs forem confirmados.

---

## 1. Objetivo

Responder com números, sobre a amostra de 25 estudos:

- Que **unidades de análise** predominam (snippet, função, sistema completo, dados retrospectivos, testes)?
- Quantos usam **oráculo/avaliação independente** do gerador?
- Quantos avaliam **defeitos**, **segurança**, **reprodutibilidade**, **qualidade não funcional**?
- Quantos tratam a **variabilidade entre execuções** (não-determinismo)?
- Quantos comparam **agentes** (e não apenas modelos)?
- Qual porcentagem combina as características do nosso desenho? (→ eventual 0% sustenta a lacuna)

---

## 2. Dimensões e regras de codificação

| Dimensão | Símbolo | Regra |
|---|---|---|
| Tipo de estudo | `SLR` / `Survey` / `Empírico` / `Retro` / `Misto` | Retro = retrospectivo sobre dados de repositórios/PRs/commits |
| Unidade de análise | — | Revisão · Snippet/função/patch · Testes · Sistema completo · Parcial · Dados retrospectivos |
| Sistema completo? | `S` / `P` (parcial) / `N` | Gera um **sistema/projeto inteiro** sob uma especificação |
| Oráculo independente? | `S` / `N` | Avaliação por suíte/critérios **não produzidos pelo próprio gerador** |
| Defeitos como objeto | `S` / `N` | Bugs/defeitos analisados e caracterizados |
| Segurança avaliada | `S` / `N` | Vulnerabilidades/CWE avaliadas nos artefatos gerados |
| Reprodutibilidade | `S` / `N` | Executabilidade/estabilidade entre execuções, ou não-determinismo |
| Múltiplas execuções | `S` / `N` | O estudo executa o gerador várias vezes para capturar variabilidade |
| Qualidade não funcional | `S` / `N` | Estrutura/manutenibilidade/performance (ex.: ISO 25010, SonarQube, smells) |
| Agente (≠ modelo) | `S` / `N` | Objeto de estudo são **agentes de programação** (Codex, Claude Code, Cursor...) |
| ≥3 modelos/agentes | `S` / `N` | Comparação entre pelo menos 3 geradores |

---

## 3. Tabela de codificação (25 artigos)

| ID | Tipo | Unidade | Sist. compl. | Oráculo indep. | Defeitos | Segurança | Reprodut. | Múlt. exec. | Não-func. | Agente | ≥3 geradores |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A01 | SLR | Revisão | — | — | — | — | — | — | — | N | — |
| A02 | SLR | Revisão | — | — | — | — | — | — | — | N | — |
| B01 | Empírico | Snippet/função | N | N | S | N | N | N | N | N | S (3) |
| B02 | Empírico | Snippet/função | N | N | S | N | N | N | N | N | S (7) |
| B03 | Empírico | Snippet/função | N | N | S | S | N | N | N | N | S (3) |
| B04 | Empírico | Snippet/função | N | N | N | N | S | S | N | N | N |
| C01 | Survey | Revisão | — | — | — | — | — | — | — | N | — |
| C02 | Empírico | Snippet/função | N | S | N | N | N | N | N | N | N |
| C03 | Empírico | Testes | N | N | N | N | N | N | N | N | N |
| C04 | Empírico | Testes | N | N | N | N | N | N | N | N | N |
| C05 | Empírico | Snippet/função | N | N | N | N | N | N | N | N | N |
| C06 | Empírico | Testes | N | N | N | N | N | N | N | N | N |
| D01 | Empírico | Snippet/função | N | S | N | N | N | N | N | N | S (3) |
| D02 | Empírico | Snippet/função | N | N | S | N | N | N | S | N | N |
| D03 | Empírico | Sistema (web app) | S | S | N | N | N | N | N | N | N |
| D04 | Misto | Snippet/função (patch) | N | N | N | N | N | N | S | N | S (3) |
| D05 | Retro | Dados (commits) | N | N | S | N | N | N | S | S (5 assist.) | S (5) |
| E01 | Retro | Snippet/função | N | N | N | S | N | N | N | N | S (3 tools) |
| E02 | Empírico | Snippet/função | N | N | N | S | N | N | N | N | S (7) |
| E03 | Empírico | Snippet/função | N | N | N | S | N | N | N | N | S (5) |
| F01 | Retro | Dados (PRs) | N | N | N | N | N | N | N | S | S (3) |
| F02 | Empírico | Sistema completo (projetos) | S | N | N | N | S | N | N | S | S (3) |
| F03 | Empírico | Parcial (interações reais) | P | N | N | S | N | N | N | N | N |
| F04 | Retro | Dados (PRs) | N | N | N | N | N | N | N | S | S (5) |
| F05 | Retro | Dados (PRs) | N | N | S | N | N | N | N | S | S (5) |

---

## 4. Frequências por dimensão (N=25)

| Dimensão | Contagem | % |
|---|---|---|
| **Tipo:** Revisão (SLR/Survey) | 3 | 12% |
| **Tipo:** Empírico (experimental/controlado) | 16 | 64% |
| **Tipo:** Empírico retrospectivo | 5 | 20% |
| **Tipo:** Misto | 1 | 4% |
| Unidade: snippet/função/algoritmo/patch | 12 | 48% |
| Unidade: testes gerados | 3 | 12% |
| Unidade: **sistema completo** | 2 | 8% |
| Unidade: sistema parcial (não controlado) | 1 | 4% |
| Unidade: dados retrospectivos (commits/PRs) | 4 | 16% |
| Unidade: revisão | 3 | 12% |
| **Oráculo independente** | 3 | 12% |
| **Defeitos como objeto central** | 6 | 24% |
| **Segurança avaliada** | 5 | 20% |
| **Reprodutibilidade/não-determinismo** | 2 | 8% |
| **Múltiplas execuções para variabilidade** | 1 | 4% |
| **Qualidade não funcional** | 3 | 12% |
| **Agentes de programação** (≠ modelo) | 5 | 20% |
| Comparação IA vs humano | 3 | 12% |
| Comparação de ≥3 modelos/agentes | 10 | 40% |

---

## 5. Análises cruzadas (as que mais sustentam a lacuna)

| Cruzamento | Contados | % | Interpretação |
|---|---|---|---|
| Sistema completo **+** oráculo independente | 1 (D03) | 4% | Quase ninguém avalia um sistema inteiro com critérios fora do gerador |
| Sistema completo **+** defeitos | 0 | 0% | Nenhum estudo gera sistema completo **e** caracteriza seus defeitos |
| Sistema completo **+** segurança | 0 | 0% | Nenhum estudo gera sistema completo **e** avalia vulnerabilidades |
| Sistema completo **+** reprodutibilidade | 1 (F02) | 4% | Só o estudo de reprodutibilidade gera projetos inteiros (mas sem defeitos/segurança/oráculo) |
| Agente **+** sistema completo | 1 (F02) | 4% | Só 1 estudo investiga agentes gerando sistemas completos |
| Agente **+** sistema completo **+** oráculo indep. **+** múltiplas execuções **+** segurança **+** defeitos | **0** | **0%** | A combinação integral da nossa proposta não aparece em nenhum estudo |

**Leitura direta:** a literatura revisada cobre bem os fragmentos (código, testes, defeitos, segurança) de forma **isolada**, mas o desenho **integrado e controlado** — mesma especificação → diferentes agentes → sistemas completos → múltiplas execuções → oráculo independente → defeitos + segurança + manutenibilidade + reprodutibilidade → estatística — não foi encontrado.

---

## 6. Leitura das lacunas (G1–G5)

- **G1 — Sistemas completos:** só **8%** (2/25) geram sistemas/projetos completos; **48%** trabalham com snippets/funções e **16%** com dados retrospectivos.
- **G2 — QA independente:** apenas **12%** (3/25) usam oráculo independente (C02, D01, D03), e só **1** deles com sistema completo (D03).
- **G3 — Código + testes + defeitos juntos:** 0 estudos combinam sistema completo + defeitos; os estudos de testes (C03, C04, C06) não avaliam os defeitos dos sistemas que os testes deveriam cobrir.
- **G4 — Comparação controlada entre agentes:** 5 estudos (20%) investigam agentes, mas só **1 (4%)** com sistema completo (F02) e **0** com o desenho integral (mesmo requisito/prompt + múltiplas execuções + oráculo independente).
- **G5 — Métricas de teste contestadas:** apenas 2–3 estudos (C05, C06) problematizam coverage/mutation como evidência de qualidade; nenhum combina métricas múltiplas com detecção real de defeitos em sistemas completos.

---

## 7. Implicações para o desenho experimental

A análise quantitativa **direciona** cada decisão metodológica:

| Decisão do experimento | Justificativa quantitativa |
|---|---|
| Sistema completo (ex.: API de tarefas), não snippet | Apenas 8% dos estudos fazem isso; 0% combinam com defeitos |
| Mesmo requisito + mesmo prompt para todos os agentes | Nenhum estudo (0%) faz comparação controlada desse tipo para sistemas completos |
| ≥3 execuções por agente | Só 4% dos estudos tratam a variabilidade entre execuções |
| Oráculo independente do gerador | Só 12% usam oráculo independente; é prática rara e nosso diferencial |
| Defeitos + segurança + manutenibilidade juntos | 0% combinam sistema completo + defeitos + segurança |
| Não confiar em coverage/mutation isolados (C05) | 2 estudos contestam essas métricas; nosso oráculo deve combinar métricas |
| Incluir corner cases e valores especiais (None/inf/NaN, cf. C06) | Estudos mostram que testes de IA omitem sistematicamente esses casos |
| Medir reprodutibilidade/executabilidade (F02) | Só 8% dos estudos medem; agrega dimensão ausente na maioria |

---

## 8. Limitações desta análise

1. **Amostra de conveniência:** 25 estudos identificados em buscas iniciais, não uma SLR exaustiva com query registrada e dupla triagem.
2. **Codificação preliminar:** classificações de alguns estudos dependem de confirmar autores/DOIs (*a confirmar*); nova evidência pode alterar células da tabela.
3. **Campos binários simplificados:** dimensões como "oráculo independente" têm gradação; a tabela usa S/N para permitir contagem reproduzível.
4. **Viés de seleção:** a busca favoreceu os eixos da pesquisa (defeitos, testes, segurança, qualidade, agentes); pode haver estudos fora desses eixos.
5. Recomenda-se: registrar strings de busca e bases usadas, e reexecutar esta codificação quando a matriz fechar 30 artigos consolidados.

---

*Documento de trabalho — revisar ao consolidar DOIs e expandir a matriz.*