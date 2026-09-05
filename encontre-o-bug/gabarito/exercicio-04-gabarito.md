# Gabarito - Exercício 04 - Formulário com validação JS

> Consulte APENAS depois de tentar. Abra `exercicio-04-formulario.html` no navegador e teste cada regra.

## Bugs / fragilidades presentes

### BUG 1 - E-mail "a@b.c" é aceito como válido (Severidade: Média)
- **Onde:** `validarEmail()` só exige um "@" e um ponto no domínio.
- **Teste:** digite `a@b.c` -- passa na validação.
- **Esperado:** Validação robusta (TLD mínimo de 2 letras, domínio real).

### BUG 2 - CPF é validado apenas pelo FORMATO, não pelo conteúdo (Severidade: Alta)
- **Onde:** `validarCpf()` usa regex `\d{3}\.\d{3}\.\d{3}-\d{2}`.
- **Teste:** `000.000.000-00` e `111.111.111-11` **passam** na validação (são CPFs matematicamente inválidos).
- **Esperado:** Validação dos dígitos verificadores (veja o arquivo `exercicio-06-cpf.py`).

### BUG 3 - Validação de idade aceita números com casas decimais (Severidade: Baixa)
- **Onde:** `parseInt("25.9", 10)` retorna 25.
- **Teste:** digite "25.9" ou "30.5" -- passa. Idade deve ser inteira.
- **Esperado:** rejeitar valores fracionários.

### BUG 4 - Limpar não reseta o estado corretamente quando há erro de "Cadastrar" pendente (Severidade: Baixa)
- **Onde:** os erros são ocultados, mas o campo "mensagem" geral é limpo apenas na próxima tentativa.

### BONUS - Mensagens de sucesso aparecem mesmo sem validações adicionais (ex.: CPF válido de verdade)
- Após "corrigir" os bugs 1–3, o alerta de sucesso ainda aceita CPF fake e e-mails estranhos: **reforce a validação de dados, não só a de formato.**

---

## Correções sugeridas
- Reutilizar a lógica de dígitos verificadores do CPF (exercício 06).
- Usar regex mais robusta de e-mail e rejeitar domínios de 1 letra.
- Verificar `Number.isInteger(Number(idade))`.