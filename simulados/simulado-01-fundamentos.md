# Simulado 01 - Fundamentos de QA (20 questões)

Responda no formato **1-A**, **2-C**... Confira no gabarito no final de cada bloco.

---

## Bloco A - Conceitos

**1.** Complete: "A falha observável ocorre quando:
A) uma ação humana causa um resultado incorreto
B) um defeito é executado em execução
C) o código está mal documentado
D) o ambiente não é o de produção"

**2.** Um bug de alta severidade e baixa prioridade é aquele em que:
A) quebra muito o sistema mas pode esperar
B) o impacto é pequeno, mas o cliente quer resolvido logo
C) não afeta o usuário
D) foi aprovado pelo PO sem teste

**3.** A técnica que identifica valores nos limites das classes de equivalência chama-se:
A) Particionamento de equivalência
B) Análise de valor-limite
C) Teste de caixa-branca
D) Pairwise

**4.** "Devemos construir o produto CORRETO?" é a definição de:
A) Verificação
B) Validação
C) Regressão
D) Smoke test

**5.** No fluxo, a ordem correta de ocorrência é:
A) falha -> erro -> defeito
B) erro -> defeito -> falha
C) defeito -> erro -> falha
D) erro -> falha -> defeito

---

### Gabarito Bloco A
1-B, 2-A, 3-B, 4-B, 5-B

---

## Bloco B - Software testing (prática)

**6.** Um sistema aceita idade entre 18 e 65 anos. Usando análise de valor-limite, quais valores devem ser testados?
A) 18, 19, 64, 65
B) 17, 18, 65, 66
C) 0, 18, 65, 999
D) 17, 18, 19, 64, 65, 66

**7.** Qual a melhor descrição de Smoke Test?
A) Teste executado uma vez a cada release por dias corridos
B) Bateria rápida para confirmar que o build instala e as funções principais estão de pé
C) Teste de aceitação com o cliente
D) Teste de balanceamento de carga

**8.** Para automatizar, o melhor seletor é:
A) `//tabela/div/tr[2]/td[3]`
B) `element.css("cor")`
C) `[data-testid="btn-finalizar"]`
D) `div[class*="btn"]:nth-child(3)`

**9.** Ao testar uma API, o QA deve validar obrigatoriamente:
A) somente o status HTTP
B) o status HTTP e o corpo da resposta (schema/conteúdo)
C) somente o tempo de resposta
D) a documentação do dev

**10.** Que teste NÃO deveria ser automatizado?
A) Regressão com 200 casos estáveis
B) Login em mais de 5 browsers
C) Testes exploratórios de uma tela nova e instável
D) Consumo de uma API estável

---

### Gabarito Bloco B
6-D, 7-B, 8-C, 9-B, 10-C

---

## Bloco C - Cenário

**Cenário:** O sistema de pedidos da empresa tem as regras:
- Pedido mínimo de R$ 30.
- Frete grátis acima de R$ 100.
- Cupom `ATENDE15` dá 15% (substitui o frete grátis).
- Cupom `NUNCA` não existe.

**11.** O total correto de um pedido de R$ 250,00 com `ATENDE15` é:
A) 250,00
B) 212,50
C) 212,50 + frete
D) 237,50

**12.** Um pedido de R$ 99,99 deve:
A) ter frete grátis (acima de 100)
B) pagar frete
C) ser bloqueado (mín. 30)
D) aplicar cupom automaticamente

**13.** O caso de teste para "pedido mínimo" cobriria:
A) 29,99 / 30,00 / 30,01
B) 30,00 / 100,00
C) 1,00 e 1.000,00
D) só 30,00

---

### Gabarito Bloco C
11-B, 12-B, 13-A

---

## Resultado

| Acertos | Interpretação |
|---|---|
| 16–20 | Excelente. Pronto para entrevistas de nível PLENO. |
| 11–15 | Bom. Reforçar técnicas de teste e vocabulário. |
| 6–10 | Está evoluindo. Estudar fundamentos antes de avançar. |
| 0–5 | Recomeçar pelos fundamentos. Sugestão: ler o README principal. |