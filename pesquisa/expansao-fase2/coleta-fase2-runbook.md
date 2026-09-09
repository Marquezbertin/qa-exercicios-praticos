# Runbook de coleta — Fase 2 (8–10 execuções/agente)

> Seguir **exatamente** o que foi pré-registrado no OSF. Qualquer desvio vira
> "desvio pós-registro" no artigo — melhor não ter nenhum.
> **Pré-requisitos obrigatórios antes da execução nº 1:** pré-registro OSF
> publicado; codebook RQ3 v1.0 congelado; auditoria do oráculo concluída
> (versão da suíte definida); lista de modelos fechada; especificação v1.0
> congelada; oráculo imutável.

## 0. Preparação (uma vez)

- [ ] Anotar link + timestamp do pré-registro OSF: `[preencher]`
- [ ] Versão do oráculo para a Fase 2: `[v1.0 / v1.1]`
- [ ] Modelos e IDs exatos no framework `opencode`:
  - [ ] ultra — `nemotron-3-ultra-free` (repetir até 8–10 execuções totais)
  - [ ] lightning — `nemotron-3.5-lightning-free`
  - [ ] ling — `ling-3.0-flash-fin-free`
  - [ ] mimo — `mimo-v2.5-free`
  - [ ] novo 1 — `[ID exato]` · novo 2 — `[ID exato]` · novo 3 — `[ID exato]`
- [ ] Pasta de coleta criada (fora do repo público): `coleta-fase2/<modelo>/e<N>/`
- [ ] Rate limits dos tiers gratuitos verificados; cronograma distribuído.

## 1. Por execução (repetir para cada modelo, e4 → e8/e10)

1. Abrir **sessão nova e limpa** no `opencode` com o model ID exato.
2. Colar o **mesmo prompt da especificação v1.0** (FR1–FR8 + NFR). Nada de
   hints extras, correções ou reformulações no meio do caminho.
3. Aguardar a conclusão (~20–40 min). Não intervir.
4. Capturar e salvar em `coleta-fase2/<modelo>/e<N>/`:
   - `manifest.json` — versões do modelo/agente/dependências;
   - `prompt.txt` — prompt exato enviado;
   - `log.txt` — log completo da sessão;
   - `tests/` — testes gerados pelo próprio agente;
   - código entregue (sistema completo).
5. **Não abrir o oráculo nem corrigir o código** entre execuções (cegamento).
6. Anotar hora de início/fim (vira o dado de "custo de tempo").

## 2. Validação por entrega (ambiente limpo)

1. venv nova (ou container, se o Docker já estiver pronto — senão, nativo
   como na Fase 1 e Docker depois, sobre tudo junto).
2. PostgreSQL + `alembic upgrade head` + uvicorn + gate `/health`.
3. Rodar a suíte oráculo (pytest, versão registrada) → anotar
   testes/falhas/erros/aprovados + bootável (sim/não).
4. Rodar `bandit`, `pip-audit`, `ruff`, `radon` → anotar.
5. Rodar os testes do próprio agente **contra o oráculo** (dado de RQ6).

## 3. Classificação de defeitos (por entrega, após validação)

1. Dois avaliadores, **cego e independente**: categoria Tambon (10 padrões)
   + macro-grupo RQ3 (G1/G2/G3) + severidade + fonte de detecção.
2. Registrar evidência de reprodução por defeito.
3. Divergências → reunião de consenso registrada, com rationale por caso.
4. Excluir da matriz (mas listar à parte): pilotos, achados de
   infraestrutura, NFR/non-bug — mesmo protocolo da Fase 1.

## 4. Controle de progresso e parada

| Modelo | e4 | e5 | e6 | e7 | e8 | e9 | e10 |
|---|---|---|---|---|---|---|---|
| ultra (3 prontas) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| lightning (3) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| ling (3) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| mimo (3) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| novo 1 (0) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| novo 2 (0) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |
| novo 3 (0) | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

**Parar** ao atingir 10 execuções/agente **ou** antes, se RQ1/RQ6/RQ7/RQ8
atingirem IC 95% de Wilson com largura ≤ 0,30 (recalcular com
`../sbes-2027/artefatos/calcular_cis.py` a cada leva). Sem coleta extra
em busca de significância após a parada.

## 5. Regras que não podem ser quebradas

- Especificação e oráculo **não mudam** durante a coleta.
- Mesmo prompt para todos os modelos e execuções.
- Pilotos (se precisar calibrar um modelo novo) são declarados como
  pilotos e **excluídos** da matriz.
- Novos modelos entram com o contador do zero (8–10 execuções próprias),
  não herdam as 3 da Fase 1.
