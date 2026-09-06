# Laboratório Exploratório de Comportamento de Modelos de IA

> **NÃO é evidência da pesquisa formal.** Registro de experimentos exploratórios e controlados sobre o comportamento de modelos de IA (chat) em tarefas isoladas de software/QA. Fins: observação de comportamento, aprendizado, geração de hipóteses, material complementar para a discussão do artigo.

## Relação com a pesquisa principal

A pesquisa formal (`../metodologia-experimental.md`) avalia **sistemas completos gerados por agentes** com oráculo independente. Este laboratório observa **capacidades isoladas de chat-LLMs** (detecção de defeitos, geração de casos de teste). Dimensões complementares inversas:

- Pesquisa formal → **geração**: agentes produzem código → defeitos detectados pelo oráculo.
- Laboratório → **detecção/verificação**: chat-LLMs encontram defeitos e projetam testes a partir de spec + código.

Os dados do laboratório **não** entram na matriz de defeitos nem nas estatísticas da pesquisa formal. Podem alimentar **hipóteses e a discussão** (§ Conclusão dos experimentos), sempre marcados como exploratórios.

> Observação metodológica: os modelos aqui (Oreate, Claude, Gemini) são **diferentes** dos modelos do experimento formal (Nemotron Ultra/Lightning, Ling, Mimo). Comparações cruzadas entre os dois estudos são apenas hipóteses exploratórias.

## Regras do laboratório (aplicadas a todos os experimentos)

- mesmo prompt para todos os modelos;
- exatamente a mesma entrada;
- preservação das respostas originais (sem edição) como dados primários;
- gabarito independente para comparação;
- registro de defeitos encontrados e não encontrados, falsos positivos e qualidade das justificativas;
- observação de como o modelo demonstra um defeito;
- registro de comportamentos inesperados/desvios de tarefa;
- sem conclusões gerais a partir de poucos experimentos.

> Regra central: **observar comportamento, não declarar vencedores de forma geral.**

## Índice de experimentos

| ID | Capacidade avaliada | Status | Resultado principal |
|---|---|---|---|
| EXP-001 | Identificação de defeitos em código a partir de requisitos | Concluído | Oreate 6/6, Claude 6/6, Gemini 5/6 |
| EXP-002 | Geração de casos de teste a partir de requisitos | Concluído | Claude 5/6, Oreate 4/6, Gemini 4/6 (cobertura clara) |
| EXP-003 | Geração de testes orientada à detecção de defeitos | Planejado | — |

## Estrutura desta pasta

| Arquivo | Conteúdo |
|---|---|
| `README.md` | Este índice |
| `EXP-001-deteccao-defeitos.md` | Ficha EXP-001 (detalhamento abaixo) |
| `EXP-002-geracao-casos-de-teste.md` | Ficha EXP-002 |
| `respostas-brutas/` | Respostas originais não editadas dos modelos (dados primários; pendente de arquivamento dos transcripts) |

## A hipótese exploratória cruzada (EXP-001 + EXP-002 → pesquisa formal)

Dois achados do laboratório tocam diretamente nos resultados da Fase 2 da pesquisa formal:

1. **Validação em nível de tipo/domínio é um ponto cego recorrente**: o único defeito perdido no EXP-001 (Gemini, D1 — quantidade fracionária não validada) e a falha em traduzi-lo em teste no EXP-002 (Oreate/Gemini) ecoam o padrão da Fase 2: Ling produziu `wrong_input_type` (driver async/sync) e os `incomplete_generation` do Ultra omitiram validações/dependências exigidas.
2. **Condições de fronteira confundidas (`>` vs `>=`)**: os defeitos D4/D6 (EXP-001/002) são da mesma família dos defeitos de condição observados na Fase 2 — modelos erram limites exclusivos/inclusivos tanto ao gerar quanto ao validar.

Interpretação correta (não conclusiva): a hipótese de que **"validação de tipos/domínio e condições de fronteira são pontos cegos compartilhados entre detecção (chat) e geração (agentes)"** é plausível como observação exploratória, mas usa modelos diferentes em cada estudo e amostra pequena. Não pode ser apresentada como evidência no artigo — apenas como discussão/hipótese para trabalho futuro.

## Próximos passos

1. Arquivar os **transcripts brutos** das respostas (Oreate, Claude, Gemini) em `respostas-brutas/` — sem edição.
2. Preparar o EXP-003 conforme ficha EXP-002 (§19).
3. OPCIONAL (alto valor, fecha o ciclo "geração × detecção"): EXP-bridge rodando o prompt do EXP-001/EXP-002 com os **4 modelos da pesquisa formal** (Nemotron Ultra/Lightning, Ling, Mimo) — correlaciona, na mesma família, quem produz vs quem detecta (eco da RQ6: testes do agente vs oráculo).