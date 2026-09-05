# Vida+ Saúde - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs / pontos de atenção presentes no site

### BUG 1 - Não há regra de antecedência para cancelamento (Severidade: Média)
- **Onde:** `cancelar()` permite cancelar qualquer consulta agendada, inclusive a do próprio dia.
- **Esperado:** A política da clínica (definida no requisito) determina prazo para cancelamento (ex.: 24h antes). Sem isso, o horário pode ser liberado em cima da hora, prejudicando o médico e a clínica.
- **Obtido:** Cancelamento imediato sem nenhum bloqueio/aviso.
- **Como testar:** CT-10.

### BUG 2 - Validação de domingo pode falhar por fuso horário (Severidade: Baixa)
- **Onde:** `diaDaSemana()` usa `new Date(dataStr).getDay()` e o código usa `toISOString()` em `hoje()`.
- **Esperado:** O dia da semana deve ser calculado com o fuso local do usuário.
- **Obtido (potencial):** Em fusos com deslocamento negativo (ex.: UTC-3), uma data como "2026-09-06" pode ser interpretada como sábado local, deixando passar um domingo.
- **Como testar:** CT-12.

### BUG 3 - Ids das consultas são a posição no array (Severidade: Baixa - manutenção)
- **Onde:** `cancelar(i)` recebe o índice; `renderAgenda()` usa `forEach`.
- **Esperado:** Uso de ID estável, independente da ordem (importante quando houver exclusão/inserção em outra parte da tela).
- **Obtido:** Funciona hoje, mas é frágil a mudanças; um QA atento registraria como dívida técnica.

### Observação extra
- Em `renderHorarios()` existe o comentário "alteraçção de agenda" sem lógica correspondente: indício de recurso planejado e não implementado (bom candidato a bug de requisito).

---

## Principais lições deste exercício
- Regras de negócio não implementadas (cancelamento com antecedência) são bugs tão importantes quanto os de código.
- Fuso horário é fonte clássica de bugs de data -- testar com configurações de horário diferentes.
- IDs estáveis em listas evitam exclusão de registros errados.
- COMENTÁRIOS no código devem ser conferidos (recurso prometido vs. implementado).