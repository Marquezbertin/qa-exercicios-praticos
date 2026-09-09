# RQ3 — Codebook de categorias agrupadas (v1.0, pré-coleta Fase 2)

> **Status:** proposta de codebook para o pré-registro OSF da Fase 2. Deve ser
> congelado **antes** de qualquer coleta nova. A justificativa do agrupamento é
> conceitual (afinidade na taxonomia de Tambon et al. [B01]), não estatística —
> isso é o que o protege contra leitura de conveniência post-hoc.
> **Versão:** v1.0 (2026-09-09) · **Autor:** Bruno Bertin Marquez.

## 1. Motivação

A tabela agente × categoria com 6 categorias observadas (24 células) ou 10
categorias Tambon (40 células) é estatisticamente inatingível com orçamento
solo sem custo: seriam necessários ~120 defeitos (~120 execuções, ~30/agente)
para células esperadas ≥5. O agrupamento em 3 macro-grupos (12 células) corta
a exigência pela metade (~60 defeitos) e preserva a pergunta de pesquisa num
nível mais grosso, porém honesto.

## 2. Mapeamento Tambon (10 padrões) → 3 macro-grupos

| Macro-grupo | Padrões Tambon incluídos | Lógica do agrupamento |
|---|---|---|
| **G1 — Geração incompleta/estrutural** | `incomplete_generation`, `missing corner case` | Falha em produzir estrutura/cobertura completa do solicitado |
| **G2 — Erros de lógica/entrada** | `wrong_input_type`, `silly_mistake`, `misinterpretation`, `prompt-biased code` | Interpretação ou tratamento incorreto de entradas/requisitos |
| **G3 — Alucinação/atributo** | `hallucinated_object`, `wrong_attribute`, `non-prompted consideration`, `syntax error` | Referência a elementos inexistentes ou incorretos no código gerado |

> **Nota de decisão (registrar no pré-registro):** `non-prompted consideration`
> foi alocado em G3 (elemento não solicitado ≈ referência espúria) em vez de G2.
> Se houver dúvida na aplicação, o critério de desempate é: *o defeito refere-se
> a algo que não existe/deveria existir (G3) ou a algo existente tratado de
> forma errada (G2)?* Casos ambíguos seguem o mesmo protocolo de consenso dos
> avaliadores (reunião registrada, κ reportado).

## 3. Reclassificação dos 12 defeitos existentes

Fonte: matriz de defeitos Fase 2 (4 ultra + 4 lightning + 1 ling + 3 mimo).

| # | Agente/Exec | Categoria Tambon original | Macro-grupo |
|---|---|---|---|
| 1–4 | ultra e1/e2/e3 (×4) | `incomplete_generation` | G1 |
| 5 | mimo (×1) | `incomplete_generation` | G1 |
| 6 | lightning (×1) | `silly_mistake` | G2 |
| 7–8 | mimo (×2) | `silly_mistake` | G2 |
| 9 | ling (×1) | `wrong_input_type` | G2 |
| 10 | lightning (×1) | `non-prompted consideration` | G3 |
| 11 | lightning (×1) | `hallucinated_object` | G3 |
| 12 | lightning (×1) | `wrong_attribute` | G3 |

## 4. Tabela agrupada resultante (agente × macro-grupo)

| Agente | G1 (estrutural) | G2 (lógica/entrada) | G3 (alucinação) | Total |
|---|---|---|---|---|
| ultra | 4 | 0 | 0 | 4 |
| lightning | 0 | 1 | 3 | 4 |
| ling | 0 | 1 | 0 | 1 |
| mimo | 1 | 2 | 0 | 3 |
| **Total** | **5** | **4** | **3** | **12** |

Leitura descritiva (não confirmatória): ultra concentra-se em G1; lightning
concentra-se em G3; mimo divide-se entre G1/G2; ling tem 1 caso em G2.
O perfil distintivo de ultra (`incomplete_generation`, Fisher p=0,010 na
análise fina) mantém-se visível no nível agrupado (4/4 em G1).

## 5. Viabilidade estatística (honesta)

- 12 células; regra ≥5/célula → ~60 defeitos (~60 execuções a ~1 defeito/exec).
- Com 8–10 execuções/agente (32–40 novas) + 12 existentes ≈ 44–52 defeitos:
  **ainda abaixo de 60**. Portanto o pré-registro deve declarar a análise
  agrupada como **descritiva por padrão**, promovida a inferencial somente se
  o limiar for atingido — sem esse compromisso prévio, qualquer χ² posterior
  seria lido como busca de significância.
- Regra operacional proposta: aplicar χ² somente se todas as células
  esperadas ≥5 no conjunto final; caso contrário, reportar Fisher exato
  pontual por grupo como sinal informativo (mesmo padrão da Fase 2).
