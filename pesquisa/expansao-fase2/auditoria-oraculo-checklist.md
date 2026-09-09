# Auditoria de cobertura do oráculo — checklist (template)

> **Objetivo:** revisar a suíte oráculo (v1.0, 81 testes) contra a
> especificação FR1–FR8 + NFR **antes** da coleta da Fase 2. Preencher as
> colunas "Cobertura atual" e "Gap/Ação". Se novos testes forem criados,
> eles formam a **v1.1, aplicada somente às entregas novas** (versão
> registrada por entrega; sem misturar comparações entre versões).
> **Oráculo é privado** — este template contém apenas a estrutura da
> auditoria, nenhum teste interno.

## 1. Funcionais FR1–FR8 (camada pytest)

| Requisito | Cobertura atual (nº testes aprox.) | Gap identificado | Ação (manter/adicionar) |
|---|---|---|---|
| FR1 registro/login (hash + JWT) | `[preencher]` | `[preencher]` | `[preencher]` |
| FR2 task CRUD | `[preencher]` | `[preencher]` | `[preencher]` |
| FR3 permissões owner/admin | `[preencher]` | `[preencher]` | `[preencher]` |
| FR4 filtros/paginação | `[preencher]` | `[preencher]` | `[preencher]` |
| FR5 validação de entradas | `[preencher]` | `[preencher]` | `[preencher]` |
| FR6 erros padronizados | `[preencher]` | `[preencher]` | `[preencher]` |
| FR7 PostgreSQL + migrações | `[preencher]` | `[preencher]` | `[preencher]` |
| FR8 testes automatizados na entrega | `[preencher]` | `[preencher]` | `[preencher]` |

## 2. Negativos / borda (camada negativa)

| Caso | Coberto? | Gap/Ação |
|---|---|---|
| Entradas extremas (strings vazias/gigantes, IDs inválidos) | `[preencher]` | `[preencher]` |
| Permissões cruzadas (usuário A × recurso de B) | `[preencher]` | `[preencher]` |
| JWT expirado / malformado / ausente | `[preencher]` | `[preencher]` |
| Paginação com valores extremos (page=0, limit gigante) | `[preencher]` | `[preencher]` |
| Concorrência (criação simultânea — race conditions) | `[preencher]` | `[preencher]` |
| Valores especiais (None, null, tipos trocados) | `[preencher]` | `[preencher]` |

## 3. Não-funcionais (camadas segurança/estrutural)

| NFR | Ferramenta/camada | Cobertura atual | Gap/Ação |
|---|---|---|---|
| Segurança (bandit, pip-audit) | `[preencher]` | `[preencher]` | `[preencher]` |
| Estrutural (ruff, radon) | `[preencher]` | `[preencher]` | `[preencher]` |
| Manutenibilidade (code smells) | `[preencher]` | `[preencher]` | `[preencher]` |
| Reprodutibilidade (ambiente limpo) | `[preencher]` | `[preencher]` | `[preencher]` |
| Performance básica | `[preencher]` | `[preencher]` | `[preencher]` |

## 4. Decisão de versionamento

- [ ] Nenhum gap relevante → manter **v1.0** para toda a Fase 2.
- [ ] Gaps relevantes → criar **v1.1** com os testes adicionados listados
      abaixo; v1.0 avalía as 12 entregas antigas, v1.1 avalia só as novas.

**Testes adicionados na v1.1 (se houver):**

| ID novo teste | Requisito coberto | Data de criação |
|---|---|---|
| `[preencher]` | `[preencher]` | `[preencher]` |

## 5. Assinatura da auditoria

- Auditor: `[nome]` · Data: `[aaaa-mm-dd]` · Suíte avaliada: `[v1.0 / v1.1]`
- Resultado arquivado em: `[caminho do repo privado]`
