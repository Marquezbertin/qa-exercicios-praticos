# Técnicas de Teste - Exercícios

Aplique as técnicas em cenários reais. Idealmente entregue cada um como um mini documento de teste.

---

## 1. Particionamento de Equivalência

**Cenário:** Campo "quantidade de parcelas" aceita 1 a 12.

1. Defina as classes de equivalência (válida e inválidas).
2. Escolha UM representante de cada classe.
3. Explique por que NÃO é necessário testar todos os valores 1..12.

---

## 2. Análise de Valor-Limite

**Cenário:** Desconto aplica para pedidos com subtotal **maior ou igual a R$ 100,00** (`>= 100`).

1. Liste os valores a testar (limite em baixo e em cima).
2. Inclua o caso "99,99 | 100,00 | 100,01".
3. Generalize: qual a regra prática para escolher os valores de borda?

---

## 3. Tabela de Decisão

**Regra de negócio:** Frete grátis quando:
- subtotal >= R$ 100 **OU**
- cliente tem plano VIP **E** subtotal >= R$ 60

Condições: `subtotal >= 100`, `VIP >= 60`? Ações: conceder/negar frete grátis.

1. Monte a tabela de decisão completa (8 combinações => 2³).
2. Revele combinações impossíveis (ex.: VIP com subtotal baixo).
3. Escolha os casos mínimos de teste.

---

## 4. Transição de Estados

**Cenário:** Pedido de e-commerce com estados: `CRIADO`, `PAGO`, `ENVIADO`, `ENTREGUE`, `CANCELADO`, `DEVOLVIDO`.

1. Desenhe a máquina de estados (quem pode ir para onde).
2. Liste as transições permitidas.
3. Liste as transições INVÁLIDAS (ex.: `CANCELADO -> PAGO`).
4. Escolha um caminho que cubra o máximo de estados.

---

## 5. Teste Baseado em Situação / Cenário

**Cenário:** busca de voo com: origem, destino, data ida, data volta, nº de passageiros.

1. Crie 5 cenários de "jornada completa": feliz, atenção (volta antes da ida), zero resultado, máx. passageiros (9), data passada.
2. Crie a matriz de cobertura dos requisitos.

---

## 6. Pairwise (combinação mínima)

**Cenário:** combinar Navegador x SO x Dispositivo:
- Navegadores: Chrome, Firefox, Safari
- SO: Windows, macOS, Android
- Dispositivo: Desktop, Mobile

Numa combinação completa seriam 3 x 3 x 2 = 18. Usando pairwise, reduza para o mínimo que garanta cobrir cada **par** (1ª/2ª combinação, 2ª/3ª...). Escreva o conjunto que você escolheria e justifique. *(Ferramentas: pict, act - Microsoft.)*

---

## 7. Teste Exploratório

Prática com os sites deste repositório! Escolha `sites-para-testar/techstore` e:
1. Defina a missão da sessão ("descobrir bugs de cálculo de total e cupons").
2. Use um checklist mental (valores limite, caminhos alternativos, estados).
3. Documente cada ideia de teste que você explorou e o resultado.
4. Ao final, classifique os bugs por severidade.

---

## 8. Matriz de cobertura de requisitos

Para uma função (ex.: login), construa a matriz:

| Requisito | CT | Status |
|---|---|---|
| REQ-01 usuário e senha válidos autentica | CT-01 | ✅ |
| REQ-02 senha errada bloqueia | CT-02 | ✅ |
| ... | ... | ... |

- Qual % de requisitos cobertos? Qual requisito NÃO tem CT? → isso é gap de teste.

---

## Gabarito curto / dicas

1. Classes: válida [1..12], inválidas [≤0] e [≥13]. Representantes: 5, 0, 13.
2. Valores: limite 99,99 / 100,00 / 100,01. Regra: teste o limite, o imediatamente abaixo e o acima.
3. Tabela de decisão: 8 combinações; marcar quais sempre geram a mesma ação e reduzir (ex.: as com subtotal >= 100 não dependem do VIP).
4. Ver `sites-para-testar/agenda-medica` para exemplo concreto de estados (agendado/cancelado).
5-8. Não há "resposta certa única": o que importa é cobertura justificada e rastreável.