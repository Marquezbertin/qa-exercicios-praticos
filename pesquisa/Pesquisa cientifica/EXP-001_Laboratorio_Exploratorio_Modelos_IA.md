# Laboratório Exploratório de Comportamento de Modelos de IA

## 1. Objetivo deste documento

Este arquivo registra o trabalho realizado em paralelo à pesquisa científica principal sobre software gerado por agentes de Inteligência Artificial.

O objetivo deste laboratório exploratório é observar, de maneira controlada e organizada, **como diferentes modelos de IA se comportam diante de tarefas relacionadas a software e QA**, produzindo material complementar para compreender melhor suas capacidades, limitações e padrões de comportamento.

> **Importante:** os experimentos deste laboratório exploratório NÃO são tratados como evidência científica da pesquisa principal. Eles servem para exploração, aprendizado, geração de hipóteses, identificação de comportamentos interessantes e enriquecimento da discussão científica.

---

# 2. Relação com a pesquisa principal

A pesquisa principal tem como foco:

**Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial**

O objeto central da pesquisa principal é o **software completo produzido por agentes de IA**, e não simplesmente a capacidade de um chatbot encontrar bugs ou substituir profissionais de QA.

A pesquisa principal utiliza um desenho controlado, prospectivo e reprodutível, no qual diferentes agentes recebem a mesma especificação e produzem sistemas completos. Esses sistemas são posteriormente avaliados por um **oráculo independente**, mantido separado do agente.

O laboratório exploratório é mantido separado desse experimento formal.

---

# 3. Princípios do laboratório exploratório

Os experimentos devem, sempre que possível:

- utilizar o mesmo prompt para todos os modelos;
- utilizar exatamente a mesma entrada;
- preservar as respostas originais dos modelos;
- utilizar um gabarito independente para comparação;
- registrar defeitos encontrados e não encontrados;
- registrar falsos positivos;
- observar a qualidade das justificativas;
- observar como o modelo demonstra um defeito;
- registrar comportamentos interessantes ou inesperados;
- evitar conclusões gerais baseadas em poucos experimentos.

A regra principal é:

> **Observar comportamento, não declarar vencedores de forma geral.**

---

# 4. Experimento EXP-001

## Nome

**EXP-001 — Identificação de defeitos em código a partir de requisitos funcionais**

## Tipo

Experimento exploratório de comportamento de modelos de IA.

## Objetivo

Avaliar como diferentes modelos de IA identificam defeitos funcionais em um pequeno trecho de código Python quando recebem:

1. uma especificação funcional;
2. um código de implementação;
3. uma instrução explícita para identificar defeitos;
4. a exigência de demonstrar cada problema.

## Modelos avaliados

Foram selecionados três modelos de IA:

- **Oreate AI**
- **Claude AI**
- **Gemini**

As respostas foram coletadas separadamente utilizando o mesmo desafio.

---

# 5. Prompt utilizado

O prompt apresentado aos modelos foi:

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
>
> ### Requisitos
>
> 1. O pedido só pode ser criado para um usuário cujo status seja "active".
>
> 2. Cada item do pedido deve possuir uma quantidade inteira maior que zero.
>
> 3. O estoque de cada produto deve ser suficiente para atender à quantidade solicitada. Se houver exatamente a quantidade solicitada em estoque, a compra deve ser permitida.
>
> 4. O cupom "SAVE10" concede 10% de desconto quando o subtotal do pedido for maior ou igual a R$ 100,00.
>
> 5. O estoque só deve ser alterado depois que todos os itens do pedido forem validados com sucesso.
>
> 6. O valor final do pedido deve ser:
>    subtotal - desconto + frete.
>
> 7. Clientes VIP não pagam frete.
>
> 8. Clientes não VIP pagam R$ 20,00 de frete, exceto quando o subtotal for maior ou igual a R$ 200,00.
>
> ### Código
>
> ```python
> def create_order(user, items, inventory, coupon=None):
>
>     if user["status"] != "active":
>         raise ValueError("Usuário inativo")
>
>     subtotal = 0
>
>     for item in items:
>         product_id = item["product_id"]
>         quantity = item["quantity"]
>
>         if quantity <= 0:
>             raise ValueError("Quantidade inválida")
>
>         if inventory[product_id] < quantity:
>             raise ValueError("Estoque insuficiente")
>
>         inventory[product_id] -= quantity
>
>         subtotal += inventory[product_id] * quantity
>
>     discount = 0
>
>     if coupon == "SAVE10" and subtotal > 100:
>         discount = subtotal * 0.10
>
>     if user.get("vip"):
>         shipping = 20
>     elif subtotal > 200:
>         shipping = 0
>     else:
>         shipping = 20
>
>     total = subtotal - discount + shipping
>
>     return {
>         "subtotal": round(subtotal, 2),
>         "discount": round(discount, 2),
>         "shipping": round(shipping, 2),
>         "total": round(total, 2)
>     }
> ```

---

# 6. Gabarito calibrado

Inicialmente, o experimento foi concebido pensando em cinco defeitos.

Durante a análise/calibração, foi identificado um sexto defeito real, explicitamente suportado pelo requisito 2.

Portanto, para a análise final do EXP-001, foram considerados **6 defeitos reais**.

## D1 — Quantidade não validada como inteira

O requisito determina que a quantidade seja **inteira e maior que zero**.

O código verifica apenas:

```python
if quantity <= 0:
```

Assim, valores positivos fracionários, como `1.5` ou `2.5`, podem ser aceitos.

**Requisito violado:** 2.

---

## D2 — Estoque alterado antes da validação completa

O código executa:

```python
inventory[product_id] -= quantity
```

antes que todos os itens do pedido tenham sido validados.

Se um item posterior falhar, itens anteriores já terão alterado o estoque.

**Requisito violado:** 5.

---

## D3 — Subtotal calculado usando estoque restante

O código executa:

```python
subtotal += inventory[product_id] * quantity
```

depois de reduzir o estoque.

O valor do estoque restante está sendo utilizado como se fosse preço unitário.

Além disso, a estrutura apresentada não contém preço do produto.

**Requisito violado:** 6.

---

## D4 — Cupom usa `>` em vez de `>=`

O requisito determina desconto para subtotal:

```text
>= R$ 100,00
```

O código utiliza:

```python
subtotal > 100
```

Assim, exatamente R$ 100,00 não recebe desconto.

**Requisito violado:** 4.

---

## D5 — Cliente VIP paga frete

O requisito determina frete zero para clientes VIP.

O código utiliza:

```python
if user.get("vip"):
    shipping = 20
```

**Requisito violado:** 7.

---

## D6 — Frete grátis utiliza `>` em vez de `>=`

O requisito determina frete grátis para clientes não VIP quando:

```text
subtotal >= R$ 200,00
```

O código utiliza:

```python
elif subtotal > 200:
```

Assim, exatamente R$ 200,00 continua pagando frete.

**Requisito violado:** 8.

---

# 7. Resultados brutos

## Oreate AI

Oreate identificou **6 defeitos**.

Defeitos identificados:

- D1 — quantidade não inteira
- D2 — estoque alterado antes da validação completa
- D3 — subtotal incorreto
- D4 — cupom `> 100`
- D5 — frete VIP
- D6 — frete grátis `> 200`

### Resultado

**6/6 — 100% de cobertura**

Também apresentou, para os seis defeitos:

- explicação;
- localização;
- situação de ocorrência;
- exemplo;
- comportamento esperado.

---

# 8. Claude AI

Claude identificou **6 defeitos**.

Defeitos identificados:

- D1 — quantidade não inteira
- D2 — estoque alterado antes da validação completa
- D3 — subtotal incorreto
- D4 — cupom `> 100`
- D5 — frete VIP
- D6 — frete grátis `> 200`

### Resultado

**6/6 — 100% de cobertura**

Também apresentou explicação, localização, condição de ocorrência, exemplo e comportamento esperado para os defeitos.

Um ponto qualitativamente interessante foi a explicação do defeito relacionado ao subtotal, destacando que o código não possui uma referência adequada ao preço do produto e utiliza o estoque restante no cálculo.

---

# 9. Gemini

Gemini identificou **5 defeitos**.

Defeitos identificados:

- D2 — estoque alterado antes da validação completa
- D3 — subtotal incorreto
- D4 — cupom `> 100`
- D5 — frete VIP
- D6 — frete grátis `> 200`

Não identificou:

- **D1 — ausência de validação de quantidade inteira.**

### Resultado

**5/6 — 83,3% de cobertura**

O Gemini identificou todos os cinco defeitos originalmente previstos no experimento, mas não identificou o sexto defeito descoberto durante a calibração.

---

# 10. Matriz comparativa

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

---

# 11. Observações qualitativas

## Oreate

Demonstrou comportamento bastante sistemático.

Identificou inclusive o problema de tipo da quantidade, que não fazia parte da contagem inicial de cinco defeitos.

Apresentou exemplos concretos para os problemas identificados.

## Claude

Também apresentou cobertura completa.

Demonstrou bom detalhamento na explicação das relações entre código, requisito e comportamento observado.

A explicação do problema de estoque e do cálculo do subtotal foi particularmente clara.

## Gemini

Demonstrou boa capacidade para identificar as violações de lógica de negócio.

Encontrou todos os cinco defeitos inicialmente previstos.

Entretanto, não identificou a restrição explícita de que `quantity` deveria ser um número inteiro.

---

# 12. Interpretação correta do resultado

O resultado NÃO permite afirmar:

- que Oreate é melhor que Claude;
- que Claude é melhor que Gemini;
- que determinado modelo é melhor para QA em geral;
- que um modelo substitui um profissional de QA;
- que os modelos possuem determinada taxa geral de detecção de bugs.

O que pode ser afirmado é:

> **No cenário específico do EXP-001, Oreate e Claude identificaram os seis defeitos considerados no gabarito, enquanto Gemini identificou cinco dos seis.**

Também foi observado que os três modelos foram capazes de identificar os cinco defeitos originalmente planejados relacionados à lógica de negócio.

---

# 13. Observação metodológica importante

O sexto defeito foi descoberto durante a calibração.

A versão inicial do planejamento considerava cinco defeitos, porém o requisito 2 explicitamente exige:

> quantidade inteira maior que zero.

Como o código não verifica o tipo da quantidade, a ausência dessa validação constitui uma violação funcional legítima.

O defeito foi mantido na análise para evitar alterar silenciosamente o gabarito em função das respostas dos modelos.

Esse fato deve ser preservado no histórico do experimento.

---

# 14. O que este experimento nos ensinou

O EXP-001 mostrou que um experimento simples de análise de código pode revelar diferenças de comportamento entre modelos.

Mais importante do que apenas contar bugs é observar **quais tipos de defeitos cada modelo detecta**.

Neste experimento, foi possível separar pelo menos cinco dimensões:

1. regras de negócio;
2. condições de fronteira;
3. efeitos colaterais e alteração de estado;
4. cálculos;
5. validação de dados/tipos.

Uma observação exploratória inicial é:

> Neste cenário, os três modelos apresentaram boa capacidade de detectar defeitos explícitos de lógica de negócio e condições de fronteira. Oreate e Claude também detectaram a restrição de tipo da quantidade, enquanto Gemini não a identificou.

Essa observação deve ser tratada como **hipótese/observação exploratória**, e não como conclusão geral sobre os modelos.

---

# 15. Status atual

## Laboratório exploratório

**EXP-001 — CONCLUÍDO**

Modelos avaliados:

- Oreate AI
- Claude AI
- Gemini

Resultado:

- Oreate: 6/6
- Claude: 6/6
- Gemini: 5/6

Dados brutos das respostas já foram coletados nesta conversa.

## Próximo passo planejado

Antes de iniciar o EXP-002, o EXP-001 deve ser mantido como uma ficha experimental fechada e documentada.

O próximo experimento poderá avaliar outra capacidade, como:

**EXP-002 — Geração de casos de teste a partir de requisitos**

A mesma filosofia deverá ser mantida:

- mesmo prompt;
- mesma entrada;
- mesmos critérios;
- gabarito independente;
- preservação das respostas brutas;
- comparação quantitativa e qualitativa;
- nenhuma conclusão geral a partir de um único experimento.

---

# 16. Separação entre exploração e pesquisa científica

Esta separação deve ser mantida durante todo o projeto.

### Pesquisa principal

Foco:

**qualidade e defeitos em sistemas completos gerados por agentes de IA.**

Características:

- experimento controlado;
- agentes;
- sistemas completos;
- múltiplas execuções;
- oráculo independente;
- matriz de defeitos;
- métricas;
- reprodutibilidade;
- análise estatística.

### Laboratório exploratório

Foco:

**comportamento de modelos de IA em tarefas isoladas relacionadas a software e QA.**

Características:

- experimentos menores;
- exploração;
- comparação de comportamento;
- geração de hipóteses;
- observações qualitativas;
- material complementar.

Os resultados do laboratório exploratório **não devem ser apresentados como resultados do experimento científico principal**.

---

# 17. Registro de versão

**EXP-001 — versão inicial documentada**

Status: concluído.

Data de consolidação: 06/09/2026.

Próxima atividade: preparar EXP-002 somente após o registro deste experimento estar preservado.

