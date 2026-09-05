# Momento Matador - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - Busca case-sensitive (Severidade: Alta)
- **Onde:** `renderizar()` usa `j.nome.indexOf(filtro)` sem normalizar.
- **Esperado:** `zelda` e `ZELDA` devem encontrar "The Legend of Zelda".
- **Obtido:** `zelda` (minúsculas) não retorna nada, pois o nome tem "Zelda" com maiúscula.
- **Como testar:** CT-03.
- **Observação:** Este é o famoso bug de busca que quase toda loja já teve.

### BUG 2 - Promoção "até hoje" sem lógica de expiração (Severidade: Média)
- **Onde:** O aviso anuncia desconto "até hoje", mas não há nenhuma verificação de data em `renderizar()`.
- **Esperado:** Após a data de validade, o preço volta ao cheio.
- **Obtido:** O desconto é aplicado para sempre.
- **Como testar:** CT-08.

### BUG 3 - Sem feedback ao adicionar ao carrinho (Severidade: Baixa - UX)
- **Onde:** `comprar()` atualiza o carrinho sem nenhuma animação/mensagem/deslocamento de tela.
- **Esperado:** Confirmação visível (ex.: toast "item adicionado" ou destaque no carrinho).
- **Como testar:** CT-11.

---

## Principais lições deste exercício
- Buscas de texto devem ser case-insensitive (e idealmente normalizar acentos).
- Promoções com prazo exigem lógica de expiração testável.
- Sempre conferir a matemática aplicada (desconto) com o valor exibido.
- Feedback de UX faz parte da qualidade percebida.