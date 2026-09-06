# EXP-001 — Identificação de defeitos em código a partir de requisitos funcionais

**Status:** Concluído · **Natureza:** Experimento exploratório · **Consolidação:** 2026-09-06

> Pertence ao laboratório exploratório (`README.md`). **Não** constitui evidência do experimento formal da pesquisa principal.

## 1. Objetivo

Avaliar como diferentes modelos de IA identificam defeitos funcionais em um pequeno trecho de código Python quando recebem:
1. uma especificação funcional;
2. um código de implementação;
3. uma instrução explícita para identificar defeitos;
4. a exigência de demonstrar cada problema.

## 2. Modelos avaliados

Oreate AI · Claude AI · Gemini — mesmo desafio, respostas coletadas separadamente.

## 3. Prompt utilizado

> Você é um profissional experiente de QA e engenharia de software.
>
> Analise o código Python abaixo considerando os requisitos funcionais apresentados.
>
> Sua tarefa é identificar todos os defeitos que podem fazer o sistema apresentar um comportamento diferente do especificado.
>
> Para cada defeito encontrado:
> 1. Explique claramente qual é o problema.
> 2. Indique exatamente onde ele ocorre.
> 3. Explique em qual situação o defeito pode acontecer.
> 4. Dê um exemplo de entrada que demonstre o problema.
> 5. Explique qual seria o comportamento esperado.
>
> Não faça sugestões de melhoria de código que não estejam relacionadas a uma violação dos requisitos.
>
> Não reescreva o código inteiro. Concentre-se na identificação dos defeitos.

### Requisitos

1. O pedido só pode ser criado para um usuário cujo status seja "active".
2. Cada item do pedido deve possuir uma quantidade inteira maior que zero.
3. O estoque de cada produto deve ser suficiente para atender à quantidade solicitada. Se houver exatamente a quantidade solicitada em estoque, a compra deve ser permitida.
4. O cupom "SAVE10" concede 10% de desconto quando o subtotal do pedido for maior ou igual a R$ 100,00.
5. O estoque só deve ser alterado depois que todos os itens do pedido forem validados com sucesso.
6. O valor final do pedido deve ser: subtotal - desconto + frete.
7. Clientes VIP não pagam frete.
8. Clientes não VIP pagam R$ 20,00 de frete, exceto quando o subtotal for maior ou igual a R$ 200,00.

### Código

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

## 4. Gabarito calibrado (6 defeitos)

> Histórico: inicialmente planejados 5 defeitos; o 6º (D1) foi identificado na calibração e **mantido** para não alterar o gabarito em função das respostas dos modelos (evita p-hacking).

| ID | Defeito | Requisito violado |
|---|---|---|
| D1 | Quantidade não validada como inteira — valores positivos fracionários (`1.5`, `2.5`) são aceitos (`quantity <= 0` não cobre tipo) | R2 |
| D2 | Estoque alterado antes da validação completa — `inventory[product_id] -= quantity` executa antes de todos os itens serem validados | R5 |
| D3 | Subtotal usa estoque restante como se fosse preço — o código não contém preço do produto | R6 |
| D4 | Cupom usa `> 100` em vez de `>= 100` — subtotal exatamente R$100 não recebe desconto | R4 |
| D5 | Cliente VIP paga frete (`if user.get("vip"): shipping = 20`) em vez de frete grátis | R7 |
| D6 | Frete grátis usa `> 200` em vez de `>= 200` — subtotal exatamente R$200 paga frete | R8 |

## 5. Resultados brutos

| Modelo | Defeitos identificados | Cobertura |
|---|---:|---:|
| Oreate | D1, D2, D3, D4, D5, D6 | **6/6 = 100%** |
| Claude | D1, D2, D3, D4, D5, D6 | **6/6 = 100%** |
| Gemini | D2, D3, D4, D5, D6 (não identificou D1) | **5/6 = 83,3%** |

Todos os 6 defeitos identificados por Oreate e Claude vieram com explicação, localização, condição de ocorrência, exemplo e comportamento esperado.

## 6. Matriz comparativa

| Defeito | Oreate | Claude | Gemini |
|---|:---:|:---:|:---:|
| D1 — quantidade não inteira | ✅ | ✅ | ❌ |
| D2 — estoque alterado prematuramente | ✅ | ✅ | ✅ |
| D3 — subtotal usa estoque | ✅ | ✅ | ✅ |
| D4 — cupom `> 100` | ✅ | ✅ | ✅ |
| D5 — VIP paga frete | ✅ | ✅ | ✅ |
| D6 — frete `> 200` | ✅ | ✅ | ✅ |
| **Total** | **6/6** | **6/6** | **5/6** |
| **Cobertura** | **100%** | **100%** | **83,3%** |

## 7. Observações qualitativas

- **Oreate**: comportamento sistemático; identificou inclusive o problema de tipo da quantidade (fora da contagem inicial de 5); exemplos concretos.
- **Claude**: boa detalhamento das relações código–requisito–comportamento; explicação de D2/D3 particularmente clara.
- **Gemini**: boa capacidade para violações de lógica de negócio; **não identificou** a restrição explícita de `quantity` inteiro (R2).

## 8. Interpretação correta

NÃO permite afirmar que um modelo é melhor que outro em QA em geral, nem taxas gerais de detecção. O que se pode afirmar:

> No cenário específico do EXP-001, Oreate e Claude identificaram os seis defeitos do gabarito; Gemini identificou cinco dos seis. Os três detectaram os cinco defeitos de lógica de negócio originalmente planejados.

## 9. O que o experimento sugere

Diferenças de comportamento entre modelos; mais relevante que contar bugs é observar **quais tipos de defeitos cada modelo detecta**. Cinco dimensões separáveis: regras de negócio, condições de fronteira, efeitos colaterais/alteração de estado, cálculos, validação de dados/tipos.

Observação exploratória inicial:

> Neste cenário, os três modelos detectaram bem defeitos explícitos de lógica de negócio e condições de fronteira. Oreate e Claude também detectaram a restrição de tipo da quantidade; Gemini não. Tratar como hipótese/observação exploratória, não conclusão geral.

## 10. Próximo experimento relacionado

EXP-002 (mesma filosofia): geração de casos de teste a partir dos mesmos requisitos e implementação — ver `EXP-002-geracao-casos-de-teste.md`.