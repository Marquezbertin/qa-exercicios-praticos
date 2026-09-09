# Plano de Expansão — Fase 2 (amostra e credibilidade)

> **Origem:** plano de expansão de amostra recebido em 2026-09-09, consolidado
> neste repo com verificação independente dos cálculos (script
> `../sbes-2027/artefatos/calcular_cis.py` — todos os ICs reproduzidos com
> diferença máxima de 0,001 por arredondamento).
> **Documentos irmãos:** `reclassificacao-rq3.md` (codebook agrupado),
> `pre-registro-osf-draft.md` (draft do pré-registro),
> `auditoria-oraculo-checklist.md` (template de auditoria).

## 1. Diagnóstico: custos de amostra por RQ

As RQs têm custos de amostra radicalmente diferentes; isso guia o investimento.

### RQ1 (bootabilidade, tabela agente × boot/não-boot)

| Execuções/agente | N total | Menor célula esperada | χ² válido? |
|---|---|---|---|
| 3 (atual) | 12 | 0,75 | Não |
| 8 | 32 | 2,00 | Não |
| 10 | 40 | 2,50 | Não |
| 20 | 80 | 5,00 | Sim, no limite |

Com boot de 25%, o χ² formal exigiria ~20 execuções/agente (80 total) —
inatingível no curto prazo sem orçamento. Caminho realista: **estreitar o IC**
em vez de perseguir significância.

| N total | IC 95% Wilson | Largura |
|---|---|---|
| 12 (atual) | [0,089 – 0,532] | 0,443 |
| 32 (8/agente) | [0,133 – 0,421] | 0,289 (−35%) |
| 40 (10/agente) | [0,142 – 0,402] | 0,260 |
| 80 (20/agente) | [0,168 – 0,355] | 0,187 |

### RQ3 (categorias Tambon) — a mais cara

| Estrutura | Células | Defeitos necessários | Execuções estimadas |
|---|---|---|---|
| 6 categorias × 4 agentes (atual) | 24 | ~120 | ~120 (~30/agente) |
| 3 macro-grupos × 4 agentes (proposta) | 12 | ~60 | ~60 (~15/agente) |

Sem agrupar, RQ3 nunca sai do "informativo, não conclusivo". Ver codebook
agrupado em `reclassificacao-rq3.md` (G1 estrutural, G2 lógica/entrada,
G3 alucinação/atributo) — tabela agrupada dos 12 defeitos atuais: G1=5,
G2=4, G3=3.

### RQ6 (testabilidade) — mais forte e mais barata

Efeito quase determinístico (0 de N); cada execução adicional estreita o IC
rapidamente.

| N avaliado | IC 95% Wilson | Largura |
|---|---|---|
| 12 (atual) | [0,000 – 0,242] | 0,242 |
| 20 | [0,000 – 0,161] | 0,161 |
| 40 | [0,000 – 0,088] | 0,088 |
| 80 | [0,000 – 0,046] | 0,046 |

## 2. Prioridades de investimento

1. **Réplicas 8–10/agente (32–40 total).** Melhor retorno: IC de RQ1 cai ~40%
   de largura; RQ6 robustece; RQ8 ganha dados reais. Custo: zero (tempo +
   rate limits). ~15–25h distribuídas.
2. **RQ3 com 3 grupos.** Correção estrutural (ver `reclassificacao-rq3.md`).
   Custo zero; definir o codebook **antes** de nova coleta.
3. **2–3 modelos free adicionais** (mesmo framework, 8–10 execs cada),
   priorizando diversidade de proveniência (Qwen, DeepSeek, GLM, outros
   "-free").
4. **Auditoria de cobertura do oráculo** antes da nova leva; versionar a
   suíte (v1.1 só para entregas novas), sem misturar comparações.
5. **Docker** sobre o conjunto completo (antigo + novo) — validade interna.

## 3. Sequência (ordem não intercambiável)

1. Fechar definições de design (codebook RQ3, auditoria do oráculo, N-alvo,
   critério de parada, lista de modelos).
2. Publicar o pré-registro formal no OSF (`pre-registro-osf-draft.md`).
3. Coletar réplicas + novos modelos exatamente como pré-registrado.
4. Docker sobre tudo; pacote de replicação no Zenodo (nova versão, linkada
   ao OSF); atualizar preprint com novos números e ICs.

## 4. Critério de parada (declarar no pré-registro)

Parar ao atingir 10 execuções/agente, **ou** antes se RQ1/RQ6/RQ7/RQ8
atingirem IC de Wilson com largura ≤ 0,30 — o que ocorrer primeiro. Sem
coleta adicional em busca de significância após a parada.

## 5. Checklist

| Ação | Antes de nova coleta? |
|---|---|
| Codebook de 3 grupos para RQ3 | Sim — obrigatório |
| Auditoria de cobertura do oráculo | Sim — obrigatório |
| N-alvo e critério de parada | Sim — obrigatório |
| Pré-registro formal no OSF | Sim — antes de tudo |
| 2–3 modelos free adicionais (lista fechada) | Sim (parte do pré-registro) |
| Coleta 8–10 execuções/agente | É a coleta em si |
| Docker (antigas + novas) | Depois da coleta |
| Reclassificar defeitos no novo codebook | Junto com a coleta |
| Zenodo (nova versão do pacote) | No final |
| Preprint com novos números e ICs | No final |

## Resumo

O maior ganho por hora investida: (a) pré-registrar antes de coletar,
(b) ir de 3 para 8–10 execuções/agente, (c) agrupar RQ3 em 3 grupos.
