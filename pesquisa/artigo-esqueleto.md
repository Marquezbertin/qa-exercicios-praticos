# ARTIGO CIENTÍFICO — Esqueleto (estrutura integrada)

> **Estado:** ESQUELETO v0.1 — estrutura e rastreabilidade dos conteúdos. Redação das seções pendente.
> **Status das decisões:** formato de publicação (periódico/conferência) e pré-registro formal **ainda não decididos**; subseção do laboratório (Discussão 5.2) **confirmada** como material complementar não-evidenciário.
> **Formato:** estrutura genérica IMRaD (adaptável ao veículo escolhido).
> Este arquivo mapeia **onde** cada conteúdo já produzido entra; não substitui os documentos-fonte.

---

## TÍTULO (provisório)

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados**

- Resumo do entregável e abstração das variáveis: *não finalizado — depende de decisões de formato e dos números finais*.
- **Backlog:** refinamento do título após decidir público-alvo e limiar de evidência assumido.

---

## 1. Resumo / Abstract

| Campo | Conteúdo implicado | Fonte pronta? |
|---|---|---|
| Contexto | Software gerado por agentes de IA; lacuna G1–G5 (0 estudos combinam sistema completo + defeitos + segurança + múltiplas execuções + oráculo independente) | mapa-da-literatura.md |
| Objetivo | Comparar 4 agentes (opencode com 4 modelos distintos) na geração de sistema completo desde especificação controlada | problema-e-hipoteses.md (§2/§3) |
| Método | Experimento controlado prospectivo, 4 modelos × 3 execuções (n=12), oráculo independente de 81 testes + NFR + matriz de defeitos (taxonomia Tambon + severidade) + análise estatística | metodologia-experimental.md (§2–§9) |
| Resultados | 3/12 bootáveis; 12 defeitos (100% Blocker/Critical); perfis por agente; padrões reincidentes; κ; χ²/Fisher | metodologia-experimental.md (§13) |
| Conclusão | Vale comum de qualidade entre modelos free; aprovação própria ≠ validação independente; neutralidade preservada | rascunho-discussao-artigo.md (5.4) |

- **Palavras-chave (sugestão):** *software gerado por IA; agentes de código; qualidade de software; defeitos; oráculo independente; testes de software; Engenharia de Software; experimento controlado*.

---

## 2. Introdução

| Conteúdo | Fonte |
|---|---|
| Motivação: IA já produz software funcional (D03) mas com perfil de defeitos próprio, vulnerabilidades, dívida técnica e reprodutibilidade limitada | revisao-bibliografica.md; mapa-da-literatura.md (§1) |
| Lacuna: nenhum estudo combina na mesma cadeia sistema completo + defeitos + segurança + múltiplas execuções + oráculo independente (G1–G5) | mapa-da-literatura.md (§3–§4) |
| Problema de pesquisa e justificativa (neutralidade C1: os dados decidem) | problema-e-hipoteses.md (§1) |
| Objetivo geral + objetivos específicos (9) | problema-e-hipoteses.md (§3) |
| Contribuições do artigo (rascunhar: 1º experimento controlado do tipo; evidência de padrões reincidentes; evidência sobre testabilidade RQ6 a partir da própria pesquisa) | a derivar |

- **Backlog:** redigir parágrafos; montar figura/fluxo do desenho (espec→agente→oráculo→matriz).

---

## 3. Trabalhos Relacionados / Revisão (condensada)

| Conteúdo | Fonte |
|---|---|
| LLMs em Engenharia de Software (A01, A02) | revisao-bibliografica.md (§3 A) |
| Defeitos em código gerado (B01 taxonomia; B02; B03 perfis; B04 não-determinismo) | revisao-bibliografica.md (§3 B) |
| Testes de LLMs (C01–C06: test smells, detecção limitada, coverage/mutation contestados, omissão de corner cases) | revisao-bibliografica.md (§3 C) |
| Qualidade e não-funcional (D01–D05: ISO 25010, dívida) | revisao-bibliografica.md (§3 D) |
| Segurança (E01–E03) | revisao-bibliografica.md (§3 E) |
| Agentes de código (F01–F05: reprodutibilidade 68,3%; reversões 0,7%–7,6%) | revisao-bibliografica.md (§3 F) |
| Gap: G1–G5 + lacuna final; por que não são satisfeitos pelos estudos existentes | mapa-da-literatura.md (§4–§5) |

- **Backlog:** condensar 25 artigos em seção sintética; formatar citações no padrão do veículo.

---

## 4. Metodologia

### 4.1 Desenho experimental
- Experimento controlado, prospectivo, reproduzível; 1 grupo por agente; unidade = sistema completo (API REST de Tarefas) — metodologia §1–§2.
- Tratamento = identidade do modelo dentro do agente opencode (mesmo loop de ferramenta, D8) — §2.1.
- ≥3 execuções independentes por modelo (trata RQ8; B04); ambiente idêntico por execução — §2, §7.

### 4.2 Especificação controlada
- Sistema: API REST de Gerenciamento de Tarefas (escopo moderado) — §3.
- FR1–FR8 (inclui validação, permissões, erros padronizados, testes) e NFR (segurança, manutenibilidade, reprodutibilidade, performance) — §3.1–3.2.
- Documento entregue único, idêntico a todos (especificação v1.0, privada; congelada em 2026-09-05).

### 4.3 Oráculo independente
- 5 camadas: funcional, negativo (inclui None/inf/NaN — C06), segurança, estrutura, testabilidade — §4.
- 81 testes; validado contra sistema golden (não-IA); privado/imutável — §4.
- Regra: coverage reportado mas não tratado como evidência (C05) — §4.

### 4.4 Matriz de defeitos e classificação
- Campos: ID, agente/execução, local, categoria (taxonomia Tambon, 10 padrões), severidade (Blocker/Critical/Major/Minor), detecção (oráculo?), evidência — §5.
- Dupla classificação independente + κ de Cohen + resolução de divergências — §5.

### 4.5 Métricas e análise estatística
- Mapeamento RQ→métrica→instrumento (§6); testes propostos (Kruskal-Wallis, χ², Fisher, Cramér's V; variabilidade RQ8) (§8).
- Ambiente: sem Docker (D9 rev2 — validação nativa Postgres; contêineres avaliados estruturalmente) — §7.
- Ética/pré-registro: hipóteses fixadas antes da coleta (repo privado); neutralidade C1 — §9.

### 4.6 Limitações do desenho
- n pequeno, células esperadas <5, severidade influenciada por não-bootáveis, sem execução funcional nos não-bootáveis — §13.6 (espelhar na metodologia).

- **Backlog:** converter em seção formal (hoje é protocolo de trabalho); incluir detalhes de amostra exata e ferramentas.

---

## 5. Resultados

| § do artigo | Conteúdo | Fonte |
|---|---|---|
| 5.1 Caracterização das entregas | 12 entregas (4×3); 3/12 bootáveis; NFR estáticos; manifestos | metodologia §13.1 |
| 5.2 Qualidade funcional (RQ1) | pass rates: lightning/e3=1 (32F+48E); mimo/e2 e e3=12 (21F+48E) | metodologia §13.1, results privados |
| 5.3 Defeitos e densidade (RQ2/H1; RQ3/H2) | 12 defeitos; densidades 1,36/0,93/0,92/0,55; perfis por agente; χ² p=0,041 V=0,85; Fisher ultra p=0,010 | metodologia §13.1–13.2 |
| 5.4 Severidade (RQ4) | 100% Blocker/Critical (8 Blocker/4 Critical) | metodologia §13.1 |
| 5.5 Padrões reincidentes | dependência ausente 5×; passlib+bcrypt 3–4×; alembic 2×; versão fantasma 1× | metodologia §13.3 |
| 5.6 Testabilidade (RQ6/H3) | testes do agente vs oráculo (matriz 2×2 por defeito) — pendente consolidar da análise privada | results privados (analise_estatistica.md) |
| 5.7 Concordância e reprodutibilidade (RQ7) | κ 0,54 categoria / 0,91 severidade; executabilidade 3/12; variabilidade RQ8 qualitativa | metodologia §13.4–13.5 |
| 5.8 Qualidade global (RQ5/H4) | funcional vs NFR divergentes; índice único colapsaria dimensões | metodologia §13.7 |

- **Backlog:** gerar tabelas/figuras (barras densidade; heatmap defeito×agente; gráfico de perfis; matriz de confusão κ; funnel bootabilidade).

---

## 6. Discussão

| Conteúdo | Fonte |
|---|---|
| 6.1 Achados principais (H1–H4; RQ1–RQ8) e leitura honesta do poder estatístico | rascunho-discussao-artigo.md 5.1 |
| 6.2 Laboratório exploratório complementar — **NÃO-evidenciário** (decisão: INCLUIR) | rascunho-discussao-artigo.md 5.2; EXP-001/EXP-002 |
| 6.3 Limitações centrais | rascunho-discussao-artigo.md 5.3 |
| 6.4 Síntese (neutralidade; "vale comum de qualidade"; aprovação própria ≠ validação) | rascunho-discussao-artigo.md 5.4 |

- **Backlog:** converter rascunho v0.2 em texto contínuo do artigo; integrar citações ao padrão do veículo.

---

## 7. Conclusão e Trabalhos Futuros

| Conteúdo implicado | Fonte |
|---|---|
| Conclusão sobre H1–H4 e RQ1–RQ8 com a honestidade do n=12 | rascunho-discussao-artigo.md 5.4; metodologia §13.7 |
| Trabalhos futuros: EXP-003 e EXP-bridge (laboratório); extensão da amostra (χ² com células ≥5); execução Docker em máquina de produção; SLR formal se exigido | laboratorio-exploratorio/EXP-003; laboratorio/README (privado); pesquisa README (próximos passos) |

- **Backlog:** redigir.

---

## 8. Referências

- Fonte: `matriz-de-artigos.md` (fichas com DOI) + `revisao-bibliografica.md`.
- **Backlog:** montar lista final no padrão do veículo; confirmar DOI de F02 e F05; decidir inclusão de A/A2 e D01/D03 conforme seções citadas.

---

## Backlog de pendências não-textuais

| Pendência | Tipo |
|---|---|
| Decidir formato/periódico/conferência e padrão de citação | Decisão com orientadores |
| Pré-registro formal (repo privado) se o veículo exigir | Decisão + ação |
| Confirmar DOI de [F02] e [F05] | Verificação |
| Decidir / confirmar amostra final (n=12 ok) e se haverá extensão (células ≥5) | Decisão |
| Gerar figuras (densidade, perfis, heatmap, bootabilidade, κ) | Ação de produção |
| Montar seção 5.6 RQ6/H3 (matriz 2×2 agente vs oráculo) a partir dos dados privados | Ação de análise |
| Checar redação da seção 5.2 para não vazar "evidência cruzada" (limite de não-evidenciário) | Revisão |

---

*Esqueleto v0.1 — 2026-09-06. Próxima ação recomendada: decidir formato com orientadores → redigir Introdução e Metodologia.*