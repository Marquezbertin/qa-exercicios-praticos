# 📄 Projeto de Pesquisa — Avaliação da Qualidade e Defeitos em Software Gerado por IA

> Trabalho científico em desenvolvimento. Este repositório também contém exercícios práticos de QA; a pesquisa fica organizada nesta pasta (`pesquisa/`).

## Título provisório

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados**

## Área / Subárea

Engenharia de Software · Software Quality / Software Testing / Generative AI

## Estado atual

**Fase 1 — Revisão bibliográfica (em andamento).** Busca concluída; matriz consolidada com **25 artigos**, DOIs e metadados verificados (16 com DOI de periódico/conferência, 8 arXiv/preprint, 1 relatório institucional sem DOI).

| Etapa | Status |
|---|---|
| Revisão bibliográfica — Parte 1 | ✅ base concluída (v0.3) |
| Matriz de artigos (25–30) | ✅ 25 registrados, DOIs/metadados consolidados |
| Análise quantitativa da matriz | ✅ v1 (frequências e cruzamentos) |
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
| `analise-quantitativa.md` | Análise quantitativa da matriz (frequências e cruzamentos que sustentam a lacuna) |
| `problema-e-hipoteses.md` | Rascunho: problema, perguntas de pesquisa e hipóteses |

## Convenções

- Cada artigo recebe um **ID** agrupado por tema: A (LLM→ES), B (defeitos), C (testes), D (qualidade), E (segurança), F (agentes de programação).
- Padrão dos campos da matriz: **ID · Autor · Ano · Publicação · DOI · Tipo · Modelo · Agente · Linguagem · Amostra · Sistema completo? · Testes independentes? · Métricas · Bugs avaliados como? · Segurança? · Resultado principal · Limitações · Lacuna para nossa pesquisa**.
- Campos não confirmados nas buscas ficam marcados como **"a confirmar"** (nunca inventamos DOI/autor).
- Cada nova inclusão na matriz deve ter DOI ou link verificados antes de ser consolidada.

## Próximos passos

1. Construir o **mapa da literatura** (o que já foi provado, o que é controverso, o que é lacuna) a partir da matriz consolidada.
2. Fechar problema de pesquisa + RQs + hipóteses com fundamentação.
3. Definir e documentar a metodologia experimental (requisitos controlados, mesmos prompts, múltiplas execuções, oráculo independente).
4. Definir a contribuição/confirmação do trabalho (metodologia, evidências, discussão) junto aos orientadores.
5. Expandir a matriz para 25–30+ (busca sistemática contínua), se necessário para um SLR formal.