# EXP-002 — Laboratório Exploratório de Modelos de IA
## Geração de casos de teste a partir de requisitos

**Status:** Concluído
**Natureza:** Experimento exploratório
**Data:** 2026-09-06

## 1. Objetivo

Avaliar como diferentes modelos de IA projetam casos de teste a partir dos mesmos requisitos funcionais e da mesma implementação Python.

Foram observados: cobertura de defeitos, requisitos, fronteiras, entradas inválidas, efeitos colaterais, especificidade, executabilidade, redundância, ambiguidades e eventual desvio da tarefa.

**Importante:** este experimento pertence ao laboratório exploratório e não constitui evidência direta do experimento formal da pesquisa principal sobre software completo gerado por agentes de IA.

## 2. Pergunta exploratória

> Como diferentes modelos de IA projetam casos de teste quando recebem os mesmos requisitos e a mesma implementação?

Questão derivada:

> A capacidade de identificar um defeito implica necessariamente a capacidade de projetar um caso de teste específico capaz de revelá-lo?

## 3. Modelos avaliados

1. Oreate AI
2. Claude AI
3. Gemini

Todos receberam o mesmo contexto e o mesmo prompt.

## 4. Tarefa

Os modelos deveriam atuar como profissionais experientes de QA e engenharia de software e criar uma estratégia de testes para `create_order`.

Cada caso deveria conter nome, objetivo, dados de entrada, resultado esperado e requisito validado. Também deveriam ser considerados casos positivos, negativos, fronteiras, entradas inválidas, efeitos colaterais e combinações de regras.

Os modelos foram instruídos a não implementar os testes.

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

### Critério de cobertura

Um defeito só é considerado coberto quando o caso proposto contém entradas e expectativa capazes de revelar o defeito na implementação apresentada. Quantidade de testes, isoladamente, não determina qualidade.

## 8. Resultado — Oreate AI

32 casos de teste.

| Defeito | Cobertura |
|---|---|
| D1 | ❌ |
| D2 | ✅ |
| D3 | ⚠️ Parcial/fragilizada pela interface |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 4/6 = 66,7%**, mantendo D3 separado por causa da interface de precificação.

Pontos relevantes:

- forte cobertura de fronteiras, efeitos colaterais, múltiplos itens e combinações;
- não criou teste específico para quantidade fracionária positiva, embora R2 exija quantidade inteira;
- iniciou a resposta identificando bugs antes dos testes, representando desvio parcial da tarefa;
- vários casos usam subtotal/preço hipotéticos que não estão diretamente representados na interface da função.

## 9. Resultado — Claude AI

32 casos de teste.

| Defeito | Cobertura |
|---|---|
| D1 | ✅ |
| D2 | ✅ |
| D3 | ⚠️ Parcial/fragilizada pela interface |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 5/6 = 83,3%**, mantendo D3 separado.

Claude identificou explicitamente a ambiguidade de precificação e criou teste específico para `quantity = 2.5`, traduzindo diretamente a exigência de inteiro em uma condição verificável. Também apresentou forte cobertura de fronteiras, atomicidade, cupom, frete VIP e combinações.

Limitação importante: vários casos adicionam um campo `price` aos dados, embora esse campo não exista na assinatura fornecida nem seja utilizado pela implementação. Portanto, são conceitualmente adequados, mas alguns não são diretamente executáveis contra o código sem resolver a questão da precificação.

Claude também discutiu bugs/divergências antes da estratégia de testes, embora a tarefa pedisse apenas o projeto dos testes.

## 10. Resultado — Gemini

14 casos de teste.

| Defeito | Cobertura |
|---|---|
| D1 | ❌ |
| D2 | ✅ |
| D3 | ⚠️ Parcial/fragilizada pela interface |
| D4 | ✅ |
| D5 | ✅ |
| D6 | ✅ |

**Cobertura clara: 4/6 = 66,7%**, mantendo D3 separado.

Gemini produziu menos da metade dos casos de Oreate e Claude, mas cobriu os principais comportamentos e fronteiras críticas: R$100 para SAVE10 e R$200 para frete grátis. Também criou teste específico para atomicidade.

Não criou teste específico para quantidade fracionária positiva. Assim como Oreate, cobriu quantidade zero/negativa, mas não a condição de tipo inteiro.

Também iniciou a resposta identificando bugs críticos antes da estratégia de testes.

## 11. Matriz comparativa

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

## 12. Resultado quantitativo principal

| Modelo | Defeitos claramente cobertos | Cobertura |
|---|---:|---:|
| Oreate | 4/6 | 66,7% |
| Claude | **5/6** | **83,3%** |
| Gemini | 4/6 | 66,7% |

D3 foi mantido como cobertura parcial porque a função não apresenta um mecanismo claro de preço unitário. Contá-lo como cobertura plena exigiria uma premissa externa à interface fornecida.

## 13. Principal achado exploratório

O resultado mais relevante não é a quantidade de testes, mas a diferença entre:

> identificar um requisito/defeito

e

> transformá-lo em um caso de teste capaz de revelar o defeito.

D1 é o exemplo mais claro. O requisito exige quantidade inteira. Oreate e Gemini não criaram um teste específico para uma quantidade positiva fracionária, enquanto Claude criou `quantity=2.5`.

Isso sugere uma hipótese exploratória:

> Modelos podem apresentar desempenho diferente entre reconhecimento de condições defeituosas e tradução dessas condições em testes verificáveis.

Essa hipótese não deve ser tratada como conclusão generalizável.

## 14. Quantidade versus qualidade

Oreate e Claude produziram 32 casos cada; Gemini produziu 14.

Mesmo assim, a diferença de quantidade não produziu uma diferença proporcional de cobertura. Gemini atingiu a mesma cobertura clara de Oreate com menos casos.

Isso reforça que quantidade de casos não é métrica suficiente. Devem ser considerados cobertura, relevância, executabilidade, especificidade e redundância.

## 15. Comportamento de desvio da tarefa

Os três modelos apresentaram algum grau de análise de defeitos antes da elaboração dos testes.

Esse comportamento pode ser útil profissionalmente, mas representa desvio parcial da instrução experimental de produzir somente casos de teste.

É um comportamento que pode ser investigado em experimentos posteriores.

## 16. Limitações

1. Apenas três modelos foram avaliados.
2. O experimento é exploratório.
3. Não houve execução automatizada dos casos propostos.
4. A função possui ambiguidade importante relacionada à precificação.
5. Alguns modelos introduziram premissas não existentes na assinatura.
6. Quantidade de casos não representa diretamente qualidade.
7. O problema contém um conjunto pequeno e deliberadamente conhecido de defeitos.
8. Os resultados dependem do prompt.
9. D3 foi mantido como cobertura parcial.

## 17. Conclusão exploratória

No cenário avaliado, **Claude apresentou a maior cobertura clara, com 5 dos 6 defeitos**.

Oreate e Gemini cobriram claramente 4 dos 6.

Não é possível concluir que Claude seja globalmente um modelo melhor para QA. O resultado é válido somente para o cenário, prompt, requisitos e implementação deste experimento.

O achado mais relevante para a continuidade do laboratório é a diferença entre **detecção de defeitos e geração de testes para detectar defeitos**, especialmente no requisito de quantidade inteira.

## 18. Relação com a pesquisa formal

Este experimento não deve ser utilizado como evidência direta da qualidade dos sistemas completos gerados por agentes na pesquisa principal.

Ele funciona como laboratório exploratório para investigar comportamento de modelos, raciocínio sobre requisitos, geração de testes, fronteiras, efeitos colaterais e diferenças entre modelos.

A pesquisa formal permanece baseada no protocolo:

> "Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial"

com sistemas completos, execuções independentes, oráculo externo e matriz de defeitos.

## 19. Próximo experimento sugerido

### EXP-003 — Geração de testes orientada à detecção de defeitos

Investigar se fornecer apenas requisitos, sem revelar previamente a existência de defeitos, permite aos modelos gerar testes capazes de revelar sistematicamente diferentes categorias de falhas.

Possíveis condições futuras:

- testes gerados espontaneamente;
- testes derivados requisito por requisito;
- testes orientados por técnicas explícitas de QA;
- testes gerados após análise de risco.

## 20. Preservação dos dados brutos

As respostas originais dos modelos devem ser preservadas sem edição como dados primários do laboratório.

- Oreate AI — resposta original utilizada na análise.
- Claude AI — resposta original utilizada na análise.
- Gemini — resposta original utilizada na análise.

Qualquer normalização, correção ou interpretação deve ocorrer somente na camada de análise.