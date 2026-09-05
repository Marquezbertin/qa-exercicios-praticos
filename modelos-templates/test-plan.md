> 💡 Copie e preencha. Um plano simples de teste (1 página) já diferencia você de um "tester de clique".

# PLANO DE TESTE (Template compacto)

**Projeto:** __________
**Versão testada:** __________
**Autor:** __________ **Data:** __________

## 1. Objetivo
O que será validado e com qual critério de aceite. Ex.: "Validar o fluxo de compra ponta a ponta; critério de saída: 100% dos casos críticos verdes e nenhum bug Blocker aberto."

## 2. Escopo
**Inclui:** (funcionalidades/áreas)
- 

**NÃO inclui (fora de escopo):** (explícito para evitar discussão)
- 

## 3. Riscos e mitigações
| Risco | Mitigação |
|---|---|
| Ambiente de homologação instável | Definir janela de deploy / ambiente reserva |

## 4. Estratégia
- Tipos de teste: [ ] Smoke [ ] Funcional [ ] Regressão [ ] API [ ] Perf [ ] Segurança [ ] Exploratório
- Técnicas: [ ] Equivalência [ ] Valor-limite [ ] Tabela de decisão [ ] Estados [ ] Pairwise
- Manual vs automatizado: ______

## 5. Ambiente
| Item | Valor |
|---|---|
| URLs | |
| Banco | |
| Dados de teste | |

## 6. Calendário
| Fase | Datas |
|---|---|
| Preparação de dados | |
| Execução | |
| Reteste/Regressão | |

## 7. Casos de teste (referência)
- Link/planilha/Jira: `casos-de-teste/` | `modelos-templates/test-case.md`

## 8. Critérios de saída
- Todos os casos críticos executados.
- Nenhum bug nível Blocker/Alto em aberto **para o escopo**.
- Relatório de resultados enviado (veja `modelos-templates/relatorio-teste.md`).

## 9. Assinaturas/Decisões
| Responsável | Aprovação |
|---|---|
| QA | |
| PO/Product | |