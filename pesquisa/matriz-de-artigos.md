# Matriz de Artigos — Revisão Bibliográfica

**Status:** buscas iniciais concluídas · **Meta:** 25–30 artigos · **Atual:** 19 registrados

> Convenção: campos marcados **"a confirmar"** ainda não foram verificados na fonte oficial (DOI, afiliação etc.). Antes de consolidar uma ficha, o DOI/link deve ser confirmado — nunca manter DOI inventado.

## Campos da ficha

`ID · Autor(es) · Ano · Universidade/Afiliação · Publicação · DOI · Tipo (SLR/Survey/Empírico/Misto) · Modelo(s) · Agente(s) · Linguagem(ns) · Amostra · Sistema completo? · Testes independentes? · Métricas · Bugs avaliados como? · Segurança avaliada? · Resultado principal · Limitações · Lacuna para nossa pesquisa`

---

## Grupo A — LLMs aplicados à Engenharia de Software

### A01 — Revisão sistemática de LLMs em Engenharia de Software
- **Autores:** Hou et al.
- **Ano:** 2024
- **Publicação:** ACM (ToSEM — Trans. on Software Engineering and Methodology)
- **DOI:** a confirmar
- **Tipo:** Revisão Sistemática (SLR)
- **Amostra:** 395 artigos (jan/2017–jan/2024)
- **Conteúdo:** 85 tarefas de SE em 6 atividades (Requisitos, Design, Desenvolvimento, Quality Assurance, Manutenção, Gerenciamento); modelos, datasets, técnicas de prompting, métodos de avaliação, desafios e lacunas.
- **Modelo/Ferramenta:** diversos
- **Sistema completo?** — · **Testes independentes?** —
- **Resultado principal:** LLMs permeiam todo o ciclo de SE; campo amplo com lacunas de pesquisa identificadas.
- **Limitações:** até jan/2024; rápido desatualização.
- **Lacuna:** contexto e vocabulário comum para nossas RQs; base para a seção de trabalhos relacionados.

### A02 — Revisão sistemática sobre geração de código por LLMs
- **Autores:** a confirmar
- **Ano:** 2025
- **Publicação:** IEEE Access
- **DOI:** a confirmar
- **Tipo:** SLR
- **Amostra:** 58 estudos
- **Resultado principal:** limitações recorrentes — alucinações, vulnerabilidades de segurança, baixa generalização e problemas de interpretabilidade.
- **Lacuna:** fundamenta o estudo de defeitos (alucinação, segurança) como objetos de avaliação.

---

## Grupo B — Defeitos em código gerado por LLMs

### B01 — Bugs em código gerado por LLMs
- **Autores:** Florian Tambon, Arghavan Moradi Dakhel, Amin Nikanjam, Foutse Khomh, Michel C. Desmarais, Giuliano Antoniol
- **Ano:** 2024
- **Publicação:** IEEE/ACM (empírico)
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Modelos:** CodeGen, PanGu-Coder, Codex
- **Amostra:** 333 bugs
- **Método:** análise de bugs em código gerado; taxonomia validada por 34 pesquisadores e profissionais
- **Bugs avaliados como?** Taxonomia de 10 padrões:
  1. Misinterpretation 2. Syntax Error 3. Silly Mistake 4. Prompt-biased Code 5. Missing Corner Case 6. Wrong Input Type 7. Hallucinated Object 8. Wrong Attribute 9. Incomplete Generation 10. Non-Prompted Consideration
- **Resultado principal:** defeitos de código gerado por LLM possuem padrões características e recorrentes.
- **Limitações:** código gerado em contexto de função/problema; sem sistema completo; sem avaliação de severidade.
- **Lacuna:** **usar a taxonomia como base da classificação de defeitos do nosso experimento.**

### B02 — O que está errado com código gerado por LLMs?
- **Autores:** Dou et al.
- **Ano:** 2024
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Modelos:** 3 LLMs fechados + 4 open source
- **Benchmarks:** 3 benchmarks + 140 tarefas do mundo real
- **Resultado principal:** distribuição de bugs difere entre benchmarks acadêmicos e mundo real; self-critique + correção iterativa elevou aprovação em 29,2% após 2 iterações.
- **Lacuna:** sugere futura variável "revisão pela própria IA", a manter fora da primeira versão do experimento (controlar primeiro).

### B03 — Código humano vs. código gerado por IA (grande escala)
- **Autores:** Cotroneo, Improta, Liguori
- **Ano:** 2025
- **Publicação:** IEEE ISSRE 2025
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico (large-scale)
- **Modelos:** ChatGPT, DeepSeek-Coder, Qwen-Coder
- **Linguagens:** Python, Java
- **Amostra:** >500 mil amostras
- **Métricas:** defeitos (ODC), vulnerabilidades (CWE), complexidade
- **Resultado principal:** perfis de defeitos diferentes entre IA e humanos; IA com mais constructs não utilizados, debugging hardcoded e vulnerabilidades de segurança de alto risco.
- **Lacuna:** aponta para **hipótese de perfil de defeitos** em vez de "mais/menos bugs"; base para comparar IA×IA também.

### B04 — Não-determinismo do ChatGPT em geração de código
- **Autores:** Ouyang et al.
- **Ano:** 2025
- **Publicação:** ACM
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Modelos:** ChatGPT
- **Benchmarks:** CodeContests, APPS, HumanEval (829 problemas)
- **Resultado principal:** mesmo prompt produz saídas diferentes; afeta correção, consistência e reprodutibilidade de experimentos.
- **Lacuna:** **justifica múltiplas execuções independentes por modelo** no nosso desenho experimental.

---

## Grupo C — LLM + testes de software

### C01 — Testes de software com LLMs (survey)
- **Autores:** Wang et al.
- **Ano:** 2024
- **Tipo:** Survey
- **Amostra:** 102 estudos
- **Resultado principal:** geração de casos de teste, geração de código de teste e reparo de programas são aplicações representativas.
- **Lacuna:** motiva dimensão C (testabilidade) da nossa pesquisa.

### C02 — Exame de código gerado por LLMs
- **Autores:** Beer et al.
- **Ano:** 2024
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico (controlado)
- **Modelos:** ChatGPT, GitHub Copilot
- **Linguagens:** Java, Python
- **Método:** geração de algoritmos + testes unitários; avaliação de correção, qualidade e cobertura
- **Testes independentes?** Sim
- **Resultado principal:** diferenças significativas entre modelos, linguagens, código vs. testes e ao longo do tempo.
- **Limitações:** algoritmos relativamente pequenos.
- **Lacuna:** avançar de algoritmos para **sistema completo controlado**.

### C03 — Test smells em testes gerados por Copilot (Brasil)
- **Autores:** a confirmar (CBSoft)
- **Ano:** a confirmar
- **Tipo:** Estudo Empírico
- **Resultado principal:** testes gerados por Copilot exibem test smells mesmo quando válidos.
- **Lacuna:** reforça que **testes da própria IA não bastam como oráculo**.

### C04 — Geração de testes em larga escala (Defects4J)
- **Autores:** a confirmar
- **Ano:** a confirmar
- **Tipo:** Estudo Empírico
- **Amostra:** Defects4J
- **Resultado principal:** detecção de bugs muito limitada (vários modelos acharam poucos/nenhum bug) e precisão baixa dos testes gerados.
- **Lacuna:** sustenta a necessidade de **suíte independente + QA humano** no experimento.

---

## Grupo D — Qualidade de software

### D01 — Qualidade de código gerado por diferentes engines
- **Autores:** Davide Tosi
- **Ano:** 2024
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Modelos:** 3 engines de IA
- **Amostra:** 3 problemas complexos de programação
- **Método:** suítes de testes humanas + métricas de qualidade + análise de código
- **Testes independentes?** Sim
- **Resultado principal:** engines resolveram os problemas, mas com necessidade de supervisão de especialistas para código executável e de boa qualidade.
- **Lacuna:** metodologia parecida com a nossa para a parte experimental; avançar para múltiplos agentes/sistema completo.

### D02 — Qualidade LLM vs. humano (SonarQube)
- **Autores:** Molison et al.
- **Ano:** 2025
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Método:** SonarQube + diferentes configurações/estratégias de geração
- **Resultado principal:** em algumas situações a IA teve menos bugs e menor esforço estimado de correção; problemas estruturais aparecem em tarefas mais complexas.
- **Lacuna:** exige neutralidade: resultado pode ser melhor, igual ou pior conforme a situação.

### D03 — Experimento controlado do GitHub (Copilot)
- **Autores:** a confirmar
- **Ano:** a confirmar
- **DOI:** a confirmar
- **Tipo:** Experimento controlado (202 desenvolvedores de 243 recrutados)
- **Modelos/Ferramenta:** GitHub Copilot
- **Tarefa:** endpoints de aplicação web
- **Resultado principal:** grupo com IA teve maior probabilidade de passar todos os testes e melhor avaliação em funcionalidade, legibilidade, confiabilidade, manutenção e concisão.
- **Lacuna:** evidência favorável à IA → nossa pesquisa deve permitir confirmação ou refutação pelos dados.

### D04 — QA de código gerado por LLM (aspectos não funcionais)
- **Autores:** Sun, Ståhl, Sandahl, Kessler
- **Ano:** 2026
- **Publicação:** Journal of Systems and Software
- **DOI:** a confirmar
- **Tipo:** Misto (109 artigos + workshops + experimento com 3 LLMs)
- **Modelos:** 3 LLMs
- **Referencial:** ISO/IEC 25010
- **Resultado principal:** literatura concentra-se em correção funcional; segurança, manutenção e performance menos exploradas; profissionais destacam manutenção, legibilidade e dívida técnica.
- **Lacuna:** **adotar ISO/IEC 25010 como referência de qualidade não funcional** no nosso experimento.

---

## Grupo E — Segurança

### E01 — Vulnerabilidades em snippets gerados por IA (GitHub, grande escala)
- **Autores:** Fu et al.
- **Ano:** 2025
- **Publicação:** ACM Transactions on Software Engineering and Methodology
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Ferramentas:** GitHub Copilot, CodeWhisperer, Codeium
- **Amostra:** 733 snippets de projetos reais do GitHub
- **Resultado principal:** vulnerabilidades em 29,5% dos snippets Python e 24,2% dos JavaScript; 43 categorias CWE.
- **Lacuna:** baseline de segurança para our check-list (OWASP/CWE) no oráculo.

### E02 — Segurança em 7 LLMs
- **Autores:** Morkonda et al.
- **Ano:** 2026
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Modelos:** 7 LLMs
- **Resultado principal:** todos os modelos produziram código com vulnerabilidades, muitas de severidade alta ou crítica.
- **Lacuna:** medir severidade da segurança no nosso experimento.

### E03 — Segurança + prompting
- **Autores:** Aldosari, Aldawsari
- **Ano:** 2026
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico (multi-modelo)
- **Modelos:** 5 LLMs
- **Resultado principal:** prompting orientado à segurança modificou a distribuição das vulnerabilidades, mas não reduziu significativamente a frequência/densidade geral.
- **Lacuna:** variável experimental "estratégia de prompt" não elimina vulnerabilidades.

---

## Grupo F — Agentes de programação (AI coding agents)

### F01 — Refatoração agêntica (estudo empírico de agentes)
- **Autores:** Horikawa et al.
- **Ano:** 2025
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Agentes:** OpenAI Codex, Claude Code, Cursor
- **Amostra:** 15.451 atividades de refatoração · 12.256 PRs · 14.988 commits · projetos Java open source
- **Resultado principal:** agentes fazem alterações locais/de consistência; humanos, mudanças de design mais amplas.
- **Lacuna:** **modelo ≠ agente de programação** — nosso estudo deve diferenciar essas categorias no desenho.

### F02 — Código gerado por IA não é reproduzível (ainda)
- **Autores:** a confirmar
- **Ano:** a confirmar
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico
- **Agentes:** Claude Code, OpenAI Codex, Gemini
- **Amostra:** 300 projetos gerados a partir de 100 prompts padronizados (Python, JavaScript, Java)
- **Resultado principal:** apenas 68,3% executaram imediatamente em ambiente limpo; em Java, 44%; expansão média de 13,5× entre dependências declaradas e necessárias.
- **Lacuna:** executabilidade/reprodutibilidade como dimensão de qualidade — relevante para nosso oráculo.

### F03 — Vulnerabilidades introduzidas em interações reais
- **Autores:** a confirmar
- **Ano:** 2026
- **DOI:** a confirmar
- **Tipo:** Estudo Empírico (interações reais de desenvolvedores)
- **Modelos:** GPT-4o (entre outros)
- **Resultado principal:** em um experimento o GPT-4o introduziu 22 vulnerabilidades contra 10 presentes nos prompts originais; em outro, distribuição mais equilibrada.
- **Lacuna:** separar **erro pré-existente no requisito/prompt** de **erro introduzido pela IA** — controle metodológico importante.

---

## Resumo por temas (contagem)

| Grupo | Tema | Qtd. |
|---|---|---|
| A | LLMs em ES | 2 |
| B | Defeitos | 4 |
| C | Testes | 4 |
| D | Qualidade | 4 |
| E | Segurança | 3 |
| F | Agentes | 3 |
| **Total** | | **19** |

**Meta da próxima rodada:** +6–11 artigos (prioridade: estudos que avaliem **sistemas completos**, agentes de programação 2025/2026 e QA não funcional).