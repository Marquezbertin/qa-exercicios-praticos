# Simulado 02 - API, Banco de Dados e Segurança (15 questões)

Formato de resposta: **1-A**, **2-B**, ... Gabarito no final.

---

**1.** Qual verbo HTTP produz efeito colateral de ALTERAÇÃO e NÃO é idempotente?
A) GET
B) PUT
C) POST
D) DELETE

**2.** Uma API retorna `201 Created` ao criar um recurso. Isso significa:
A) sucesso com retorno de erro no corpo
B) criado com sucesso
C) sem autorização
D) aceito para processamento posterior

**3.** `GET /clientes/999` retorna `404`. O teste de **contrato** deve validar:
A) somente o 404
B) body/erro padronizado + 404
C) o tempo de resposta
D) que o servidor reiniciou

**4.** Num SELECT para QA, qual query retorna clientes que NÃO têm pedidos?
A) `SELECT * FROM clientes WHERE id NOT IN (SELECT DISTINCT cliente_id FROM pedidos)`
B) `SELECT * FROM clientes WHERE id IN (SELECT DISTINCT cliente_id FROM pedidos)`
C) `SELECT * FROM pedidos LEFT JOIN clientes ON ...`
D) `SELECT * FROM clientes WHERE pedidos IS NULL`

**5.** Para simular dados que o QA precisa validar (mesmo registro), o ideal é construir massa de dados:
A) aleatória (faker) sempre
B) determinística para fins do cenário
C) copiada inteira de produção
D) vazia

**6.** Um token expirado deve retornar:
A) 200 com dados
B) 302
C) 401 Unauthorized
D) 500

**7.** Um QA testando SQL injection em um login de site próprio (ambiente de teste) deve tentar:
A) `' OR 1=1 --` em campos de texto
B) somente em campo de senha
C) nunca testar isso em automação
D) apenas copiar o banco

**8.** O `teto` do INSS (valor máximo contribuído) num sistema financeiro deve ser testado:
A) com valor exatamente igual ao teto
B) com valor do teto e um centavo acima
C) só com valor acima
D) nunca, pois é cálculo do contador

**9.** Um bug encontrado exclusivamente em produção, reproduzido com 3 passos, deve:
A) ser descrito sem passos (é prod)
B) ser reportado com passos exatos, evidências, e pergunta sobre dados de produção
C) ser aberto no Jira sem informações (para não expor dados)
D) ser corrigido direto pelo QA

**10.** Qual técnica automatiza melhor o teste de regressão de regras de negócio (tais como cálculo de frete)?
A) Teste E2E em browser 100% do tempo
B) Testes em camadas menores (regras puras/unitárias) + poucos E2E
C) Teste manual apenas
D) Teste de estresse

**11.** O `content-type` esperado de uma API JSON que estão testando com POST é:
A) `text/html`
B) `application/json`
C) `multipart/form-data` sempre
D) `application/xml`

**12.** Em teste de perfomance, `p95 = 2s` significa:
A) 95% das requisições responderam em até 2s
B) 5% das requisições falharam
C) a latência máxima foi de 2s
D) o servidor suporta 95 usuários

**13.** Para garantir que uma alteração numa API não quebrou o consumidor, o teste ideal é:
A) unit de react
B) contract test
C) teste de carga
D) teste de usabilidade

**14.** Um teste de banco que confirma **integridade referencial** valida:
A) dados com FK apontando para registro inexistente
B) todos os campos NOT NULL
C) unicidade do e-mail
D) performance do SELECT

**15.** Ao encontrar um valor `NULL` inesperado no banco para um campo obrigatório, o QA deve:
A) ignorar (o banco deixa)
B) reportar como bug com contexto (deveria haver CONSTRAINT)
C) alterar o dado direto
D) apagar a linha

---

## Gabarito Simulado 02

1-C, 2-B, 3-B, 4-A, 5-B, 6-C, 7-A, 8-B, 9-B, 10-B, 11-B, 12-A, 13-B, 14-A, 15-B

---

## Resultado

| Acertos | Análise |
|---|---|
| 13–15 | Ótimo. Junto com o Simulado 01, pronta base p/ Pleno. |
| 9–12 | Bom. Revisar API/SQL. |
| 0–8 | Reforçar API, SQL e boas práticas antes de avançar. |