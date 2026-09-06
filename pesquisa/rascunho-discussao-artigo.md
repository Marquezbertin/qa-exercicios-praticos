# Discussão — Rascunho v0.1 (para o artigo)

> **Status:** RASCUNHO de seção, para revisão do autor — não integra ainda o corpo do artigo.
> **Base:** resultados da Fase 2 (seção 13 da `metodologia-experimental.md`) + laboratório exploratório (`laboratorio-exploratorio/`) como fonte **complementar e não-evidenciária**.
> Este rascunho segue a orientação de neutralidade (C1): os dados decidem; leitura honesta das limitações.

---

## 5. Discussão (*draft*)

Esta seção interpreta os resultados da seção de resultados do experimento controlado e, em seguida, apresenta uma exploração complementar de comportamento de modelos em tarefas de QA isoladas. **A exploração complementar não constitui evidência do experimento controlado**; ela é apresentada explicitamente como material de apoio à interpretação e à geração de hipóteses para trabalhos futuros.

### 5.1 Interpretação dos achados principais

**Densidade e natureza dos defeitos (RQ1–RQ4; H1, H2).** Os resultados indicam diferenças descritivas de densidade entre agentes (lightning 1,36 defeitos/KLOC; ultra 0,93; mimo 0,92; ling 0,55), com o achado mais sustentável concentrado no perfil do agente ultra: 100% dos defeitos classificados como `incomplete_generation` (Fisher exato p=0,010). O teste χ² global aponta associação entre agente e categoria (p=0,041, V=0,85), porém **informativo, não conclusivo**, dado o n reduzido e as células esperadas abaixo de 5. Portanto, H1 não é rejeitada nem aceita com esta amostra; H2 encontra apoio pontual (perfil ultra), mas não pode ser generalizada.

**Severidade (RQ4).** Todos os defeitos detectados foram Blocker ou Critical. Essa concentração é esperada e deve ser lida com cautela: 10 das 12 entregas não foram bootáveis, o que inflaciona mecanicamente a severidade (se o deliverable não sobe, o defeito é automaticamente bloquante) e impede medir defeitos funcionais que só apareceriam em execução.

**Detecção pelos próprios agentes (RQ6; H3).** Nenhuma entrega passou 100% do oráculo, e os testes gerados pelos agentes não detectaram a totalidade dos defeitos que o oráculo independente revelou. A impossibilidade de exercitar funcionalidade na maioria das entregas limita a comparação direta testes-próprios vs. oráculo: o dado consistente é que a aprovação própria não é garantia de conformidade (alinhado à literatura P8–P10).

**Qualidade funcional ≠ qualidade global (RQ5; H4).** Entregas que sobem ainda falham em 66–80 dos 81 testes (defeitos de autenticação/banco de dados), enquanto entregas que não sobem passam nos NFR estáticos. As dimensões funcional, estrutural e de segurança divergem entre si; um índice único colapsaria informações que devem permanecer separadas (o que sustenta o desenho multidimensional desta pesquisa).

**Padrões reincidentes.** Quatro padrões concentram os defeitos: dependência ausente (5×), incompatibilidade passlib/bcrypt gerando 500 em `/auth/register` (3–4×), misconfig de reprodução do alembic (2×) e versão fantasma (1×). Esses padrões são **transferíveis entre modelos "free"** do mesmo pipeline, sugerindo um "vale comum" de qualidade para geração de sistemas completos em modo agente no momento da coleta — independentemente da família do modelo.

**Variabilidade entre execuções (RQ8).** A variabilidade funcional mensurável é limitada (apenas 3 entregas bootáveis); onde foi possível medir (mimo), a taxa de aprovação foi estável nas duas execuções (0,15). Para ultra e ling, a ausência de sinal funcional torna a variabilidade apenas qualitativa.

### 5.2 Estudo complementar de laboratório (não-evidenciário)

Em paralelo ao experimento controlado, foram realizados experimentos exploratórios com **chat-LLMs** em tarefas isoladas de QA sobre uma mesma função (`create_order`, com um gabarito calibrado de 6 defeitos — ver EXP-001/EXP-002). Estes experimentos **não usam os mesmos modelos do experimento controlado nem a mesma unidade de análise (sistema completo)**, e por isso não podem ser usados como evidência da mesma pesquisa. Seu papel aqui é enriquecer a interpretação. **Uma ressalva metodológica importante: serão comparados modelos distintos e tarefas distintas; qualquer alinhamento entre os achados é apenas um indício, nunca evidência.**

**Detecção de defeitos (EXP-001).** Nesta tarefa isolada, dois modelos identificaram 6/6 defeitos do gabarito e um identificou 5/6, faltando a validação de que a quantidade deveria ser inteira (defeito D1, de tipo/domínio). Fronteiras explícitas (`>` vs `>=` em cupom e frete: D4, D6) foram detectadas por todos.

**Geração de casos de teste (EXP-002).** A tarefa de *projetar testes* produziu cobertura inferior à tarefa de *detectar*: 5/6, 4/6 e 4/6 dos defeitos claramente cobertos. O caso mais informativo foi D1: um modelo que **não criou teste** para quantidade fracionária positiva no EXP-002, ainda que tivesse **identificado** o mesmo defeito no EXP-001. Somente um modelo criou um teste explícito com `quantity=2.5`. Isso ilustra, em escala isolada, a mesma separação subjacente à RQ6/H3 do experimento controlado: **reconhecer uma condição defeituosa e traduzi-la em um teste capaz de revelá-la são capacidades distintas**.

**Hipótese exploratória cruzada (a testar — não evidência).** O alinhamento observado nos experimentos isolados — dificuldade com validação de **tipo/domínio** e, em menor grau, com **fronteiras de igualdade** — guarda semelhança qualitativa com defeitos do experimento controlado que envolvem interface de dados e condições de limite (ex.: `wrong_input_type` do ling; concentração de `incomplete_generation` do ultra). Isso sugere, como **hipótese complementar**, que pontos cegos de validação de tipo/domínio e de condições de fronteira possam ser comuns entre tarefas de *geração de sistema* e tarefas de *validação* dos próprios modelos. Dada a diversidade de modelos e tarefas entre os dois estudos, esta hipótese **não pode ser afirmada**: apresenta-se apenas como direção para trabalho futuro (protocolos EXP-003 e EXP-bridge foram pré-registrados para teste, sem contaminação com o experimento formal).

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

*Rascunho v0.1 — 2026-09-06. Revisar com orientadores; assinalar lacunas de citação da literatura (P8–P10, taxonomia Tambon) e decidir inclusão final da subseção 5.2 no artigo.*