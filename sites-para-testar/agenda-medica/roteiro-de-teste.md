# Vida+ Saúde - Roteiro de Testes (Agenda Médica)

**Empresa:** Vida+ Saúde (fictícia)
**Sistema:** Agendamento de consultas
**QA responsável:** __________
**Data:** __________

**Regras divulgadas:** Atendimento Seg a Sáb, 8h às 18h. Horários de 30 em 30 min.

---

## Casos de Teste

### CT-01 - Renderização de médicos por especialidade
| Campo | Valor |
|---|---|
| Passos | Troque entre as especialidades no select |
| Resultado esperado | A lista de médicos muda conforme a especialidade (Clínico tem 2, demais têm 1) |

Status: [ ] Passou [ ] Falhou

### CT-02 - Data no passado
| Campo | Valor |
|---|---|
| Passos | Escolha data de ontem |
| Resultado esperado | Erro "data já passou"; nenhum horário é listado |

Status: [ ] Passou [ ] Falhou

### CT-03 - Data num DOMINGO
| Campo | Valor |
|---|---|
| Passos | Escolha o próximo domingo |
| Resultado esperado | Erro "não atendemos aos domingos" |

Status: [ ] Passou [ ] Falhou

### CT-04 - Agendar consulta válida
| Campo | Valor |
|---|---|
| Passos | Clínico Geral / Dra. Fernanda / data daqui a 5 dias / paciente "José Santos" / horário 09:00 |
| Resultado esperado | Mensagem de sucesso; consulta na tabela com status Agendado |

Status: [ ] Passou [ ] Falhou

### CT-05 - MESMO médico, MESMO dia e horário (conflito)
| Campo | Valor |
|---|---|
| Passos | Após o CT-04, tente agendar de novo com o mesmo médico, data e horário 09:00 |
| Resultado esperado | O horário 09:00 deve aparecer ocupado (cinza) e não ser selecionável |

Status: [ ] Passou [ ] Falhou

### CT-06 - MESMO médico, MESMO dia, horário diferente
| Campo | Valor |
|---|---|
| Passos | Agende com o mesmo médico das 09:30 |
| Resultado esperado | Permitido (apenas 1 consulta por horário do médico) |

Status: [ ] Passou [ ] Falhou

### CT-07 - Paciente sem nome
| Campo | Valor |
|---|---|
| Passos | Deixe o nome vazio e clique em "Agendar consulta" |
| Resultado esperado | Erro "informe o nome do paciente" |

Status: [ ] Passou [ ] Falhou

### CT-08 - Agendar sem selecionar horário
| Campo | Valor |
|---|---|
| Passos | Preencha nome e data, mas não clique em nenhum horário |
| Resultado esperado | Erro "selecione um horário" |

Status: [ ] Passou [ ] Falhou

### CT-09 - Cancelar consulta
| Campo | Valor |
|---|---|
| Passos | Clique em "Cancelar" na consulta do CT-04 e confirme |
| Resultado esperado | Status vira "Cancelado"; o horário 09:00 volta a ficar disponível |

Status: [ ] Passou [ ] Falhou

### CT-10 - Cancelar consulta hoje (no mesmo dia)
| Campo | Valor |
|---|---|
| Pré-condição | Consulte as regras de negócio da clínica |
| Passos | Crie uma consulta para hoje e tente cancelá-la |
| Resultado esperado | **Depende da regra definida.** Se a regra exige cancelamento com antecedência (ex.: 24h), um cancelamento no mesmo dia deve ser bloqueado ou avisado. Verifique o que o sistema faz |

Status: [ ] Passou [ ] Falhou

### CT-11 - Cancelar consulta já cancelada
| Campo | Valor |
|---|---|
| Passos | Clique em "Cancelar" em uma consulta já cancelada |
| Resultado esperado | Aviso "já foi cancelada", sem duplicação de estado |

Status: [ ] Passou [ ] Falhou

### CT-12 - Fuso horário afetando o dia da semana
| Campo | Valor |
|---|---|
| Passos | Use o DevTools para simular um fuso com deslocamento negativo (ex.: UTC-3) e observe a data de um domingo (dica: `new Date("YYYY-MM-DD").getDay()`) |
| Resultado esperado | A validação de domingo deve considerar o dia local do usuário, não o UTC |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Filtro de médicos por especialidade
- [ ] Validação de data passada e domingo
- [ ] Conflito de horário por médico bloqueado
- [ ] Mensagens de erro claras
- [ ] Cancelamento correto e sem duplicidade
- [ ] Regra de cancelamento (antecedência) respeitada

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |