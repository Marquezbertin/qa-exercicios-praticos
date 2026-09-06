# 📄 Projeto de Pesquisa — Avaliação da Qualidade e Defeitos em Software Gerado por IA

> Trabalho científico em desenvolvimento. Este repositório também contém exercícios práticos de QA; a pesquisa fica organizada nesta pasta (`pesquisa/`).

## Título provisório

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados**

## Área / Subárea

Engenharia de Software · Software Quality / Software Testing / Generative AI

## Estado atual

**Fase 2 — Experimento controlado CONCLUÍDO (2026-09-06).** Oráculo independente (81 testes, privado), sistema golden, piloto e batch completo **4 modelos × 3 execuções = 12 entregas** validados. Resultados: **3/12 bootáveis**, 12 defeitos classificados (taxonomia Tambon, dupla classificação), concordo inter-avaliador κ=0,54 (categoria, moderado) e κ=0,91 (severidade, quase perfeito), análise estatística disponível na seção 13 da metodologia.

| Etapa | Status |
|---|---|
| Revisão bibliográfica — Parte 1 | ✅ base concluída (v0.3) |
| Matriz de artigos (25–30) | ✅ 25 registrados, DOIs/metadados consolidados |
| Análise quantitativa da matriz | ✅ v1 (frequências e cruzamentos) |
| Mapa da literatura / análise de lacunas | ✅ v0.1 (provado/controverso/inexplorado/lacuna final) |
| Problema de pesquisa + RQs + hipóteses | ✅ consolidado (v0.2, ancorado no mapa) |
| Metodologia experimental | ✅ v0.2 executado; resultados na seção 13 |
| Especificação controlada FR/NFR | ✅ **v1.0 congelada** (aprovada em 2026-09-05; decisões D1–D7 registradas) |
| Experimento controlado | ✅ **CONCLUÍDO** (piloto + batch 4×3 + classificação + análise estatística) |
| Escrita do artigo | ⏳ não iniciada (seção de resultados disponível para consolidação) |

## Estrutura desta pasta

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Este guia do projeto de pesquisa |
| `revisao-bibliografica.md` | Documento principal da Parte 1 (método, síntese, lacunas) |
| `matriz-de-artigos.md` | Matriz detalhada com as fichas completas dos artigos (A–F) |
| `mapa-da-literatura.md` | Mapa: o que foi provado, o que é controvertido, o que é inexplorado e a lacuna final |
| `analise-quantitativa.md` | Análise quantitativa da matriz (frequências e cruzamentos que sustentam a lacuna) |
| `problema-e-hipoteses.md` | Problema, perguntas de pesquisa e hipóteses (consolidado) |
| `metodologia-experimental.md` | Protocolo do experimento controlado (oráculo independente, stack, métricas, estatística) **+ resultados da execução completa** (seção 13) |
| `especificacao-tarefas-v1.0.md` | Especificação controlada FR/NFR (documento entregue aos agentes; oráculo é privado) |
| `laboratorio-exploratorio/` | Estudos exploratórios de comportamento de chat-LLMs em tarefas de QA (NÃO é evidência da pesquisa formal) — EXP-001 (detecção de defeitos) e EXP-002 (geração de casos de teste) |

## Resultados-resumo (Fase 2 — repo privado tem evidências completas)

- **12 execuções** (4 modelos opencode × 3), 2 pilotos excluídos; free-tier.
- **3/12 bootáveis** (lightning/e3, mimo/e2, mimo/e3) — nenhuma delivery passou 100% do oráculo (81 testes).
- **12 defeitos** Tambon, 100% Blocker/Critical; densidade lightning 1,36 > ultra 0,93 ≈ mimo 0,92 > ling 0,55 /KLOC.
- **Perfil**: ultra = `incomplete_generation` concentrado (Fisher p=0,010); demais sem perfil dominante.
- **Padrões reincidentes**: dependência ausente (4; +1 piloto), passlib+bcrypt→500 (3; +1 piloto), misconfig alembic (1; +1 piloto), versão fantasma (1).
- **κ**: categoria 0,54 (moderado) · severidade 0,91 (quase perfeito).
- χ² agente×categoria p=0,041 (V=0,85) — **informativo, não conclusivo** (células <5 no n=12).
- Leitura honesta e limitações detalhadas na **seção 13** da metodologia.

## Convenções

- Cada artigo recebe um **ID** agrupado por tema: A (LLM→ES), B (defeitos), C (testes), D (qualidade), E (segurança), F (agentes de programação).
- Padrão dos campos da matriz: **ID · Autor · Ano · Publicação · DOI · Tipo · Modelo · Agente · Linguagem · Amostra · Sistema completo? · Testes independentes? · Métricas · Bugs avaliados como? · Segurança? · Resultado principal · Limitações · Lacuna para nossa pesquisa**.
- Campos não confirmados nas buscas ficam marcados como **"a confirmar"** (nunca inventamos DOI/autor).
- Cada nova inclusão na matriz deve ter DOI ou link verificados antes de ser consolidada.

## Próximos passos

1. **Consolidar a seção de resultados no artigo** (base: seção 13 da metodologia + análises privadas).
2. Decidir com orientadores o formato de publicação (periódico/conferência) e a formalização do pré-registro.
3. Se necessário, estender a amostra (mais execuções/execução em Docker na máquina de produção) para elevar o poder estatístico (células esperadas ≥5 para o χ²).
4. Manter a busca sistemática contínua se um SLR formal for exigido.