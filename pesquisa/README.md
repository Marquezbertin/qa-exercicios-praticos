# 📄 Projeto de Pesquisa — Avaliação da Qualidade e Defeitos em Software Gerado por IA

> Trabalho científico em desenvolvimento. Este repositório também contém exercícios práticos de QA; a pesquisa fica organizada nesta pasta (`pesquisa/`).

## Título provisório

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados**

## Área / Subárea

Engenharia de Software · Software Quality / Software Testing / Generative AI

## Estado atual

**Fase 1 — Revisão bibliográfica (em andamento).** Busca concluída; matriz consolidada com **25 artigos**, DOIs e metadados verificados (16 com DOI de periódico/conferência, 8 arXiv/preprint, 1 relatório institucional sem DOI); análise quantitativa v1 e **mapa da literatura + lacuna final** prontos.

| Etapa | Status |
|---|---|
| Revisão bibliográfica — Parte 1 | ✅ base concluída (v0.3) |
| Matriz de artigos (25–30) | ✅ 25 registrados, DOIs/metadados consolidados |
| Análise quantitativa da matriz | ✅ v1 (frequências e cruzamentos) |
| Mapa da literatura / análise de lacunas | ✅ v0.1 (provado/controverso/inexplorado/lacuna final) |
| Problema de pesquisa + RQs + hipóteses | ✅ consolidado (v0.2, ancorado no mapa) |
| Metodologia experimental | 🔶 v0.1 (proposta; stack definida: Python + FastAPI + PostgreSQL) |
| Experimento controlado | ⏳ não iniciado |
| Escrita do artigo | ⏳ não iniciada |

## Estrutura desta pasta

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Este guia do projeto de pesquisa |
| `revisao-bibliografica.md` | Documento principal da Parte 1 (método, síntese, lacunas) |
| `matriz-de-artigos.md` | Matriz detalhada com as fichas completas dos artigos (A–F) |
| `mapa-da-literatura.md` | Mapa: o que foi provado, o que é controvertido, o que é inexplorado e a lacuna final |
| `analise-quantitativa.md` | Análise quantitativa da matriz (frequências e cruzamentos que sustentam a lacuna) |
| `problema-e-hipoteses.md` | Problema, perguntas de pesquisa e hipóteses (consolidado) |
| `metodologia-experimental.md` | Protocolo do experimento controlado (oráculo independente, stack, métricas, estatística) |

## Convenções

- Cada artigo recebe um **ID** agrupado por tema: A (LLM→ES), B (defeitos), C (testes), D (qualidade), E (segurança), F (agentes de programação).
- Padrão dos campos da matriz: **ID · Autor · Ano · Publicação · DOI · Tipo · Modelo · Agente · Linguagem · Amostra · Sistema completo? · Testes independentes? · Métricas · Bugs avaliados como? · Segurança? · Resultado principal · Limitações · Lacuna para nossa pesquisa**.
- Campos não confirmados nas buscas ficam marcados como **"a confirmar"** (nunca inventamos DOI/autor).
- Cada nova inclusão na matriz deve ter DOI ou link verificados antes de ser consolidada.

## Próximos passos

1. **Fechar decisões da metodologia** (seção 11 do protocolo): lista de agentes, detalhamento da especificação, ferramentas do oráculo.
2. Fase 1 do experimento: fechar especificação v1.0 e construir o **oráculo independente** (artefatos privados, fora do alcance dos agentes).
3. Definir a contribuição/confirmação do trabalho (evidências, metodologia, discussão) junto aos orientadores.
4. Expandir a matriz para 25–30+ (busca sistemática contínua), se necessário para um SLR formal.