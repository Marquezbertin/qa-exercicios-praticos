# EXP-002 — Geração de casos de teste a partir de requisitos

**Status:** Concluído · **Natureza:** Experimento exploratório · **Data:** 2026-09-06

> Pertence ao laboratório exploratório (`README.md`). **Não** constitui evidência direta do experimento formal da pesquisa principal (sistemas completos gerados por agentes).

## 1. Objetivo

Avaliar como diferentes modelos de IA projetam casos de teste a partir dos mesmos requisitos funcionais e da mesma implementação Python.

Observados: cobertura de defeitos, requisitos, fronteiras, entradas inválidas, efeitos colaterais, especificidade, executabilidade, redundância, ambiguidades e eventual desvio da tarefa.

## 2. Pergunta exploratória

> Como diferentes modelos de IA projetam casos de teste quando recebem os mesmos requisitos e a mesma implementação?

Questão derivada:

> A capacidade de identificar um defeito implica necessariamente a capacidade de projetar um caso de teste específico capaz de revelá-lo?

## 3. Modelos avaliados

Oreate AI · Claude AI · Gemini — mesmo contexto, mesmo prompt.

## 4. Tarefa

Atuação como profissionais experientes de QA e engenharia de software: criar estratégia de testes para `create_order`. Cada caso com nome, objetivo, dados de entrada, resultado esperado e requisito validado. Considerar casos positivos, negativos, fronteiras, entradas inválidas, efeitos colaterais e combinações de regras. Instruídos a **não implementar** os testes.

## 5. Requisitos utilizados

- **R1:** somente usuários com status `active` podem criar pedidos.
- **R2:** quantidade de cada item deve ser inteira e maior que zero.
- **R3:** estoque deve ser suficiente; quantidade exatamente igual ao estoque é permitida.
- **R4:** `SAVE10` concede 10% quando subtotal >= R$100.
- **R5:** estoque somente pode ser alterado após validação de todos os itens.
- **R6:** total = subtotal - desconto + frete.
- **R7:** clientes VIP não pagam frete.
- **R8:** não VIP paga R$20, exceto subtotal >= R$200.

## 6. Implementação analisada

```python
def create_order(user, items, inventory, coupon=None):

    if user["status"] != "active":
        raise ValueError("Usuário inativo")

    subtotal = 0

    for item in items:
        product_id = item["product_id"]
        quantity = item["quantity"]

        if quantity <= 0:
            raise ValueError("Quantidade inválida")

        if inventory[product_id] < quantity:
            raise ValueError("Estoque insuficiente")

        inventory[product_id] -= quantity

        subtotal += inventory[product_id] * quantity

    discount = 0

    if coupon == "SAVE10" and subtotal > 100:
        discount = subtotal * 0.10

    if user.get("vip"):
        shipping = 20
    elif subtotal > 200:
        shipping = 0
    else:
        shipping = 20

    total = subtotal - discount + shipping

    return {
        "subtotal": round(subtotal, 2),
        "discount": round(discount, 2),
        "shipping": round(shipping, 2),
        "total": round(total, 2)
    }
```

## 7. Gabarito calibrado de defeitos

| ID | Defeito | Requisito |
|---|---|---|
| D1 | Quantidade positiva fracionária é aceita porque não há validação de inteiro | R2 |
| D2 | Estoque é decrementado antes da validação de todos os itens | R5 |
| D3 | Subtotal usa estoque restante como se fosse preço | R6 / cálculo |
| D4 | SAVE10 usa `> 100` em vez de `>= 100` | R4 |
| D5 | VIP recebe frete de R$20 em vez de frete grátis | R7 |
| D6 | Frete grátis usa `> 200` em vez de `>= 200` | R8 |

**Critério de cobertura:** um defeito só é considerado coberto quando o caso proposto contém entradas e expectativa capazes de revelar o defeito na implementação apresentada. Quantidade de testes, isoladamente, não determina qualidade.

## 8. Resultados por modelo

### Oreate AI — 32 casos

| Defeito | Cobertura |
|---|---|
| D1 | ❌ |
| D2 | ✅ |
| D3 | ⚠️ |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 4/6 (66,7%)** — D3 separado (interface de precificação). Pontos:

- forte cobertura de fronteiras, efeitos colaterais, múltiplos itens e combinações;
- não criou teste específico para quantidade fracionária positiva (embora R2 exija inteiro);
- iniciou a resposta identificando bugs antes dos testes (desvio parcial da tarefa);
- vários casos usam subtotal/preço hipotéticos não representados diretamente na função.

### Claude AI — 32 casos

| Defeito | Cobertura |
|---|---|
| D1 | ✅ |
| D2 | ✅ |
| D3 | ⚠️ |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 5/6 (83,3%)** — D3 separado. Pontos:

- identificou explicitamente a ambiguidade de precificação e criou teste específico para `quantity = 2.5` (tradução direta da exigência de inteiro);
- forte cobertura de fronteiras, atomicidade, cupom, frete VIP e combinações;
- limitação: vários casos adicionam um campo `price` inexistente na assinatura — conceitualmente adequados, mas nem todos diretamente executáveis contra o código sem resolver a precificação;
- discutiu bugs/divergências antes da estratégia de testes (desvio parcial da tarefa).

### Gemini — 14 casos

| Defeito | Cobertura |
|---|---|
| D1 | ❌ |
| D2 | ✅ |
| D3 | ⚠️ |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 4/6 (66,7%)** — D3 separado. Pontos:

- menos da metade dos casos de Oreate/Claude, mas cobriu os principais comportamentos e fronteiras críticas (R$100 SAVE10, R$200 frete grátis);
- criou teste específico para atomicidade;
- não criou teste para quantidade fracionária positiva; cobriu zero/negativa apenas;
- iniciou a resposta identificando bugs críticos antes da estratégia de testes.

## 9. Matriz comparativa

| Critério | Oreate | Claude | Gemini |
|---|---:|---:|---:|
| Nº de casos | 32 | 32 | 14 |
| D1 — quantidade inteira | ❌ | ✅ | ❌ |
| D2 — atomicidade | ✅ | ✅ | ✅ |
| D3 — subtotal | ⚠️ | ⚠️ | ⚠️ |
| D4 — SAVE10 >=100 | ✅ | ✅ | ✅ |
| D5 — VIP sem frete | ✅ | ✅ | ✅ |
| D6 — frete >=200 | ✅ | ✅ | ✅ |
| Fronteiras | Forte | Forte | Forte |
| Efeitos colaterais | Forte | Forte | Forte |
| Entradas inválidas | Forte | Forte | Moderada |
| Combinações | Forte | Forte | Moderada |
| Ambiguidade de preço | Moderada | **Forte** | Moderada |
| Especificidade | Boa | **Muito boa** | Boa |
| Economia de casos | Baixa | Baixa | **Alta** |

## 10. Resultado quantitativo principal

| Modelo | Defeitos claramente cobertos | Cobertura |
|---|---:|---:|
| Oreate | 4/6 | 66,7% |
| Claude | **5/6** | **83,3%** |
| Gemini | 4/6 | 66,7% |

D3 mantido como cobertura parcial: a função não apresenta mecanismo claro de preço unitário; cobertura plena exigiria premissa externa à interface fornecida.

## 11. Principal achado exploratório

O resultado mais relevante é a diferença entre **identificar um requisito/defeito** e **transformá-lo em um caso de teste capaz de revelá-lo**.

D1 é o exemplo mais claro: o requisito exige quantidade inteira; Oreate e Gemini não criaram teste específico para quantidade fracionária positiva, enquanto Claude criou `quantity=2.5`.

Hipótese exploratória (não generalizável):

> Modelos podem apresentar desempenho diferente entre reconhecimento de condições defeituosas e tradução dessas condições em testes verificáveis.

## 12. Quantidade versus qualidade

Oreate e Claude: 32 casos; Gemini: 14. A diferença de quantidade não produziu diferença proporcional de cobertura (Gemini igualou a cobertura clara de Oreate com menos casos). Quantidade de casos **não** é métrica suficiente: considerar cobertura, relevância, executabilidade, especificidade e redundância.

## 13. Desvio da tarefa

Os três modelos apresentaram análise de defeitos antes da elaboração dos testes — útil profissionalmente, mas desvio parcial da instrução experimental. Comportamento candidato a investigação em experimentos posteriores.

## 14. Limitações

1. Apenas três modelos avaliados.
2. Experimento exploratório.
3. Nenhuma execução automatizada dos casos propostos.
4. Ambiguidade importante de precificação na função.
5. Alguns modelos introduziram premissas inexistentes na assinatura.
6. Quantidade de casos não representa diretamente qualidade.
7. Conjunto pequeno e deliberadamente conhecido de defeitos.
8. Resultados dependem do prompt.
9. D3 mantido como cobertura parcial.

## 15. Conclusão exploratória

No cenário avaliado, **Claude apresentou a maior cobertura clara (5/6)**; Oreate e Gemini cobriram claramente 4/6. Não é possível concluir que Claude seja globalmente melhor para QA — o resultado vale somente para cenário, prompt, requisitos e implementação deste experimento. O achado mais relevante é a diferença entre **detecção de defeitos e geração de testes para detectar defeitos**, especialmente na exigência de quantidade inteira.

## 16. Próximo experimento sugerido — EXP-003

**Geração de testes orientada à detecção de defeitos**: fornecer apenas requisitos (sem revelar a existência de defeitos) e avaliar se os modelos geram testes capazes de revelar sistematicamente categorias de falhas.

Condições futuras possíveis: testes espontâneos; testes derivados requisito por requisito; testes orientados por técnicas explícitas de QA; testes gerados após análise de risco.