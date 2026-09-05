# Gabarito - Exercício 05 - Gerenciador de eventos e datas

> Consulte APENAS depois de tentar. Execute `exercicio-05-datas.py` e observe a falha no Teste 10.

## Bugs intencionais

### BUG 1 - Limite de 30 dias incorreto (Severidade: Alta)
- **Onde:** `if dias >= 30` em `status_efetivo()`.
- **Regra:** "Eventos PENDENTES com mais de 30 dias" devem virar VENCIDO, ou seja, **somente acima de 30 dias** (31+).
- **Esperado:** Um evento com exatamente 30 dias de atraso continua PENDENTE.
- **Obtido:** Com 30 dias exatos o status vira VENCIDO -> Teste 10 falha (`data_30_dias` = hoje - 30 dias).
- **Correção:** voltar para `dias > 30`.

### BUG 2 - `listar()` cria um dicionário com chave "data" sobrescrita em duplicatas (Severidade: Média)
- **Onde:** `listar()` usa `{id: {...}}` onde `id` é a variável do loop -- se você renomear a chave de um evento, `listar()` quebraria. (Fragilidade estrutural; observe a variável `id` sombreando o parâmetro.)

### Observação (não-implementação esperada)
- O exercício NÃO implementa "evento VENCIDO armazenado": o VENCIDO é derivado em `status_efetivo()`, conforme a regra 6. Isso é um comportamento correto (nenhuma persistência de status fantasma).

---

## Verificação independente
- `datetime.strptime(data, "%Y-%m-%d")` + `datetime.now()` é usado em todo o fluxo. Confirme que comparações de datas usam o mesmo fuso; caso o servidor esteja em UTC e o usuário em UTC-3, datas "de hoje" podem escorregar 1 dia (bug de fuso potencial).