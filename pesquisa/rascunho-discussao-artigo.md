# Discussão — Rascunho v0.1 (para o artigo)

> **Status:** RASCUNHO v0.2 — subseção 5.2 confirmada para o artigo; referências inseridas.
> **Base:** resultados da Fase 2 (seção 13 da `metodologia-experimental.md`) + laboratório exploratório (`laboratorio-exploratorio/`) como fonte **complementar e não-evidenciária**.
> **Decisão do autor:** a subseção 5.2 **entra na pesquisa** como material complementar de discussão, com a ressalva de não-evidência explicitada.
> Este rascunho segue a orientação de neutralidade (C1): os dados decidem; leitura honesta das limitações.

---

## 5. Discussão (*draft*)

Esta seção interpreta os resultados da seção de resultados do experimento controlado e, em seguida, apresenta uma exploração complementar de comportamento de modelos em tarefas de QA isoladas. **A exploração complementar não constitui evidência do experimento controlado**; ela é apresentada explicitamente como material de apoio à interpretação e à geração de hipóteses para trabalhos futuros.

### 5.1 Interpretação dos achados principais

**Densidade e natureza dos defeitos (RQ1–RQ4; H1, H2).** Os resultados indicam diferenças descritivas de densidade entre agentes (lightning 1,36 defeitos/KLOC; ultra 0,93; mimo 0,92; ling 0,55), com o achado mais sustentável concentrado no perfil do agente ultra: 100% dos defeitos classificados como `incomplete_generation`, um dos padrões da taxonomia de Tambon et al. [B01]. A interpretação em termos de perfil — e não apenas de quantidade — segue a evidência de Cotroneo, Improta e Liguori [B03] de que IA e humanos têm perfis de defeitos diferentes; aplicada aqui à comparação entre agentes. O teste χ² global aponta associação entre agente e categoria (p=0,041, V=0,85), porém **informativo, não conclusivo**, dado o n reduzido e as células esperadas abaixo de 5. Portanto, H1 não é rejeitada nem aceita com esta amostra; H2 encontra apoio pontual (perfil ultra), mas não pode ser generalizada.

**Severidade (RQ4).** Todos os defeitos detectados foram Blocker ou Critical. Essa concentração é esperada e deve ser lida com cautela: 10 das 12 entregas não foram bootáveis, o que inflaciona mecanicamente a severidade (se o deliverable não sobe, o defeito é automaticamente bloquante) e impede medir defeitos funcionais que só apareceriam em execução.

**Detecção pelos próprios agentes (RQ6; H3).** Nenhuma entrega passou 100% do oráculo, e **os testes gerados pelos agentes não detectaram nenhum dos 12 defeitos Tambon (0/12; 0/18 linhas da matriz, incluindo NFR e piloto)**. Na matriz 2×2, nas entregas em que a funcionalidade foi exercitável, o oráculo detectou **4/4** defeitos alcançáveis enquanto os testes do próprio agente detectaram **0** — mesmo quando a suíte do agente pôde rodar contra o oráculo (lightning/e3; mimo/e2, e3). O dado consistente e transversal é que **a aprovação própria não é garantia de conformidade**: o padrão 0-vs-4 (Fisher marginal extremo, reportado como tendência, não significância, dado o n) sustenta H3 em nível descritivo. Isso está em linha com a literatura, que demonstra efetividade limitada dos testes gerados por IA [C04, C03], a perda de confiabilidade de coverage/mutation na presença de bugs [C05] e a omissão sistemática de casos especiais [C06]. A assimetria metodológica (8/12 defeitos sem execução funcional do oráculo por entrega não-bootável) torna a comparação intrinsecamente limitada e deve ser reportada como tal.

**Qualidade funcional ≠ qualidade global (RQ5; H4).** Entregas que sobem ainda falham em 69–80 dos 81 testes (defeitos de autenticação/banco de dados), enquanto entregas que não sobem passam nos NFR estáticos. As dimensões funcional, estrutural e de segurança divergem entre si; um índice único colapsaria informações que devem permanecer separadas (o que sustenta o desenho multidimensional desta pesquisa).

**Padrões reincidentes.** Quatro padrões concentram os defeitos (ocorrências entre as 12 execuções formais, piloto à parte): dependência ausente (4; +1 no piloto), incompatibilidade passlib/bcrypt gerando 500 em `/auth/register` (3; +1 no piloto), misconfig de reprodução do alembic (1; +1 no piloto) e versão fantasma (1). Esses padrões são **transferíveis entre modelos "free"** do mesmo pipeline, sugerindo um "vale comum" de qualidade para geração de sistemas completos em modo agente no momento da coleta — independentemente da família do modelo. Estudos de agentes em tarefas reais já mostram confiabilidade desigual entre ferramentas ([F05], reversões de 0,7% a 7,6%) e reprodutibilidade/executabilidade limitada de projetos gerados ([F02], 68,3% executam imediatamente; 44% em Java); nosso resultado estende esse quadro para o cenário de modelos gratuitos em modo agente, mesmo com especificações controladas.

**Variabilidade entre execuções (RQ8).** A variabilidade funcional mensurável é limitada (apenas 3 entregas bootáveis); onde foi possível medir (mimo), a taxa de aprovação foi estável nas duas execuções (0,15). Para ultra e ling, a ausência de sinal funcional torna a variabilidade apenas qualitativa.

### 5.2 Estudo complementar de laboratório (não-evidenciário) — DECISÃO: INCLUIR NO ARTIGO

Em paralelo ao experimento controlado, foram realizados experimentos exploratórios com **chat-LLMs** em tarefas isoladas de QA sobre uma mesma função (`create_order`, com um gabarito calibrado de 6 defeitos — ver EXP-001/EXP-002). Estes experimentos **usam modelos distintos dos do experimento controlado e outra unidade de análise (função isolada, não sistema completo)**, e por isso **não constituem evidência do experimento controlado**. Sua função na discussão é enriquecer a interpretação e subsidiar trabalhos futuros. **Ressalva metodológica: na subseção 5.2 comparam-se modelos e tarefas distintos do experimento formal; qualquer convergência entre os achados é apenas indício, nunca evidência cruzada.**

**Detecção de defeitos (EXP-001).** Nesta tarefa isolada, dois modelos identificaram 6/6 defeitos do gabarito e um identificou 5/6, faltando a validação de que a quantidade deveria ser inteira (defeito D1, de tipo/domínio) — padrão que ecoa a categoria `wrong input type` da taxonomia de Tambon et al. [B01] e a omissão de casos especiais relatada por [C06]. Fronteiras explícitas (`>` vs `>=` em cupom e frete: D4, D6) foram detectadas por todos.

**Geração de casos de teste (EXP-002).** A tarefa de *projetar testes* produziu cobertura inferior à tarefa de *detectar*: 5/6, 4/6 e 4/6 dos defeitos claramente cobertos. O caso mais informativo foi D1: um modelo que **não criou teste** para quantidade fracionária positiva no EXP-002, ainda que tivesse **identificado** o mesmo defeito no EXP-001. Somente um modelo criou um teste explícito com `quantity=2.5`. Isso ilustra, em escala isolada, a mesma separação subjacente à RQ6/H3 do experimento controlado: **reconhecer uma condição defeituosa e traduzi-la em um teste capaz de revelá-la são capacidades distintas** — coerente com a baixa detecção de defeitos observada em testes gerados por LLMs ([C04]: 29–60% em Defects4J) e com a presença de test smells mesmo em testes válidos [C03].

**Hipótese exploratória cruzada (à testar — não é evidência).** O alinhamento observado nos experimentos isolados — dificuldade com validação de **tipo/domínio** e, em menor grau, com **fronteiras de igualdade** — guarda semelhança qualitativa com defeitos do experimento controlado que envolvem interface de dados e condições de limite (ex.: `wrong input type` do ling; concentração de `incomplete generation` do ultra). Isso sugere, como **hipótese complementar**, que pontos cegos de validação de tipo/domínio e de condições de fronteira possam ser comuns entre tarefas de *geração de sistema* e tarefas de *validação* pelos próprios modelos. Dada a diversidade de modelos e tarefas entre os dois estudos, esta hipótese **não é afirmada**: apresenta-se apenas como direção para trabalho futuro (protocolos EXP-003 e EXP-bridge pré-registrados para teste, sem contaminação com o experimento formal).

Observação qualitativa adicional: os três modelos do laboratório **desviaram parcialmente** da tarefa de projetar testes, analisando bugs antes de produzir testes — comportamento produtivo na prática profissional, mas que representa desvio instrucional e merece estudo dedicado.

### 5.3 Leitura honesta — limitações centrais

1. **Poder estatístico restrito**: n=12, células esperadas <5 no χ²; H1/H2 sustentam tendências, não conclusões.
2. **Pequena fração funcionalmente avaliável**: 3/12 bootáveis; a dimensão funcional (oráculo) observou apenas essas entregas; defeitos latentes em entregas não-bootáveis não puderam ser medidos.
3. **Condicionante de ambiente**: validação *native* (sem Docker); entregas configuradas apenas para contêiner foram classificadas como defeito de portabilidade — cuida-se para não confundir "defeito" com "suposição de ambiente".
4. **Classificação manual**: κ categoria moderado (0,54) — as 6 divergências foram resolvidas e registradas, mas a taxonomia sobre defeitos de integração permanece ambígua.
5. **Laboratório não-evidenciário**: modelos e unidades diferentes do experimento formal; nº de execuções mínimo por condição; sem execução automatizada dos casos projetados.
6. **Free-tier**: uma execução degenerada e uma validação perdida por disco cheio foram **excluídos** da análise (infraestrutura, não defeito).

### 5.4 Síntese

No cenário controlado desta pesquisa, agentes de modelos "free" em modo agente produziram sistemas completos com baixa taxa de execução (3/12), defeitos concentrados em poucos padrões reincidentes e nenhuma conformidade plena com o oráculo. A evidência mais sustentável é o **perfil de geração incompleta do ultra**; a mais geral é a existência de um **vale comum de qualidade** entre modelos gratuitos do mesmo pipeline. O laboratório exploratório complementar, embora não-evidenciário, reforça — em escala isolada — a separação entre *detectar* e *testar*, alinhada à RQ6/H3. Os resultados não sustentam nem a afirmação "IA não funciona" nem a de "IA substitui QA"; sustentam que, **sob requisitos controlados e com oráculo independente, a qualidade entregue por esses agentes no momento da coleta ficou abaixo do mínimo funcional em 9 de 12 execuções**, e que a aprovação pelos próprios agentes não é substituta da validação independente.

---

## Referências citadas (nesta discussão)

- [B01] TAMBON, F.; DAKHEL, A. M.; NIKANJAM, A.; KHOMH, F.; DESMARAIS, M. C.; ANTONIOL, G. *Bugs in Large Language Models Generated Code: An Empirical Study*. Empirical Software Engineering, v. 30, art. 65, 2025. DOI: `10.1007/s10664-025-10614-4`.
- [B03] COTRONEO, D.; IMPROTA, C.; LIGUORI, P. *Human-Written vs. AI-Generated Code: A Large-Scale Study of Defects, Vulnerabilities, and Complexity*. IEEE ISSRE 2025, pp. 252–263. DOI: `10.1109/ISSRE66568.2025.00035`.
- [C03] ALVES, V. A.; SANTOS, C.; BEZERRA, C. I. M.; MACHADO, I. *Detecting Test Smells in Python Test Code Generated by LLM: An Empirical Study with GitHub Copilot*. SBES 2024, CBSoft. DOI: `10.5753/sbes.2024.3561`.
- [C04] YANG, L.; YANG, C.; GAO, S.; WANG, W. et al. *On the Evaluation of Large Language Models in Unit Test Generation*. ASE 2024. DOI: `10.1145/3691620.3695529`.
- [C05] ZHAO, J.; ZHOU, S.; COHEN, E. *Do Coverage and Mutation Scores of LLM-Generated Test Suites Correlate with Their Effectiveness? (Replicability Study)*. ISSTA 2026. DOI: `10.1145/3832093`.
- [C06] WALCZAK, J.; TOMALAK, P.; LASKOWSKI, A. *Impact of code context and prompting strategies on automated unit test generation with modern general-purpose large language models*. Journal of Systems and Software, v. 237, art. 112834, 2026. DOI: `10.1016/j.jss.2026.112834`.
- [F02] VANGALA, B. P.; ADIBIFAR, A.; GEHANI, A.; MALIK, T. *AI-Generated Code Is Not Reproducible (Yet): An Empirical Study of Dependency Gaps in LLM-Based Coding Agents*. arXiv:2512.22387, 2025/2026. DOI: `10.48550/arXiv.2512.22387`. Apresentado em RAI 2025 workshop e na executiva da AAAI 2026.
- [F05] OUKHAY, I.; BEGOUG, M.; CHOUCHEN, M.; OUNI, A. *When AI Code Doesn't Stick: An Empirical Study on Reverted Changes Introduced by AI Coding Agents*. In: Proc. of the 23rd Intl. Conference on Mining Software Repositories (MSR 2026), pp. 847–851. ACM, 2026. DOI: `10.1145/3793302.3793587`.

> IDs de referência seguem a codificação da matriz (`matriz-de-artigos.md`) e da revisão bibliográfica (`revisao-bibliografica.md`). DOIs de [F02] e [F05] confirmados via Crossref/DataCite em 2026-09-06.

---

*Rascunho v0.3 — 2026-09-06. Subseção 5.2 confirmada para o artigo; citações P8–P10/taxonomia Tambon inseridas; DOIs de [F02] e [F05] resolvidos.*