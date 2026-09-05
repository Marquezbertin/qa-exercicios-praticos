# Simulações - Você é o QA dessas empresas

Cenários de entrevista e de trabalho real. Sem resposta pronta: o objetivo é TREINAR o raciocínio, a comunicação e a documentação. Leia o cenário e responda como faria.

---

## Cenário 1 - QA em entrevista (Sprint Review)

**A empresa:** a loja `TechStore` (site deste repositório).
**Pergunta do recrutador:** "Você vai testar o carrinho de compras. Por onde começa? O que documenta?"

**O que fazemos na resposta ideal:**
1. Defino o escopo (carrinho, cupons, frete, cálculo total).
2. Levanto as regras de negócio (limite do frete, cupons não acumulam, etc.).
3. Crio casos: feliz, negativo e de borda (99,99 / 100,00 / 100,01).
4. Executo manual e, se possível, exploro (DevTools) para achar defeitos extras.
5. Reporto cada defeito com passos, evidência, severidade.
6. Fecho com matriz de resultados.

**Entregue:** escreva aqui o mini plano (5-10 linhas).

---

## Cenário 2 - Bug "urgente" em produção

**Situação:** Cliente liga: "sisteminha mostrou saldo errado depois de uma transferência do Banco ABC". Você tem 2 minutos para tomar decisões.
**Sua resposta (escreva):**
- Quais as 3 primeiras coisas que você faz?
- O que pergunta ao cliente para reproduzir?
- Como tria a severidade?
- Como comunica ao dev e ao PO?

**Check final:** respondeu com "reproduzir primeiro -> confirmar a regra (taxa 2% acima de 1000?) -> verificar saldo/banco -> reportar com evidência", está no caminho.

---

## Cenário 3 - Sprint com escopo estourado

**Situação:** A sprint tem 20 histórias; o time só consegue testar 10 com a qualidade mínima. O PO pede qualidade MÁXIMA em tudo.
**Sua postura (escreva):**
- Você concorda em tudo? 
- Como negocia priorização?
- Quais riscos você comunica?

**Pistas:** negociar critérios de aceite, priorizar crítico/regressão, propor release em fatias, usar smoke para o restante. Nunca "aceitar silenciosamente".

---

## Cenário 4 - Teste móvel para o `FoodGo`

**Situação:** Aplicativo de delivery. Precisa funcionar offline? Sem sinal o pedido não vai sair.
**Sua abordagem (escreva):**
- Liste os testes de conectividade (sem sinal, wifi instável, mudança 4G->wifi).
- Como você testa "estado do pedido" se o app perder conexão no meio do fluxo?
- O que é mais crítico de testar antes do release?

---

## Cenário 5 - Automação que não aguenta mais

**Situação:** 400 casos E2E frágeis (quebram toda sexta). O time quer "automatizar tudo".
**Sua resposta (escreva):**
- Como você tria os 400 (bug de teste vs. bug de app)?
- Quais casos você NÃO automatiza?
- Que melhoria técnica propõe (Page Objects, waits, data-testid, CI)?
- Como convence o time a recomeçar com menos casos estáveis?

---

## Cenário 6 - Release gate

**Situação:** Falta 1 dia para release e foi encontrado 1 bug de segurança (login aceita qualquer senha de 8 dígitos -- veja `portal-cliente`/`banco-abc`).
**Sua posição (escreva):**
- Release sai ou não? Quem decide?
- Que dados você apresenta para convencer?
- Que plano de mitigação você sugere (fix rápido, workaround, rollout)?

**Pistas:** bug de autenticação = severidade CRÍTICA. Idealmente NÃO lança sem correção, ou lança com plano e rollback. Documentar a decisão.

---

## Como usar estes cenários

- **Em dupla:** um é QA, outro é entrevistador/cliente.
- **Sozinho:** escreva 5-10 linhas por cenário e revise em 48h (você melhora revisando).
- Grave-se respondendo (1 min por cenário) para treinar clareza.