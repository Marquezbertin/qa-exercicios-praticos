# SQL para QA - Exercícios Práticos

Objetivo: o QA usa SQL o tempo todo (conferir massa, validar resultado de telas, auditoria). Use MySQL/Postgres/SQLite local, ou o site de treino SQLite Online. Crie as tabelas abaixo e responda.

---

## Schema de exemplo (loja)

```sql
CREATE TABLE clientes (
  id INTEGER PRIMARY KEY,
  nome TEXT NOT NULL,
  email TEXT UNIQUE,
  data_cadastro TEXT
);

CREATE TABLE pedidos (
  id INTEGER PRIMARY KEY,
  cliente_id INTEGER,
  total REAL,
  status TEXT,
  FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO clientes VALUES
  (1, 'Ana Souza', 'ana@email.com', '2026-01-05'),
  (2, 'Bruno Lima', 'bruno@email.com', '2026-02-10'),
  (3, 'Carla', 'carla@email.com', '2026-03-15'),
  (4, 'Sem Pedido', 'sp@email.com', '2026-04-01');

INSERT INTO pedidos VALUES
  (100, 1, 250.00, 'entregue'),
  (101, 1, 39.90, 'cancelado'),
  (102, 2, 119.50, 'entregue'),
  (103, 3, 5000.00, 'pendente');
```

---

## Exercício 1 - Seleções básicas
1. Liste todos os clientes.
2. Liste os clientes cadastrados em fevereiro de 2026 ou depois.
3. Liste nome e email de quem NÃO tem pedido (LEFT JOIN + IS NULL).

## Exercício 2 - Agregações
4. Total de pedidos por cliente (com nome).
5. Valor médio dos pedidos ENTREGUES.
6. Maior e menor pedido.

## Exercício 3 - Subconsultas
7. Clientes com pedido acima da média geral.
8. Pedidos de clientes que se cadastraram antes de 2026-03-01.

## Exercício 4 - Atualização (massa) [CUIDADO]
9. Atualize o status dos pedidos `pendente` da Carla para `cancelado` (simule negócio).
10. DELETE: apague apenas pedidos cancelados. (Confirme antes com SELECT!)
11. **Desafio:** suas queries 9-10 alteraram o número retornado do Exercício 1? Explique por quê.

## Exercício 5 - Validação de dados (QA mindset)
12. Escreva uma query que retorne clientes com e-mail duplicado (deveria dar vazio: UNIQUE).
13. Escreva uma query que detecte "órfãos": pedidos com `cliente_id` inexistente.
14. Escreva uma query que retorne pedidos com `total` negativo (deveria ser impossível na tela).

---

## Gabarito esperado (confira as suas respostas!)

**1.** `SELECT * FROM clientes;`

**2.** `SELECT nome FROM clientes WHERE data_cadastro >= '2026-02-01';`
   -> Bruno, Carla, Sem Pedido.

**3.** `SELECT c.nome FROM clientes c LEFT JOIN pedidos p ON p.cliente_id = c.id WHERE p.id IS NULL;`
   -> Sem Pedido (id 4).

**4.** `SELECT c.nome, COUNT(p.id) AS pedidos FROM clientes c LEFT JOIN pedidos p ON p.cliente_id=c.id GROUP BY c.id;`

**5.** `SELECT AVG(total) FROM pedidos WHERE status='entregue';` -> (250 + 119,50)/2 = 184,75.

**6.** `SELECT MAX(total), MIN(total) FROM pedidos;` -> 5000 e 39,90.

**7.** 
```sql
SELECT c.nome, p.total FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
WHERE p.total > (SELECT AVG(total) FROM pedidos);
```
   -> Carla (5000 acima de média ~1352,35).

**8.** `SELECT * FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE data_cadastro < '2026-03-01');`
   -> pedidos 100, 101, 102.

**9.** `UPDATE pedidos SET status='cancelado' WHERE cliente_id=3 AND status='pendente';`

**10.** `DELETE FROM pedidos WHERE status='cancelado';` (antes, `SELECT * FROM pedidos WHERE status='cancelado';`)

**11.** Após o DELETE, o cliente 3 (Carla) deixa de ter pedidos -> passa a aparecer no Exercício 1 item 3 (sem pedidos). **Isto ilustra como mudanças de massa mudam o resultado esperado dos testes — sempre documentar!**

**12.** `SELECT email, COUNT(*) FROM clientes GROUP BY email HAVING COUNT(*) > 1;`

**13.** `SELECT * FROM pedidos WHERE cliente_id NOT IN (SELECT id FROM clientes);`

**14.** `SELECT * FROM pedidos WHERE total < 0;`

---

## Dica importante para QA
- Sempre rode o `SELECT` antes do `UPDATE`/`DELETE` (mesmo banco de teste!).
- Use transações (`BEGIN;` ... `ROLLBACK;`) quando o ambiente permitir, para não poluir a massa.