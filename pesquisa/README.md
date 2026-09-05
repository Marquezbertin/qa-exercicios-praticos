# 📄 Projeto de Pesquisa — Avaliação da Qualidade e Defeitos em Software Gerado por IA

> Trabalho científico em desenvolvimento. Este repositório também contém exercícios práticos de QA; a pesquisa fica organizada nesta pasta (`pesquisa/`).

## Título provisório

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados**

## Área / Subárea

Engenharia de Software · Software Quality / Software Testing / Generative AI

## Estado atual

**Fase 1 — Revisão bibliográfica (em andamento).** Busca inicial concluída; matriz com ~19 artigos levantada; refinamento e expansão para 25–30 artigos em curso.

| Etapa | Status |
|---|---|
| Revisão bibliográfica — Parte 1 | ✅ em andamento |
| Matriz de artigos (25–30) | 🔶 ~19 registrados |
| Mapa da literatura / análise de lacunas | 🔶 em construção |
| Problema de pesquisa + RQs + hipóteses | 🔶 rascunho salvo |
| Metodologia experimental | ⏳ não iniciada |
| Experimento controlado | ⏳ não iniciado |
| Escrita do artigo | ⏳ não iniciada |

## Estrutura desta pasta

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Este guia do projeto de pesquisa |
| `revisao-bibliografica.md` | Documento principal da Parte 1 (método, síntese, lacunas) |
| `matriz-de-artigos.md` | Matriz detalhada com as fichas completas dos artigos (A–F) |
| `problema-e-hipoteses.md` | Rascunho: problema, perguntas de pesquisa e hipóteses |

## Convenções

- Cada artigo recebe um **ID** agrupado por tema: A (LLM→ES), B (defeitos), C (testes), D (qualidade), E (segurança), F (agentes de programação).
- Padrão dos campos da matriz: **ID · Autor · Ano · Publicação · DOI · Tipo · Modelo · Agente · Linguagem · Amostra · Sistema completo? · Testes independentes? · Métricas · Bugs avaliados como? · Segurança? · Resultado principal · Limitações · Lacuna para nossa pesquisa**.
- Campos não confirmados nas buscas ficam marcados como **"a confirmar"** (nunca inventamos DOI/autor).
- Cada nova inclusão na matriz deve ter DOI ou link verificados antes de ser consolidada.

## Próximos passos

1. Expandir a matriz para 25–30 artigos (buscar sistematicamente ACM, IEEE, Springer, Elsevier, arXiv).
2. Consolidar DOIs e metadados de cada artigo.
3. Construir o **mapa da literatura**: o que já foi provado, o que é controverso, o que é lacuna.
4. Fechar problema de pesquisa + RQs + hipóteses com fundamentação.
5. Definir e documentar a metodologia experimental (requisitos controlados, mesmos prompts, múltiplas execuções, oráculo independente).