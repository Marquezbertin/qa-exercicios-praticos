# Pacote de Validação Crítica (Opcional) — Pesquisador Independente

> **Finalidade:** apoiar uma **reunião de validação crítica** (opcional) do experimento com um professor/pesquisador da área. **Decisão de pesquisa:** o autor conduz o estudo como **pesquisador independente** (ORCID `0009-0005-3546-8302`) e **não depende de orientador formal** para escrever nem publicar. Um professor/pesquisador é bem-vindo como **revisor crítico** e, se houver contribuição efetiva, como **coautor** ou suporte a afiliação/endosso (ex.: arXiv cs.SE).
> **Preparado em:** 2026-09-06. Artefatos após a revisão interna (commit `2befdaa`), versão em inglês (commit `d726c43`) e identidade de autor com ORCID incluída.
> **Material de apoio central:** `dossie-veiculo-publicacao.md` (comparativo de veículos e itens de decisão, §4).

---

## 1. Materiais prontos (o que levar)

| Material | Caminho | Observação de uso |
|---|---|---|
| Manuscrito completo (PT) | `pesquisa/artigo-manuscrito-v0.1.md` | IMRaD completo, pós-revisão interna — documento principal para ler junto |
| Manuscrito completo (EN) | `pesquisa/artigo-manuscrito-en-v0.1.md` | Tradução fiel (v0.1-EN), alvo EMSE/internacional |
| Pré-print pronto (OSF) | `pesquisa/preprint/ROTEIRO-submissao-osf.md` + `preprint-submissao.md` | Decidir com o orientador **quando** depositar (antes/depois da anuência) |
| Dossiê de veículos | `pesquisa/dossie-veiculo-publicacao.md` | Itens de decisão na §4; executar a mesa redonda com base nele |
| Figuras 1–5 | `pesquisa/figuras/fig1.png … fig5.png` (script: `gerar_figuras.py`) | Reproduzíveis a partir dos agregados |
| Resultados e metodologia (públicos) | `pesquisa/metodologia-experimental.md` (§13) | Sintetiza Fase 2 (12 entregas, matriz, estatística) |
| Pré-registro | *repo privado* `qa-experimento-oraculo/pre-registro.md` | Mostrar **sob demanda** (contém âncoras temporais via git); não anexar a material público |
| Oráculo (81 testes) e dados brutos | *repo privado* `qa-experimento-oraculo/oracle/`, `results/` | Artefato de replicação; compartilhar só em contexto de avaliação/parceria |

---

## 2. Resumo executivo (one-pager para a reunião)

**O que é.** Experimento controlado, prospectivo e reproduzível sobre a qualidade e os defeitos de **sistemas completos** gerados por **agentes de IA** (não snippets/funções isoladas).

**Desenho.** 4 modelos "free" (Nemotron Ultra, Nemotron Lightning, Ling, Mimo) executados no **mesmo framework de agente** (`opencode`), **3 execuções independentes** cada → **12 entregas** de uma mesma API REST (Python/FastAPI/PostgreSQL) a partir da **mesma especificação**. Avaliação por **oráculo independente** (81 testes + segurança + estrutura + reprodutibilidade), matriz de defeitos na **taxonomia Tambon**, severidade, **dupla classificação cega** (κ).

**Resultados-chave.**
- **3/12 entregas bootáveis**; nenhuma passou 100% do oráculo (1/81 e 12/81).
- **12 defeitos Tambon, 100% Blocker ou Critical** (8 Blocker / 4 Critical); densidades 1,36 / 0,93 / 0,92 / 0,55 por KLOC.
- Perfil mais sustentável: **ultra** 100% `incomplete_generation` (Fisher p=0,010; χ² p=0,041, V=0,85 — **informativo, não conclusivo**).
- **RQ6/H3 (o achado central):** testes do próprio agente detectaram **0/12** defeitos; o oráculo detectou **4/4** dos alcançáveis → **aprovação própria ≠ validação independente**.
- Padrões **reincidentes e transferíveis entre modelos "free"** ("vale comum" de qualidade): dependência ausente, passlib+bcrypt → 500, misconfig de migração, versão "fantasma".

**Limitações declaradas (leitura honesta).** n=12 com células esperadas <5 (χ² apenas informativo); 3/12 funcionalmente avaliáveis (viés Blocker por não-bootabilidade); validação **nativa sem Docker**; modelos free no momento da coleta; um único sistema-alvo/stack (sem generalização). **Neutralidade (C1):** se os dados mostrassem IA igual ou melhor, seria resultado, não limitação.

**O que pedimos na validação (revisão crítica — opcional).**
1. Validação do desenho experimental e da honestidade das limitações.
2. Voto de apoio na decisão de **veículo, idioma e formato** (tabela na §4).
3. Verificação das **regras de afiliação/autor** do veículo escolhido (importante para submissão) e opinião sobre o **momento do pré-print OSF**.
4. Opinião sobre **ampliar a amostra** antes da submissão ou publicar com n=12.

---

## 3. Roteiro de conversa (reunião de validação crítica — opcional)

1. **5 min — visão geral.** Apresentar o one-pager (§2), sem detalhes estatísticos exaustivos.
2. **10–15 min — desenho e honestidade.** Percorrer §§3 e 5 do manuscrito (desenho, oráculo, limitações). Pedir críticas explícitas ao poder estatístico e à operacionalização da RQ6/H3.
3. **10 min — mesa redonda de decisões** com base no dossiê (§4 abaixo): veículo, idioma, formato, pré-registro.
4. **5 min — ética e autoria.** Possibilidade de parceria (coautoria/afiliação/endosso arXiv) — deixar explícito ANTES de qualquer submissão.
5. **5 min — próximos passos e cronograma** (SBES 2027 ~abr/2027; EMSE rolling; depósito OSF).

> **Dica:** levar também os *commits* relevantes do repositório público (manuscrito, método, figuras) como demonstrativo de reprodutibilidade — é o ponto forte do estudo perante SBES/EMSE.

---

## 4. Itens de decisão para a reunião (espelho do dossiê §4)

| # | Decisão | Opções | Quem decide |
|---|---|---|---|
| 1 | **Veículo principal** | SBES 2027 / EMSE / JSS / SQJ / IST | Orientador + autor |
| 2 | **Ampliar amostra antes de submeter?** | Sim (n=24/36) / Não (n=12) | Orientador (custo/tempo: execução Docker em produção) |
| 3 | **Idioma** | Português (SBES aceita pt/en) / Inglês (periódicos internacionais, EMSE) | Orientador |
| 4 | **Formato do paper** | Longo (EMSE ~20p) / Curto (SBES 10p) | Veículo |
| 5 | **Pré-registro formal** | Já criado no repo privado (recomendado) — oficializar versão final | Autor |

---

## 5. Aspectos éticos e de autoria

- **Pesquisador independente:** escrever e ser autor **não exige** orientador nem doutorado (regras de autoria de revistas/congressos não exigem titulação do primeiro autor; podem exigir vínculo/afiliação de um autor — verificar por veículo). O pre-print OSF não exige afiliação.
- **Anuência institucional:** submeter em veículo *peer-reviewed* pode exigir vinculação/afiliação; se um professor/pesquisador aderir como autor/afiliado, formalizar a contribuição (CRediT) **antes** da submissão.
- **Autoria/coautoria:** deixar explícitas as contribuições de qualquer coautor eventual antes da primeira submissão para evitar discussões posteriores.
- **Pre-registro privado:** contém âncoras de decisão e detalhes do oráculo; compartilhar **sob demanda** no contexto de avaliação/parceria; o pre-print público usa a **versão limpa** (sem bloco interno de trabalho).
- **Oráculo e dados brutos:** não expor em material público; disponibilizar para artefato/replicação apenas em contexto de submissão ou parceria.
- **Identidade acadêmica (ORCID):** usar `0009-0005-3546-8302` nos metadados de submissão/pre-print; recomenda-se completar o perfil com as pós-graduações, afiliação "Pesquisador independente", palavras-chave e, depois, o DOI do pre-print.
- **Neutralidade:** estudo sem patrocínio industrial; declaração de ausência de conflitos na submissão.

---

## 6. Próximos passos (independente de reunião com professor)

1. **Depositar o pré-print no OSF** (executável já, sem depender de orientador) via `ROTEIRO-submissao-osf.md` — metadados com ORCID prontos.
2. Confirmar **veículo e idioma** com base no dossiê (a reunião de validação crítica é opcional; se houver, ajuda a decidir) → ajustar modelo de citações e limites de páginas.
3. Decidir **ampliação da amostra** → atualizar pré-registro (n=24/36, Docker em produção) e refazer figuras.
4. Se houver parceria/coautoria: registrar contribuições (CRediT) e usar eventual endosso para o **arXiv cs.SE** com a versão em inglês.
5. Montar cronograma: SBES 2027 (prazo ~abr/2027) e/ou EMSE (rolling).

---

*Pacote v0.2 — 2026-09-06. Reframing: pesquisador independente; validação crítica opcional. Consolida manuscrito (PT/EN), dossiê de veículos, pré-print OSF e itens de decisão; não substitui a decisão de veículo nem a consulta às regras do periódico/evento.*