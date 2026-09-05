# Contabilidade KM - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bug principal presente no site

### BUG 1 - CPMF (0,38%) cobrada de todo salário bruto (Severidade: Alta - regra de negócio)
- **Onde:** `var cpmf = salario * 0.0038;` e exibição em "CPMF / Contrib."
- **Esperado:** O CPMF foi **extinto em 2007** no Brasil. Salvo requisito específico (imposto sobre transação, DARF, etc.), esse desconto não deveria existir numa folha de pagamento.
- **Obtido:** Todo salário tem 0,38% descontado e o líquido final é menor.
- **Observação QA:** Este é o tipo de bug que só aparece quando o tester **conhece o domínio** ou **verifica contra legislação**. A matemática do site está "certinha"; o erro está na premissa.

## Pontos que NÃO são bugs, mas devem ser verificados (exercício de rigor)

1. **Fronteiras das faixas:** No IRPF, erros de *off-by-one* nos limites (ex.: `<=` vs `<`) muitas vezes produzem **o mesmo resultado** por causa das parcelas dedutíveis ("suavização" marginal). Confirme com valores-limite exatos.
2. **INSS teto:** O site aplica o teto corretamente (máx. sobre R$ 7.786,02).
3. **Arredondamento:** O site usa floats diretamente; valores com muitas casas podem gerar divergência de centavo na conferência manual. Um QA rigoroso reporta como baixa severidade.

## Falsos alvos que um QA experiente NÃO deve reportar como bug
- Cálculo do IR sobre a base (salário - INSS - dependentes): comportamento correto.
- Parcela dedutível aplicada corretamente por faixa.
- Exibição "R$ x,xx" via `toLocaleString('pt-BR')` (correta).

---

## Principais lições deste exercício
- Bug de regra de negócio ≠ bug de código: a matemática pode estar certa e a regra errada.
- Conferir com fontes oficiais da legislação.
- Casos-limite exatos merecem tabela própria de teste.