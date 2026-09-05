# Banco ABC - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - Credenciais demo não funcionam como documentado (Severidade: Alta)
- **Onde:** Campo de senha tem `maxlength="8"`, mas a senha demo documentada é `qatest123` (9 caracteres).
- **Esperado:** A senha demo deve funcionar conforme documentado na tela de login.
- **Obtido:** O usuário só consegue digitar 8 caracteres; a senha documentada é impossível de informar.
- **Como testar:** CT-03.

### BUG 2 - Login aceita QUALQUER senha de 8 caracteres (Severidade: Alta - Segurança)
- **Onde:** `entrar()` valida apenas `senha.length === 8`; não compara com uma senha armazenada real.
- **Esperado:** Somente a senha correta da conta deve permitir acesso.
- **Obtido:** Qualquer senha com 8 caracteres (ex.: `12345678`) libera acesso mesmo sendo diferente da demo.
- **Como testar:** CT-04 (com `12345678` o acesso é liberado).

### BUG 3 - Depósito/transferência com vírgula perdem os centavos (Severidade: Média)
- **Onde:** `parseFloat()` interpreta `"1000,50"` como `1000`.
- **Esperado:** O sistema (em pt-BR) deve aceitar `1000,50` como R$ 1.000,50.
- **Obtido:** Digitar `1000,50` deposita/transfere R$ 1.000,00 -- os R$ 0,50 são "engolidos" silenciosamente.
- **Como testar:** CT-06 e CT-14.

### BUG 4 - Conta destino não é validada nos formatos aceitos (Severidade: Média)
- **Onde:** Regex `^\d{5}-\d{1}$`.
- **Esperado:** O formato `NNNNN-N` (ex.: 12345-6) é o único aceito, com mensagem clara.
- **Obtido:** *Verifique: o regex aceita apenas dígitos; formatos com letras são rejeitados, mas o hífen é obrigatório. Teste também `12345-60` (6 dígitos após hífen).*
  - **Observação:** o padrão atual aceita `12345-0` a `12345-9`, o que é o esperado. PORÉM a mensagem de "conta não encontrada" só aparece para contas fora da lista. Note que um QA deve confirmar que o formato está restrito de forma consistente com o que aparece no extrato/contas demo.

### BUG 5 - Mensagem do depósito acima do limite vs. valor exato (Severidade: Baixa)
- **Onde:** Condição `valor > 10000`.
- **Esperado:** Depósito de exatamente R$ 10.000,00 é permitido; acima disso é rejeitado. Confirme se a mensagem é clara para o usuário (limite informado).
- **Obtido:** comportamento de borda correto, mas **verifique se a documentação/UX informa o limite antes do erro** (falha de usabilidade).

### Ponto de atenção (não é bug intencional do site, mas de teste)
- A taxa de 2% é corretamente cobrada do remetente. Para valores **acima** de R$ 1.000,00 (CT-15 confirma o caso-limite de R$ 1.000,00 sem taxa).

---

## Boas práticas que este exercício reforça
- Nunca confiar apenas na documentação: testar as credenciais reais informadas na tela.
- Testar formatos de moeda locais (vírgula vs ponto).
- Testar casos-limite (limite máximo de depósito, limite da taxa).
- Conferir se valores com centavos não são perdidos silenciosamente.