# Portal Cliente - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - CPF duplicado é aceito no cadastro (Severidade: Alta)
- **Onde:** `cadastrar()` só verifica duplicidade de **e-mail**; não valida CPF único.
- **Esperado:** Um mesmo CPF não pode gerar duas contas.
- **Obtido:** O mesmo CPF `529.982.247-25` pode criar contas com e-mails diferentes.
- **Como testar:** CT-08.

### BUG 2 - E-mail tratado como *case-sensitive* (Severidade: Média/Alta)
- **Onde:** Comparações diretas de string (`usuario.email === email`, `u.email === email`).
- **Esperado:** `MARIA@email.com` e `maria@email.com` são o mesmo endereço.
- **Obtido:** Login com maiúsculas retorna "usuário não encontrado"; cadastro em maiúsculas cria conta duplicada.
- **Como testar:** CT-11 e CT-12.

### BUG 3 - Código morto/duplicado `validarCpf` (Severidade: Baixa - manutenção)
- **Onde:** Existe `validarCpf()` (só conta 11 dígitos) e `validarCpfCompleto()`. A primeira não é usada.
- **O que observar:** Dois métodos para a mesma regra confundem a manutenção e podem levar o QA a testar o comportamento errado. Este tipo de "code smell" geralmente esconde bugs futuros.

### Observações de teste (não são bugs intencionais, mas devem ser anotadas)
- Não existe "esqueci minha senha" (aplicação demo não implementa a tela).
- Não há limite de tentativas de login (bloqueio por força bruta). Em um QA de segurança, isso seria um ponto de atenção.

---

## Principais lições deste exercício
- Regras de unicidade (CPF, e-mail) devem ser testadas com exclusão/inclusão.
- Campos de identificação (e-mail) devem ser tratados sem distinção de maiúsculas.
- Testar o fluxo completo: cadastrar -> sair -> logar (o mesmo usuário deve entrar).
- Verificar mensagens de erro e sucesso em cada cenário.