# Metodologia Experimental — Protocolo

**Projeto de pesquisa:** Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial
**Versão:** v0.1 (proposta para validação) · **Data:** 2026-09-05 · **Status:** RASCUNHO DE PROTOCOLO — decisões finais em aberto marcadas como **[DECIDIR]**

> Decisões já tomadas com o autor: **stack = Python + FastAPI + PostgreSQL**. O protocolo segue os princípios do `problema-e-hipoteses.md` (mesmo requisito, mesmo prompt, ≥3 execuções, oráculo independente, ISO/IEC 25010). A lacuna preenchida é a combinação integral G1–G5 (0% na literatura, `mapa-da-literatura.md`).

---

## 1. Posição metodológica

Experimento **controlado, prospectivo e reproduzível** (não retrospectivo como D05/F04/F05). Cada agente recebe a **mesma especificação**, tem a **mesma quantidade de oportunidades**, e o produto é avaliado por um **oráculo independente** que o agente nunca viu.

**Neutralidade (C1):** o experimento não parte de "IA é ruim". As hipóteses H1–H4 são bidirecionais ou direcionadas conforme a evidência (ex.: H2 espera distribuições *diferentes*, não *piores*). Se os dados mostrarem IA igual/melhor em alguma dimensão, isso é resultado — não limitação.

---

## 2. Desenho experimental

| Item | Definição |
|---|---|
| Tipo | Experimento controlado com comparação entre grupos (um grupo por agente) |
| Unidade experimental | Um **sistema completo** (API REST) gerado por um agente a partir da especificação |
| Tratamento | Identidade do agente (variável independente) |
| Repetições | **≥3 execuções independentes por agente** (não-determinismo P6/B04; trata RQ8) |
| Blindagem | Oráculo **escrito por QA independente** e **mantido em repositório privado/fora do alcance dos agentes** (evita data leakage — cf. C06) |
| Ambiente de execução | Contêiner Docker limpo e idêntico para todas as execuções (reprodutibilidade F02) |

### 2.1 Agentes — **D8 (RESOLVIDA 2026-09-05)**

Critérios de seleção (aplicados na escolha):

1. Modo **agente** (loop de tarefas/arquivos/testes — F01/F02), não apenas modelo via chat.
2. Disponibilidade/acessibilidade para o pesquisador (inclui custo).
3. Cobertura de linhagens diferentes (ex.: 1–2 por família) para não concentrar um único provedor.
4. Documentar **versão/modelo exato** usado em cada execução (agentes têm versões; F05 mostrou diferenças entre agentes).

Proposta inicial de 4 agentes **[DECIDIR]**: **Claude Code**, **OpenAI Codex**, **Gemini CLI**, + 1 alternativa (ex.: **Cursor** ou agente open source). N=4 agentes × 3 execuções = **12 sistemas completos gerados e avaliados**. (Ampliar para 5×3 se recurso permitir.)

> **D8 (RESOLVIDA):** na máquina de execução só o **opencode** está disponível (sem CLIs comerciais autenticados). Os 4 tratamentos passam a ser **opencode como shell único de agente** + 4 modelos distintos (mesmo loop de agente, comparando modelos — máxima redução de confundimento de ferramenta):
>
> | Modelo | ID opencode |
> |---|---|
> | Nemotron 3 Ultra (NVIDIA) | `opencode/nemotron-3-ultra-free` |
> | Nemotron 3.5 Lightning (NVIDIA) | `opencode/nemotron-3.5-lightning-free` |
> | Ling 3.0 Flash | `opencode/ling-3.0-flash-fin-free` |
> | Mimo v2.5 | `opencode/mimo-v2.5-free` |
>
> Famílias distintas (2× Nemotron, Ling, Mimo) atendem ao critério de linhagens diferentes. A versão exata de cada modelo é capturada por execução (critério 4). Riscos registrados: (a) perde-se a comparação entre **ferramentas** agentes (mitigado: os modelos comparados expõem o mesmo loop de navegação/edição/teste do opencode); (b) mudanças de naming/rotas dos modelos free exigem congelar os IDs e registrá-los no manifest.

> Nota metodológica: estudos F (F01, F02, F04, F05) são **retrospectivos** e não isolam requisito; nosso desenho prospectivo elimina o confundimento de requisitos diferentes entre grupos (G4).

---

## 3. Especificação controlada (o "mesmo requisito")

O **sistema completo** a ser gerado: **API REST de Gerenciamento de Tarefas** (escopo moderado, realista e testável).

### 3.1 Requisitos funcionais (FR) — resumo da especificação

| ID | Requisito funcional |
|---|---|
| FR1 | Cadastro e login de usuários (senha com hash; tokens JWT) |
| FR2 | CRUD de tarefas (título, descrição, prioridade, status, deadline) |
| FR3 | Regras de permissão: apenas o dono (ou admin) altera/exclui a tarefa |
| FR4 | Filtros e paginação na listagem (por status, prioridade, deadline) |
| FR5 | Validação de entrada: campos obrigatórios, tipos, tamanhos, datas válidas |
| FR6 | Tratamento de erros padronizado (códigos HTTP e mensagens consistentes) |
| FR7 | Persistência em PostgreSQL (schema com migrações) |
| FR8 | Testes automatizados acompanhando a entrega (unitários/integração/API) |

A especificação completável (em documento versionado v1.0, artefato privado) define **casos de aceite** para cada FR, com exemplos concretos de entrada/saída. É o ÚNICO documento entregue aos agentes, em formato idêntico.

### 3.2 Requisitos não funcionais (NFR) — informados aos agentes e avaliados depois

| NFR | Âncora |
|---|---|
| Segurança (autenticação, autorização, injeção SQL, segredos, dependências) | E01–E03 (CWE/OWASP) |
| Manutenibilidade (estrutura, complexidade, code smells, duplicação) | D04 (ISO/IEC 25010), D05 |
| Repro-dutibilidade/executabilidade (sobe em ambiente limpo com instruções) | F02 |
| Performance básica (resposta sob carga leve; sem gargalos evidentes) | D04 |

> Os NFR **não** são detalhados com "solução" — apenas o critério de aceite comportamental, para não induzir o agente (mesmo prompt para todos).

---

## 4. Oráculo independente

Construído e versionado **fora do alcance dos agentes** (repositório privado). Composto por:

| Camada | Conteúdo | Ferramentas propostas |
|---|---|---|
| Funcional | Testes de unit, integração, API e E2E cobrindo FR1–FR8 e casos de aceite (pytest + httpx) | pytest, pytest-cov |
| Negativo | Invalid input, extremos (None/inf/NaN), ausência de dados, permissões, autenticação (cf. C06: corner cases que LLMs omitem) | pytest parametrizado |
| Segurança | Verificação de autenticação/autorização, injeção, dependências vulneráveis | bandit, pip-audit/npm-audit, OWASP ZAP (básico) |
| Estrutura | Complexidade, duplicação, code smells, manutenibilidade | SonarQube/SonarScanner ou Ruff + radon |
| Testabilidade | Testes do próprio agente executados contra o oráculo; taxa de detecção real (C04, C05) | pytest |

**Regras do oráculo:**
- Não é revisado pelo agente e nunca é exposto em prompt;
- Válido quanto a ele mesmo (testes do oráculo passam num sistema de referência implementado à parte — sistema "golden" mínimo, não de IA);
- Cobre **todos os FR/NFR**, incluindo casos de aceite (não apenas caminho feliz);
- Métricas de coverage do oráculo são reportadas, mas **não são vistas como evidência de qualidade** (C05): o que vale é a **detecção real de defeitos**.

---

## 5. Matriz de defeitos

Cada defeito detectado é registrado com:

| Campo | Regra |
|---|---|
| ID | Sequencial |
| Agente + execução | Identificação da origem |
| Local (arquivo/módulo/rota) | Onde ocorre |
| **Categoria** | Taxonomia Tambon (10 padrões, B01) → mapeada por 2 pessoas (dupla classificação) |
| **Severidade** | Blocker / Critical / Major / Minor (harmonizada com CWE p/ segurança) |
| Detectado automaticamente? | Pelo oráculo? Pelos testes do agente? |
| Evidência | Teste que reproduz (do oráculo ou do agente) |

- **Dupla classificação independente** (2 avaliadores) com cálculo de acordo inter-avaliador (κ de Cohen) e resolução de divergências em reunião.
- Densidade de defeitos = defeitos por KLOC do projeto entregue (permite H1).

---

## 6. Métricas e mapas para RQ/H

| RQ/H | Métrica | Instrumento |
|---|---|---|
| RQ1 (funcional) | Taxa de passagem do oráculo (testes passando/total) por execução | pytest |
| RQ2 → H1 (densidade) | Defeitos/KLOC por agente; comparação entre grupos | Matriz de defeitos + estatística |
| RQ3 → H2 (categorias) | Distribuição dos 10 padrões por agente | Matriz de defeitos + χ² |
| RQ4 → (severidade) | Distribuição de severidades; % crítico/blocker | Matriz de defeitos |
| RQ5 → H4 (seg./manut.) | Vulns (CWE) + smells/dívida (ISO 25010) | bandit/pip-audit + SonarQube |
| RQ6 → H3 (testabilidade) | Defeitos que os testes do agente detectam vs oráculo (matriz 2×2) | Execução das suítes |
| RQ7 → (reprodutibilidade) | Executa em Docker limpo? instruções completas? deps corretas (13,5× F02)? | Levantamento por execução |
| RQ8 → (variabilidade) | Variância entre as ≥3 execuções do mesmo agente nas métricas acima | Estatística descritiva |

**Funcionalidade ≠ qualidade global (H4):** cria-se um índice composto reportado separadamente (funcional, segurança, manutenibilidade, reprodutibilidade) — sem colapsar em um único número arbitrário.

---

## 7. Procedimento de coleta (execução)

1. Congelar a **especificação v1.0** e o **oráculo** (privado, imutável durante o experimento).
2. Para cada agente, **criar sessão nova** em ambiente Docker idêntico, com o mesmo prompt = "implemente a especificação no README, entregue um sistema executável com os testes".
3. Executar **≥3 sessões independentes** por agente (novo contêiner, novo contexto, sem feedback entre execuções).
4. Capturar em cada execução: versão exata do agente/modelo, transcrição do prompt (idêntico), log, repositório entregue, testes entregues.
5. Avaliar cada entrega apenas com o **oráculo** e a **matriz de defeitos** (avaliadores cegos quanto ao agente, se possível).
6. Registrar tudo em planilha de evidências (link a commits/artefatos).

> **D9 (RESOLVIDA 2026-09-05, REV 2):** ambiente de validação = **PostgreSQL nativo (serviço Windows)** — a máquina de execução é uma VM **sem virtualização aninhada** (`HypervisorPresent=False`), então Docker Desktop não consegue iniciar o engine. Cada deliverable roda via `uvicorn` contra o Postgres nativo; o oráculo é black-box (não depende do backend). Os artefatos Docker exigidos na entrega (compose, Dockerfile, migrações) continuam obrigatórios e validados estruturalmente (`check_structure`/`check_repro`), e serão executados em containers na máquina de produção do experimento.

> Evitar viés: definir fim do experimento e análise **antes** de ver os resultados (pré-registro em repositório privado — para evitar p-hacking).

---

## 8. Análise estatística

| Análise | Teste proposto | Nota |
|---|---|---|
| H1 (densidade) | Kruskal-Wallis entre agentes + post-hoc (Dunn/Bonferroni) e tamanho de efeito (ε²/Cliff's delta) | n pequeno (3/agente): interpretar com bootstrapping; relatar poder limitado |
| H2 (categorias) | χ² de independência na tabela agente × categoria + resíduos padronizados; Cramér's V | Garantir células esperadas ≥5 (junção de categorias raras) |
| H3 (testabilidade) | Proporção de defeitos detectados (agente vs oráculo); teste exato de Fisher | Matriz de contagem 2×2 por defeito |
| H4 (qualidade global) | Comparação funcional vs não funcional por agente (descritivo + testes por dimensão) | Sem índice único arbitrário |
| RQ8 (variabilidade) | Coeficiente de variação por agente nas métricas | Descritivo |

- Nível de significância α=0,05 com correção para múltiplas comparações.
- Resultados negativos são reportados como resultados (neutralidade C1).

---

## 9. Ameaças à validade e mitigação

| Ameaça | Mitigação |
|---|---|
| Data leakage do oráculo (C06) | Oráculo privado, imutável, não exposto a agentes |
| Não-determinismo (B04) | ≥3 execuções; reportar variância (RQ8) |
| Confundimento entre agentes | Mesmo requisito, mesmo prompt, mesmo ambiente (G4) |
| Agente muda durante o estudo | Congelar versões; registrar exatamente a versão usada |
| Poder estatístico baixo (n=3) | Relatar tamanho de efeito + bootstrapping; possível piloto para calibrar |
| Viés do avaliador | Dupla classificação, κ; avaliadores cegos ao agente; pré-registro |
| Oráculo embutir soluções | Oráculo escrito a partir da especificação e validado contra sistema golden de referência |
| Viés de publicação/self-serving | Pré-registro das hipóteses antes de coletar resultados |
| Escopo da tarefa muito fácil/difícil | Especificação moderada (tarefas CRUD + regras + validação); pilotar com 1 agente antes |

---

## 10. Fases e artefatos

| Fase | Entregável |
|---|---|
| 1. Fechar especificação v1.0 | `spec-tarefas-v1.0` (privado) |
| 2. Construir oráculo + sistema golden | Suíte completa (privado) |
| 3. Piloto (1 modelo opencode, 1 execução) | **CONCLUÍDO** (2026-09-05) — calibração registrada abaixo e no README do repo privado |
| 4. Execução completa (4×3) | 12 entregas + registros |
| 5. Classificação e análise | Matriz de defeitos, estatística |
| 6. Consolidação | Seção de resultados do artigo |

---

## 11. Decisões em aberto **[DECIDIR]**

- ~~Lista final de agentes~~ → **D8 RESOLVIDA** (opencode + 4 modelos, seção 2.1).
- ~~Ambiente de validação~~ → **D9 RESOLVIDA rev2** (PostgreSQL nativo local; Docker indisponível sem virtualização — seção 7).
- Detalhamento final da especificação FR/NFR (documento privado).
- Ferramentas exatas do oráculo (propostas na seção 4; validar licença/custo).
- Quantidade de executores na dupla classificação (2 propostos).
- Pré-registro formal (ex.: lista de hipóteses + datas) em repositório privado.

---

## 12. Piloto (Fase 3) — registro de calibração [2026-09-05]

**Execução:** 1 modelo (`opencode/nemotron-3-ultra-free`) via opencode, 1 execução, prompt único (PROMPT.md) + spec v1.0 como README. Artefatos no repo privado (`execucoes/`, `results/piloto/`).

**Achados de processo:**
1. Modelo free é **lento**: >30 min para implementação parcial (skeleton + parte dos testes). Ajuste: execuções em background via `runner/run_agent.ps1`, snapshot antes de validar, orçamento de tempo por execução registrado.
2. **Validação nativa validada ponta a ponta**: banco PostgreSQL dedicado + venv + `alembic upgrade head` + uvicorn + gating por `/health` + oráculo 81 testes + 4 checagens NFR + manifest por execução.
3. Deliverable **não executável** é tratado sem abortar: oráculo marcado como não executado e NFR ainda é coletado.

**Defeitos reais detectados na entrega piloto (prova de conceito do oráculo):**
| Defeito | Classe (mapa) | Detecção |
|---|---|---|
| `/auth/register` → 500 (passlib 1.7.4 + bcrypt ≥4.x) | incompatibilidade de dependências (funcional/segurança) | oráculo (auth/negativos) | 
| `alembic.ini` sem `script_location` | reprodutibilidade (F02) | now `check_repro` (NFR1) |
| `requirements.txt` sem `pydantic-settings` (importado no app) | executabilidade/requirements incompletos | runner (app não sobe) |

**Ajustes de protocolo incorporados no runner/checks (privado):** oráculo tolerante a app morto; `check_repro` valida `script_location`+`env.py`+`/health` e vira NFR1 real (retornava 0 mesmo com migração quebrada); parser JUnit corrigido (`<testsuite>`); métricas recursivas (`collect_metrics`); uvicorn destacado do processo pai (job em produção).

**Intervenção de calibração (documentada, não faz parte dos dados):** para exercitar o oráculo sobre app que sobe, o snapshot piloto recebeu 2 fixes mínimos (requirements + alembic.ini) → oráculo acusou **15 passed / 18 failed / 48 errors**, confirmando que defeitos funcionais são detectados quando a entrega é executável.

---

## 13. Referências no projeto

- Lacuna e fundamentação: `mapa-da-literatura.md` (P1–P18, C1–C6, G1–G5).
- RQs/hipóteses: `problema-e-hipoteses.md` (v0.2, consolidado).
- Números que sustentam o desenho: `analise-quantitativa.md`.
- Fichas com DOI: `matriz-de-artigos.md`.

---

*Protocolo de trabalho v0.1 — validar com o autor antes de iniciar a Fase 1 (fechamento da especificação).*