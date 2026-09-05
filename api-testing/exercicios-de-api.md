# Testes de API - Exercícios Práticos

Objetivo: praticar testes de API de verdade. Use **Postman**, **Insomnia**, **newman** ou scripts **Python (requests)**. APIs públicas gratuitas sugeridas: JSONPlaceholder, ReqRes, PokéAPI.

> Alguns exercícios usam a ideia de uma API fictícia de e-commerce que você mesmo irá modelar. Anote tudo como se fosse um relatório de QA.

---

## 🔹 Exercício 1 - Fluxo CRUD básico (JSONPlaceholder)

`https://jsonplaceholder.typicode.com/posts`

1. Crie um POST enviando `{ "title": "QA test", "body": "abc", "userId": 1 }`.
2. Listar `GET /posts` e `GET /posts/1`.
3. Atualizar com PUT e com PATCH (explique a diferença de comportamento).
4. Deletar `DELETE /posts/1`.

**O que registrar (QA):** status esperado por verbo (200/201/204), formato do corpo de resposta, header que confirma. Verifique também `GET /posts/9999` (404 esperado).

---

## 🔹 Exercício 2 - Validação de status codes e corpo

Para cada cenário, preencha a tabela:

| Requisição | Status esperado | O que valida no corpo |
|---|---|---|
| `GET /users/1` (ReqRes ou JSONPlaceholder) | 200 | `{ "data": {...} }` |
| `GET /users/99999` |  |  |
| POST `/users` sem `name` |  |  |
| GET com header `Authorization` inválido em API que protege (ex.: ReqRes com token errado) |  |  |

**Conclusão esperada:** status sozinho não é suficiente; o corpo também precisa ser conferido.

---

## 🔹 Exercício 3 - Teste de contrato

"O consumidor (front-end) espera que `GET /users/{id}` retorne SEMPRE: `id`, `name`, `email`, `phone`."

1. Monte uma coleção/collection que valide: presença dos campos, tipos (int de id, string de name).
2. **Bonus (automação):** escreva um teste em Python com `requests` que falhe se qualquer campo faltar ou tiver tipo errado.

---

## 🔹 Exercício 4 - Testes negativos de API

Para a API fictícia de pedidos, liste e execute:
1. Enviar JSON malformado (`{ "valor": ` ) -> esperado **400**.
2. Enviar valor negativo `-10` -> UI valida, mas API precisa validar (400/422).
3. Enviar `Content-Type: text/plain` -> 415 **Unsupported Media Type** (se a API validar).
4. Enviar token vencido -> 401.
5. Tentar `DELETE /pedidos/1` sem permissão -> 403.

Registre o que a **sua** API (fictícia) retornaria em cada caso, e o que um QA DEFINIRIA como aceitável.

---

## 🔹 Exercício 5 - Performance baseline

Usando um endpoint simples (`GET /users/1`), meça 50 requisições e registre:
- Latência média
- p95
- Número de falhas

Defina um SLA plausível (ex.: p95 < 800ms) e verifique se passa. (Pode usar `hey`, `k6`, Locust, ou um loop em Python.)

---

## 🔹 Exercício 6 - Testes de dados (dinâmico)

Use uma massa em CSV com os casos (use `utils/data_generator` ou crie você):

| id | name | email | status esperado |
|---|---|---|---|
| 1 | Ana | ana@email.com | válido |
| 2 | Bia | bia@ | inválido |
| 3 | Camila | camila@site | inválido (sem TLD) |
| 4 | Dan | dan@empresa.com.br | válido |

Escreva um script que rode TODA a massa contra sua API e reporte quantos passaram.

---

## 🔹 Exercício 7 - Documentação do teste de API (entrega)

Produza um mini documento contendo, para o fluxo **"POST /pedidos"**:
1. Pré-condições (autenticação, massa).
2. Casos (feliz, validação, autenticação, duplicado).
3. Matriz de resultado (Passou/Falhou).
4. Exemplo de bug reportado (modelo em `modelos-templates/bug-report.md`).