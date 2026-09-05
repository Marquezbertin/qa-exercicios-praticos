# Especificação Controlada — API de Gerenciamento de Tarefas

**Projeto de pesquisa:** Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial
**Versão:** **v1.0 (CONGELADA)** · **Data:** 2026-09-05 · **Status:** APROVADA pelo autor — documento imutável para o experimento

> Este é o **ÚNICO documento entregue aos agentes** no experimento (desenho G4). O oráculo independente (suíte de testes) é construído a partir desta especificação e **permanece privado**, fora do alcance dos agentes. Requisitos estão numerados (FR/NFR) para permitir rastreabilidade de índice de defectos.

---

## 1. Visão geral do produto

Uma **API REST para gerenciamento de tarefas** com autenticação de usuários. Cada usuário gerencia suas próprias tarefas; um usuário **admin** pode gerenciar qualquer tarefa. A entrega deve ser um **sistema completo e executável**, com banco de dados **PostgreSQL**, seguindo a stack definida no projeto.

## 2. Stack técnica e restrições

| Item | Restrição |
|---|---|
| Linguagem | Python 3.11+ |
| Framework | FastAPI |
| Banco | PostgreSQL (via ORM; migrações versionadas — ex.: Alembic) |
| Autenticação | JWT (Bearer) |
| Senhas | Hash forte (bcrypt ou argon2) — nunca texto puro |
| Rodar | `docker compose up` deve subir banco + aplicação (RNF1) |
| Dependências | Versões pinadas; arquivo de aplicação (`requirements.txt` ou `pyproject.toml` + lock) |
| Configuração | Variáveis de ambiente (nunca segredos hardcoded) |
| Testes | Suíte automatizada que acompanha a entrega (RNF5) |

---

## 3. Modelo de dados

### Entidade `User`

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | gerado automaticamente |
| name | string | 1–100 caracteres, obrigatório |
| email | string | e-mail válido, normalizado em minúsculas, **único** |
| password | string | senha com hash; mínimo 8 caracteres |
| role | enum | `user` \| `admin` |
| created_at | datetime | UTC, ISO 8601 |

### Entidade `Task`

| Campo | Tipo | Regra |
|---|---|---|
| id | UUID | gerado automaticamente |
| title | string | 1–140 caracteres, obrigatório |
| description | string | 0–2000 caracteres, opcional (ausente = `null`/omitido) |
| priority | enum | `low` \| `medium` \| `high`; default `low` |
| status | enum | `pending` \| `in_progress` \| `completed`; default `pending` |
| due_date | date | ISO 8601 `YYYY-MM-DD`; opcional; **hoje ou futuro** (UTC) |
| owner_id | UUID | referência ao usuário dono |
| created_at | datetime | UTC, ISO 8601 |
| updated_at | datetime | UTC, ISO 8601; atualizado em qualquer modificação |

**Regras de negócio transversais:**
- e-mail é único (duplicado → **409 Conflict**).
- `due_date` no passado → **422**.
- Campos de enum fora dos valores definidos → **422**.
- Modificação/exclusão apenas pelo **dono** ou por **admin** → caso contrário **403**.

---

## 4. Requisitos funcionais (FR)

### FR1 — Registro e login de usuários

**Roteiros:**
- `POST /auth/register` — corpo `{ "name": string, "email": string, "password": string }`.
  - Sucesso → **201** com perfil do usuário (`id`, `name`, `email`, `role`, `created_at`) — **sem senha**. `role` default = `user`.
  - E-mail inválido → **422**. Senha < 8 → **422**. E-mail já cadastrado → **409**.
- `POST /auth/login` — corpo `{ "email": string, "password": string }`.
  - Sucesso → **200** com `{ "access_token", "token_type": "bearer", "expires_in", "user": {...} }`.
  - Credenciais inválidas (e-mail inexistente **ou** senha errada) → **401** com mensagem genérica (`Invalid credentials`).
- `GET /auth/me` — cabeçalho `Authorization: Bearer <token>`.
  - Sucesso → **200** perfil do usuário autenticado.
  - Token ausente/expirado/ inválido → **401**.

**Casos de aceite (resumo):**
- Dado senha com hash, a resposta não contém a senha.
- Dado token expirado ou adulterado, toda rota autenticada retorna **401**.

### FR2 — CRUD de tarefas

| Rota | Autenticação | Permissão | Sucesso | Erros |
|---|---|---|---|---|
| `POST /tasks` | sim | usuário autenticado (dono = autor) | **201** | 401, 422 |
| `GET /tasks` | sim | lista **somente as próprias** (admin: todas) | **200** | 401 |
| `GET /tasks/{id}` | sim | dono ou admin | **200** | 401, 403, 404 |
| `PUT /tasks/{id}` | sim | dono ou admin | **200** | 401, 403, 404, 422 |
| `PATCH /tasks/{id}` | sim | dono ou admin | **200** | 401, 403, 404, 422 |
| `DELETE /tasks/{id}` | sim | dono ou admin | **204** | 401, 403, 404 |

- `POST /tasks` corpo: `{ "title": obrigatório, "description"?, "priority"?, "status"?, "due_date"? }` (valores default conforme modelo).
- `PUT` deve aceitar **todos** os campos editáveis (reposição completa).
- `PATCH` deve aceitar **subconjunto** (atualização parcial).
- Tarefa inexistente → **404** em `GET/PUT/PATCH/DELETE`.

**Objeto de resposta (Task):**

```json
{
  "id": "uuid",
  "title": "string",
  "description": "string | null",
  "priority": "low|medium|high",
  "status": "pending|in_progress|completed",
  "due_date": "YYYY-MM-DD | null",
  "created_at": "ISO 8601 UTC",
  "updated_at": "ISO 8601 UTC",
  "owner": { "id": "uuid", "name": "string", "email": "string" }
}
```

### FR3 — Regras de permissão

- Usuário **não-admin** e **não-dono** ao acessar `GET/PUT/PATCH/DELETE /tasks/{id}` → **403**.
- Admin pode ler, editar e excluir tarefa de qualquer usuário.
- Listagem (`GET /tasks`) nunca expõe tarefas de outros usuários, a não ser que o solicitante seja **admin** (admin vê todas — o objeto pode incluir a informação do dono).

**Caso de aceite:** Dado usuário A dono da tarefa T e usuário B comum, `PATCH /tasks/{T}/status` por B → **403**.

### FR4 — Filtros e paginação

Query params de `GET /tasks`:

| Parâmetro | Filtra por | Observação |
|---|---|---|
| `status` | status exato | enum |
| `priority` | prioridade exata | enum |
| `due_date_from` | `due_date >= data` | `YYYY-MM-DD` |
| `due_date_to` | `due_date <= data` | `YYYY-MM-DD` |
| `q` | título contém (case-insensitive) | texto parcial |
| `page` | página (≥1) | default 1 |
| `page_size` | itens por página (1–100) | default 20 |

- Combinações de filtros: **todos aplicados em conjunto** (AND).
- Resposta: `{ "items": [Task...], "total": int, "page": int, "page_size": int }`.
- Ordenação default: `created_at` decrescente.
- `page` ou `page_size` fora do intervalo → **422**.

**Caso de aceite:** Dado 25 tarefas (statuses mistos), `GET /tasks?status=pending&page=1&page_size=10` → `total` de pendentes e 10 itens.

### FR5 — Validação de entrada

| Regra | Resposta |
|---|---|
| `title` ausente ou vazio | **422** |
| `title` > 140 caracteres | **422** |
| `description` > 2000 caracteres | **422** |
| `email` com formato inválido | **422** |
| `password` < 8 | **422** |
| `due_date` inválido (formato) | **422** |
| `due_date` no passado | **422** |
| `status`/`priority` fora do enum | **422** |
| `page`/`page_size` fora do intervalo | **422** |
| Parâmetros desconhecidos no corpo de `POST/PUT/PATCH` | **422** (rejeição por schema) |

- Valores de borda e tipos errados (ex.: `"abc"` em numérico, `null` em campo obrigatório) devem ser rejeitados de forma **consistente** com **422** e mensagem de erro estruturada.

### FR6 — Tratamento de erros padronizado

- Resposta de erro sempre JSON, formato compatível com FastAPI/Pydantic (campo `detail`):
  - Erro de validação (422): `detail` com lista de problemas por campo.
  - Erro de negócio (401/403/404/409): `detail` com mensagem textual.
- Sem stack traces ou informações internas em respostas de erro.
- Métodos não suportados em rota existente → **405**.

### FR7 — Persistência e migrações

- Schema criado por **migrações versionadas** (ex.: Alembic) e aplicado automaticamente no boot do contêiner.
- O banco deve conter as entidades `users` e `tasks` com as constraints de unicidade (e-mail) e integridade referencial (`owner_id` → `users.id`).
- Reinício do contêiner não perde dados (volume persistente).

### FR8 — Testes automatizados acompanhando a entrega

- Suíte executável documentada (comando único).
- Deve cobrir pelo menos: fluxo completo de registro → login → criar → listar → editar → excluir; e casos negativos básicos.
- Testes não podem depender de informações/estado pré-populados manualmente (use fixtures/setup).

---

## 5. Requisitos não funcionais (NFR)

### NFR1 — Reproducibilidade/executabilidade (âncora F02)

- `docker compose up` levanta aplicação + PostgreSQL sem passos manuais adicionais.
- `README.md` com: pré-requisitos, passo a passo, portas, e como executar a suíte de testes.
- Arquivo `.env.example` documentando todas as variáveis (sem valores sensíveis reais).
- Aplicação responde no endpoint `/health` (GET) → **200 `{"status":"ok"}`** sem autenticação.

### NFR2 — Segurança (âncora E01–E03; CWE/OWASP)

- Senhas somente com hash; **nunca** em texto puro ou em resposta.
- JWT assinado com segredo de configuração; expiração presente (ex.: 60 min).
- **Sem** secretos hardcoded/commitados (DB password, JWT secret, etc.).
- Acesso a dados somente via ORM/parametrização (resistência a SQL injection).
- Dependências: auditoria sem vulnerabilidades **conhecidas** (ex.: `pip-audit`) no momento da avaliação.
- Erro 401/403/404 não revelam existência de recurso de forma inconsistente em cenário simples de autorização (não vazar dados de outros usuários).

### NFR3 — Manutenibilidade (âncora D04/ISO 25010; D05)

- Código organizado em módulos com responsabilidade clara (rotas, schemas, serviços, modelos) — sem camadas gigantes com lógica misturada.
- Nomenclatura consistente (PEP 8); sem código morto óbvio (variáveis/funções sem uso).
- Duplicação de lógica evitada (extração em funções/reutilização).
- Migrações e configuração centralizadas e legíveis.
- Avaliação de referência: lint sem erros bloqueantes (ex.: `ruff`) e complexidade/duplicação sem alertas críticos no SonarQube.

### NFR4 — Performance básica (âmbito D04)

- `GET /tasks` com 1.000 tarefas na base de um usuário e paginação default responde em **< 500 ms** (máquina de referência, sem cache pré-aquecido).
- **Sem** N+1 evidente ao listar tarefas com dono (carregamento eficiente da relação).

### NFR5 — Testabilidade (âncora C05/C06)

- A suíte entregue deve **executar** no ambiente limpo (sem internet adicional além das dependências declaradas).
- Testes não podem exigir estado global/ordem fixa entre si (isolamento).

---

## 6. Formato da entrega esperado

Artefatos que o agente deve produzir (estrutura de referência):

```
/ (raiz do projeto)
├── README.md            # instruções de execução e testes
├── .env.example
├── docker-compose.yml
├── requirements.txt (ou pyproject.toml + lock)
├── migrations/          # migrações versionadas
├── app/                 # código da aplicação
│   ├── main.py          # entrypoint FastAPI
│   ├── models/ · schemas/ · routers/ · services/
│   └── config.py        # leitura de env
└── tests/               # suíte automatizada
```

> A estrutura interna é livre; os requisitos **comportamentais** (seções 4 e 5) são o critério de aceite. O documento desta especificação deve ser usado pelo agente como requisito único.

---

## 7. Casos de aceite consolidados (visão do oráculo)

| # | Cenário | Método/Path | Esperado |
|---|---|---|---|
| C01 | Registro válido | POST /auth/register | 201, sem senha na resposta |
| C02 | E-mail duplicado | POST /auth/register | 409 |
| C03 | Login válido | POST /auth/login | 200 + token |
| C04 | Login inválido | POST /auth/login | 401 genérico |
| C05 | Rota autenticada sem token | GET /auth/me | 401 |
| C06 | Criar tarefa válida | POST /tasks | 201 |
| C07 | Título vazio | POST /tasks | 422 |
| C08 | due_date no passado | POST /tasks | 422 |
| C09 | Listar minhas tarefas | GET /tasks | 200, só as minhas |
| C10 | Ver tarefa de outro (não-admin) | GET /tasks/{id} | 403 |
| C11 | Editar tarefa de outro (não-admin) | PATCH /tasks/{id} | 403 |
| C12 | Admin edita tarefa de outro | PATCH /tasks/{id} | 200 |
| C13 | Filtro por status + página | GET /tasks?status=..&page=.. | 200, total correto |
| C14 | Tarefa inexistente | GET /tasks/{uuid-inexistente} | 404 |
| C15 | Excluir e confirmar ausência | DELETE → GET | 204 → 404 |
| C16 | Fluxo completo (A→F) | register→login→create→list→edit→delete | tudo OK |
| C17 | Health sem auth | GET /health | 200 |

---

## 8. Decisões aprovadas (registro do congelamento)

Todas aprovadas pelo autor em 2026-09-05. Estes valores são **obrigatórios** na implementação e no oráculo.

| # | Decisão | Valor congelado |
|---|---|---|
| D1 | Criação de admin | Via variável de ambiente `ADMIN_EMAIL` (e-mail cadastrado vira admin no registro) |
| D2 | Formato de erro | `detail` no padrão FastAPI/Pydantic |
| D3 | Expiração do token | 60 minutos |
| D4 | Status válidos | `pending`, `in_progress`, `completed` |
| D5 | Prioridades | `low`, `medium`, `high` |
| D6 | `due_date` passado | Rejeitar com 422 |
| D7 | Lista admin | Admin vê todas as tarefas (com o dono no objeto) |

> **Congelamento:** a partir desta versão o documento é imutável para o experimento. Qualquer alteração exige nova versão (v1.1+, ex.: após calibração do piloto) e revalidação dos artefatos derivados (oráculo).

---

## 9. Rastreabilidade do experimento

- FR1–FR8 → RQ1 (funcional), matriz de defeitos e oráculo.
- NFR1 → RQ7 (reprodutibilidade); NFR2 → RQ5 (segurança); NFR3 → RQ5 (manutenibilidade); NFR4 → RQ5; NFR5 → RQ6 (testes do próprio agente, H3).
- Validações (FR5) e cenários negativos → gap G5 (corner cases que LLMs omitem, C06).

---

*Especificação controlada **v1.0 congelada** — aprovada em 2026-09-05. Usado para construir o oráculo privado e servir de prompt único aos agentes. Referência de desenho: `metodologia-experimental.md`.*