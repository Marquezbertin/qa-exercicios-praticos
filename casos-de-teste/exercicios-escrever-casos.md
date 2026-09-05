# Casos de Teste - Exercícios de escrita

Escrever casos de teste BEM escritos é a habilidade nº1 de um QA. Aqui há cenários para treinar.

---

## Exercício 1 - Escreva casos para: "Login do Portal Cliente"

Escreva no mínimo 8 casos cobrindo:
- Feliz (credenciais corretas)
- E-mail errado
- Senha errada
- Campos vazios
- E-mail com maiúsculas (case)
- Limite de caracteres (senha)
- Mensagens de erro amigáveis
- (extra) tentaçativas repetidas

Use o modelo `modelos-templates/test-case.md`. Uma versão pronta está em `sites-para-testar/portal-cliente/roteiro-de-teste.md`.

---

## Exercício 2 - Escreva casos para: "Calculadora de desconto"

Regra: desconto entre 0 e 50%, preço > 0, total nunca negativo. Cobre bordas:
- preço 0 (deve falhar)
- preço negativo
- desconto 0 (sem desconto)
- desconto 50 (limite)
- desconto 50,01 (deve falhar)
- preço com centavos (100,50 - 10% = 90,45)

Compare com `encontre-o-bug/codigo/exercicio-01-calculadora.py`.

---

## Exercício 3 - Escreva casos para: "Carrinho da TechStore com cupom"

Regras: frete grátis ACIMA de R$ 100; cupom QA10 (-10%); não acumulam; total nunca negativo.
Cubra resumo e total (não só feliz). Compare depois com o `roteiro-de-teste.md` da TechStore.

---

## Exercício 4 - Reescreva um caso RUIM

O caso abaixo está ruim. Descubra por quê e reescreva bem:

> "Testar o botão de comprar. Clica e vê se funciona."

**Problemas esperados:** sem pré-condição, sem dados, sem resultado esperado mensurável, sem passos reprodutíveis.

---

## Exercício 5 - Priorização de casos

Você tem 3 horas para testar o `Banco ABC`. Priorize ESTES casos (ordene e justifique):

- Transferência com taxa de 2% (acima de 1000)
- Login com credenciais demo
- Depósito com vírgula (centavos)
- Botão "ocultar saldo"
- Transferência para conta inexistente
- Extrato (ordem das linhas)

**Dica:** o que causa prejuízo/erro crítico vai primeiro.

---

## Checklist de um bom caso de teste

- [ ] ID e título claros (ação + objeto + resultado desejado)
- [ ] Pré-condições (estado, dados, ambiente)
- [ ] Passos numerados e reprodutíveis
- [ ] Dados de entrada específicos (não "valor qualquer")
- [ ] Resultado esperado MENSURÁVEL
- [ ] Pós-condição (estado do sistema após)
- [ ] Independência (não depender de outra execução)