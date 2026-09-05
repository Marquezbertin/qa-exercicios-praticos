# Hotel Reserva Fácil - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - Estadia de "0 noites" é permitida (Severidade: Alta)
- **Onde:** `validarPeriodo()` usa `fim < ini` em vez de `fim <= ini`.
- **Esperado:** Check-out DEVE ser estritamente posterior ao check-in (estadia mínima de 1 noite).
- **Obtido:** Check-in igual ao check-out é aceito; a busca mostra "0 noite(s)" e o preço total fica R$ 0,00.
- **Como testar:** CT-03.

### BUG 2 - Promoção "7ª noite grátis" anunciada, mas NÃO aplicada (Severidade: Alta)
- **Onde:** O resumo anuncia a promoção, mas `precoTotal = preco * noches` e o total no modal também calculam todas as noites.
- **Esperado:** Estadias de 7+ noites devem descontar 1 noite (ex.: 7 noites = 6 pagas).
- **Obtido:** 7 noites no Standard (250) apresentam Total = R$ 1.750,00 em vez de R$ 1.500,00.
- **Como testar:** CT-06.

### BUG 3 - Duplo clique em "Confirmar reserva" cria reservas duplicadas (Severidade: Média)
- **Onde:** `confirmar()` não bloqueia reentrância (botão não é desabilitado durante a operação).
- **Esperado:** Uma única reserva por clique; sem duplicidade no array de reservas.
- **Obtido:** Cliques rápidos consecutivos adicionam a reserva mais de uma vez (observável ao buscar novamente o mesmo período).
- **Como testar:** CT-12.

### BUG 4 - Validação de e-mail muito frágil (Severidade: Baixa/Média)
- **Onde:** `confirmar()` aceita `a@b.c` e `x@.com` como e-mails válidos.
- **Esperado:** Um e-mail com domínio real (ex.: `maria@site.com`) e rejeição de formatos incompletos.
- **Como testar:** CT-10.

---

## Bugs que você PODE ter notado e não são intencionais
- Uso de `toISOString()` para datas pode gerar deslocamento de 1 dia dependendo do fuso do navegador (bug de fuso real, comum em QA!). Anote se observou.

---

## Principais lições deste exercício
- Testar casos-limite de datas (mesmo dia, dia anterior).
- Verificar se promoções anunciadas realmente se refletem nos cálculos.
- Tentar duplo-clique e ações rápidas para encontrar condições de corrida.
- Nunca aceitar o valor exibido sem conferir a matemática.