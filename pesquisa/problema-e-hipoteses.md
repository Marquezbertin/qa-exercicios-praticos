# Problema, Perguntas de Pesquisa e Hipóteses — Rascunho

> **Status: RASCUNHO — não consolidado.** O plano da pesquisa é fechar estas definições somente após a revisão bibliográfica sistemática (matriz com 25–30 artigos). Este arquivo preserva o estado da discussão para servir de base.

---

## 1. Problema

A crescente utilização de LLMs e agentes de IA aumenta a capacidade de geração de software, mas ainda existem questões abertas sobre:

- a **qualidade** do software produzido (funcional e não funcional);
- os **tipos de defeitos** introduzidos;
- a **capacidade de detecção** desses defeitos (inclusive pelos testes gerados pela própria IA).

## 2. Objetivo geral

Avaliar empiricamente a qualidade e os defeitos presentes em sistemas de software produzidos por diferentes agentes/modelos de IA sob condições experimentais controladas.

## 3. Objetivos específicos

1. Comparar diferentes IAs/agentes na produção de software a partir do mesmo requisito.
2. Identificar defeitos nos artefatos gerados.
3. Classificar os defeitos (base: taxonomia de Tambon et al. [B01]; severidade).
4. Avaliar a severidade dos defeitos.
5. Medir cobertura e efetividade de testes.
6. Avaliar qualidade estrutural (ISO/IEC 25010 como referência [D04]).
7. Avaliar segurança (CWE/OWASP [E01]–[E03]).
8. Investigar a capacidade da própria IA de detectar seus defeitos.
9. Comparar os resultados estatisticamente.

## 4. Pergunta principal

> Como diferentes agentes de Inteligência Artificial generativa influenciam a qualidade, a densidade e a natureza dos defeitos, a testabilidade e a reprodutibilidade de sistemas de software desenvolvidos sob requisitos controlados?

## 5. Perguntas de pesquisa (rascunho RQ1–RQ8)

- **RQ1:** Existem diferenças na qualidade funcional entre sistemas produzidos por diferentes agentes?
- **RQ2:** Existem diferenças na densidade de defeitos?
- **RQ3:** Quais categorias de defeitos são predominantes em cada agente?
- **RQ4:** Existem diferenças na severidade dos defeitos?
- **RQ5:** Existem diferenças de segurança e manutenibilidade?
- **RQ6:** Os testes gerados pelo próprio agente conseguem detectar seus defeitos?
- **RQ7:** Quão reprodutíveis são os sistemas gerados?
- **RQ8:** Quanto os resultados variam entre execuções do mesmo agente? *(justificada pelo não-determinismo [B04])*

## 6. Hipóteses (rascunho)

- **H1:** Há diferenças estatisticamente significativas na **densidade de defeitos** entre softwares produzidos por diferentes agentes/modelos a partir dos mesmos requisitos.
- **H2:** Diferentes modelos produzem **distribuições diferentes de categorias de defeitos** (perfil de defeitos — cf. [B03]).
- **H3:** A utilização de IA para geração de testes **não garante a detecção** dos defeitos introduzidos pela própria IA ([C03], [C04]).
- **H4:** A qualidade funcional do software **não é suficiente** para representar sua qualidade global (é preciso avaliar vulnerabilidades, performance, manutenibilidade, edge cases, dívida técnica — cf. [D04]).

## 7. Princípios metodológicos já assumidos

- **Mesmo requisito** para todas as IAs.
- **Mesmo prompt/especificação** (sem melhorar prompt para "corrigir" uma IA).
- **Mesma quantidade de oportunidades**: ≥3 execuções independentes por modelo (não-determinismo [B04]).
- **Oráculo independente** da IA geradora:
  - testes funcionais (unitários, integração, API, E2E);
  - testes negativos (invalid input, extremos, ausência de dados, permissões, autenticação);
  - segurança (OWASP, vulnerabilidades, dependências);
  - qualidade estrutural (complexidade, duplicação, code smells, manutenibilidade).
- **Matriz de defeitos**: `ID · IA · Categoria · Severidade · Detectado automaticamente?`.
- **Análise estatística** sobre os resultados (comparações entre modelos).
- **Neutralidade experimental:** a pesquisa não parte de "IA é ruim" — deve permitir que os dados mostrem IA melhor, igual ou pior conforme o contexto ([D02](), [D03]()).

## 8. Dimensões do experimento

- **A — Qualidade:** quanto software funcional a IA consegue produzir?
- **B — Defeitos:** quais defeitos são produzidos (taxonomia + severidade)?
- **C — Testabilidade:** os testes conseguem encontrar esses defeitos? (diferencial da pesquisa)

## 9. Decisões em aberto (não definir ainda)

- Título final (provisório: "Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados").
- Stack do experimento: Python + FastAPI + PostgreSQL **ou** Node.js + TypeScript + PostgreSQL.
- Lista definitiva de RQs/hipóteses (fundamentar na matriz após revisão completa).
- Inclusão (ou não) de variável "revisão pela própria IA" (self-correction [B02]) na primeira versão — **provável exclusão** para manter o estudo controlado.