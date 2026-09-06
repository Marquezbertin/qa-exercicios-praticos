# EXP-003 — Geração de testes orientada à detecção de defeitos

**Status:** PLANEJADO (pré-registro de protocolo — ainda não executado)
**Natureza:** Experimento exploratório
**Data do planejamento:** 2026-09-06

> Pertence ao laboratório exploratório (`README.md`). **Não** constitui evidência do experimento formal da pesquisa principal. Este arquivo é o **pré-registro**: o desenho e os critérios são fixados ANTES da coleta, para evitar ajuste de protocolo em função dos resultados.

---

## 1. Motivação e justificativa (ancorada em EXP-001/EXP-002)

Os experimentos anteriores do laboratório observaram:

- **EXP-001** (detecção de defeitos): modelos receberam spec + código e foram instruídos a identificar defeitos. Resultado: Oreate 6/6, Claude 6/6, Gemini 5/6 (D1 perdido pelo Gemini).
- **EXP-002** (projeto de casos de teste): modelos receberam a **mesma** spec + código e foram instruídos a **projetar testes**. Resultado: Claude 5/6, Oreate 4/6, Gemini 4/6.

A observação mais relevante entre os dois: **D1** (quantidade deve ser inteira) foi **reconhecido** pelo Oreate no EXP-001, mas **não foi traduzido em teste** pelo Oreate no EXP-002. Claude traduziu (B4, `quantity=2.5`). Isso sugere que "reconhecer um defeito" e "projetar um teste que o revele" são capacidades **distintas e não necessariamente correlacionadas**.

O EXP-003 investiga se essa capacidade muda quando **a existência de defeitos não é revelada** e quando **técnicas explícitas de QA são fornecidas**.

## 2. Pergunta exploratória

> Quando os modelos recebem apenas requisitos (sem o código defeituoso e sem a informação de que existem defeitos), eles conseguem gerar testes capazes de revelar categorias de falhas?

Questões derivadas:

> Q1. Existe diferença entre testes gerados espontaneamente e testes gerados com técnicas explícitas (fronteira/negativos/particionamento)?
>
> Q2. A revelação prévia de defeitos (EXP-002) melhora a tradução requisito→teste em relação à não revelação (EXP-003)?

## 3. Desenho proposto (pré-registro)

| Item | Definição |
|---|---|
| Unidade | Uma estratégia de casos de teste para `create_order` (mesma função de EXP-001/EXP-002, **sem o código**) |
| Tratamentos (condições) | C1: espontâneo (sem técnica); C2: requisito por requisito; C3: técnicas explícitas de QA (BVA, particionamento, negativos); C4: após análise de risco |
| Modelos | Mesmos 3 do laboratório: Oreate, Claude, Gemini |
| Entrada | Apenas os requisitos R1–R8 (documento `especificacao EXP-003`), **sem código e sem menção a defeitos** |
| Gabarito | Mesmo gabarito de 6 defeitos (D1–D6) do EXP-002; cobertura por critério já definido (entradas + expectativa que revelem o defeito) |
| Bloqueio de contaminação | Ponto CRÍTICO: o EXP-003 não pode ser executado por modelos/instâncias que já viram o código defeituoso. A coleta deve ocorrer em conversa/sessão nova, sem histórico |

### Critérios de avaliação (pré-fixados)

Os mesmos do EXP-002, para permitir comparação direta:

1. Cobertura dos 6 defeitos (D1–D6);
2. Cobertura de requisitos (R1–R8);
3. Cobertura de fronteiras;
4. Cobertura de entradas inválidas;
5. Cobertura de efeitos colaterais (atomicidade de estoque — D2);
6. Executabilidade dos casos (sem campo `price` fictício em desacordo com a assinatura);
7. Especificidade dos dados;
8. Redundância (economia de casos vs cobertura);
9. Identificação de ambiguidades de requisito;
10. Desvio da tarefa (análise de defeitos antes dos testes, mesmo sem código);
11. Capacidade de transformar requisito em teste verificável (foco em D1);
12. Qualidade das expectativas/resultados esperados.

## 4. Hipóteses exploratórias (pré-registradas)

- **HE-1**: a revelação prévia de defeitos (EXP-002) NÃO altera substancialmente a cobertura de `create_order` — i.e., a capacidade de transformar requisito em teste é relativamente estável entre EXP-002 e EXP-003 (mesmo modelo).
- **HE-2**: técnicas explícitas (C3) aumentam a cobertura de D1 (tipo/domínio) em relação a C1 (espontâneo), especialmente nos modelos que o perderam (Oreate, Gemini).
- **HE-3**: a ausência do código reduz o desvio de tarefa, pois não há "bugs" visíveis para analisar; espera-se menos pré-análise de defeitos que no EXP-002.

> Nenhuma dessas hipóteses, confirmada ou não, será apresentada como evidência da pesquisa formal. São direções para o laboratório.

## 5. Protocolo de coleta

1. Preparar o documento **único de entrada** ("especificação EXP-003"): somente requisitos R1–R8, sem código, sem exemplos de defeito, com o texto pedindo apenas a estratégia de testes (mesmo prompt base do EXP-002, **removida** a seção "Código").
2. Para **cada modelo × cada condição (C1–C4)**: sessão/conversa nova. Recomendação técnica: usar uma conversa separada ou limpar o contexto; registrar o ID/hora da coleta.
3. Coletar o transcript bruto e arquivar em `respostas-brutas/EXP-003_<condicao>_<modelo>.txt`.
4. Avaliar com o gabarito D1–D6 + os 12 critérios da seção 3, em camada de análise separada.
5. Consolidar comparação: EXP-002 vs EXP-003 (para HE-1) e entre condições (para HE-2/HE-3).

## 6. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| Contaminação entre tratamentos (modelo "lembra" do conteúdo da mensagem anterior) | Sessão nova por execução; registrar na ficha o identificador da conversa/hora; se houver indício de memória de contexto, descartar e refazer |
| Amostra pequena (1 resposta por modelo×condição) | Manter como exploratório; relatar somente descritivamente; não generalizar |
| Ambiguidade de precificação da função reaparece nos testes | Critério 6 pré-fixado: casos que exigem `price` fora da assinatura são registrados como "conceitualmente adequados porém não executáveis" (mesmo tratamento do D3 no EXP-002) |
| Falta de tempo/disponibilidade dos modelos | Planejar 12 coletas (3 modelos × 4 condições) em sequência; registrar duração por coleta |

## 7. Resultados esperados (antes da execução — o que cada desfecho permitiria)

- Se **HE-1** confirmada (cobertura semelhante sem o código): reforça que o gargalo é **tradução requisito→teste**, não análise de código — consistente com o achado central do EXP-002.
- Se **HE-2** confirmada: técnicas explícitas de QA compensam a lacuna de D1 (tipo/domínio) — direção útil para promptarção de agentes de teste.
- Se **HE-3** confirmada (menos desvio sem código): o desvio do EXP-002 era reativo ao código defeituoso visível, não uma tendência intrínseca.

## 8. Delimitação (o que NÃO é)

- Não é estudo da eficácia de nenhum framework de teste.
- Não compara qualidade global dos modelos para QA.
- Não alimenta a matriz de defeitos da pesquisa formal.
- Avalia apenas a **tradução requisito → teste** em uma função específica, com um gabarito fixo e 6 defeitos conhecidos.

## 9. Rastreabilidade com o laboratório

| Artefato | Relação |
|---|---|
| `EXP-001-deteccao-defeitos.md` | Provê o gabarito D1–D6 e a detecção (reconhecimento) |
| `EXP-002-geracao-casos-de-teste.md` | Provê a tradução com código presente (baseline de HE-1) |
| `EXP-003-geracao-testes-sem-codigo.md` | Este pré-registro |
| `respostas-brutas/` | Evidência primária (transcripts) |

---
*Pré-registro v0.1 — 2026-09-06. Executar somente após aprovação deste desenho e, preferencialmente, após o EXP-bridge (protocolo separado) para evitar contaminação de contexto com os 4 modelos da pesquisa formal.*