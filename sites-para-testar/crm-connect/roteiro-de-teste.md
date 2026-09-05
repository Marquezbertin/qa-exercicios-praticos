# CRM Connect - Roteiro de Testes

**Empresa:** CRM Connect (fictício)
**Sistema:** Gestão de clientes (CRUD)
**QA responsável:** __________
**Data:** __________

---

## Casos de Teste

### CT-01 - Cadastrar cliente válido
| Campo | Valor |
|---|---|
| Passos | Nome "João Pereira", e-mail "joao@empresa.com", fone "(11) 98765-4321", categoria Normal |
| Resultado esperado | Mensagem de sucesso; cliente aparece na tabela; contador do header aumenta |

Status: [ ] Passou [ ] Falhou

### CT-02 - Cadastro com nome curto
| Campo | Valor |
|---|---|
| Passos | Nome "Jo" |
| Resultado esperado | Erro "nome deve ter pelo menos 3 caracteres" |

Status: [ ] Passou [ ] Falhou

### CT-03 - E-mail inválido
| Campo | Valor |
|---|---|
| Passos | E-mail "joao@" e "joao@site" |
| Resultado esperado | Erro de e-mail inválido |

Status: [ ] Passou [ ] Falhou

### CT-04 - Telefone obrigatório e formato
| Campo | Valor |
|---|---|
| Passos | (a) Telefone vazio; (b) Telefone "987654321" (sem DDD); (c) "(11) 98765-4321" |
| Resultado esperado | (a) erro obrigatório; (b) erro de formato; (c) salva |

Status: [ ] Passou [ ] Falhou

### CT-05 - E-mail duplicado (exatamente igual)
| Campo | Valor |
|---|---|
| Passos | Cadastre ana@souza.com (já existe no banco inicial) |
| Resultado esperado | Erro "já existe um cliente com este e-mail" |

Status: [ ] Passou [ ] Falhou

### CT-06 - E-mail duplicado (variação de MAIÚSCULAS)
| Campo | Valor |
|---|---|
| Passos | Cadastre `ANA@SOUZA.COM` |
| Resultado esperado | Erro (e-mail duplicado deve ignorar maiúsculas) |

Status: [ ] Passou [ ] Falhou

### CT-07 - Busca por nome
| Campo | Valor |
|---|---|
| Passos | Digite "ana" na busca |
| Resultado esperado | Mostra somente a Ana |

Status: [ ] Passou [ ] Falhou

### CT-08 - Busca deve ignorar acentos
| Campo | Valor |
|---|---|
| Pré-condição | Cadastre o cliente "João Carlos" (fone válido, e-mail joao@c.com) |
| Passos | Busque por "joao" (sem acento) |
| Resultado esperado | O cliente "João Carlos" deve aparecer (busca não distingue acento) |

Status: [ ] Passou [ ] Falhou

### CT-09 - Busca sem resultados
| Campo | Valor |
|---|---|
| Passos | Busque "zzzz" |
| Resultado esperado | Mensagem "Nenhum cliente encontrado" |

Status: [ ] Passou [ ] Falhou

### CT-10 - Editar cliente
| Campo | Valor |
|---|---|
| Passos | Clique em "Editar" na Ana; altere o telefone para "(11) 90000-0000"; clique em "Atualizar" |
| Resultado esperado | Telefone atualizado na tabela; mensagem de sucesso; formulário volta ao modo novo |

Status: [ ] Passou [ ] Falhou

### CT-11 - Excluir cliente
| Campo | Valor |
|---|---|
| Passos | Clique em "Excluir" no Bruno; confirme o diálogo |
| Resultado esperado | Bruno removido da lista; contador decrementa |

Status: [ ] Passou [ ] Falhou

### CT-12 - Excluir cliente e DEPOIS salvar a edição pendente dele
| Campo | Valor |
|---|---|
| Passos | 1. Clique em "Editar" no Bruno (continua aberto o formulário de edição). 2. No formulário aberto, não salve ainda. 3. Clique em "Excluir" na linha do Bruno na tabela e confirme. 4. Agora clique em "Atualizar" no formulário ainda aberto |
| Resultado esperado | Mensagem de erro (cliente não existe mais) ou nenhuma ação; NUNCA mensagem de sucesso enganosa |

Status: [ ] Passou [ ] Falhou

### CT-13 - Cancelamento de edição
| Campo | Valor |
|---|---|
| Passos | Edite um cliente, depois clique em "+ Novo" (ou "Novo") para descartar a edição |
| Resultado esperado | Formulário limpo, título "Novo Cliente", nenhuma alteração salva |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Validações de nome, e-mail, telefone funcionam
- [ ] E-mail único (independente de maiúsculas)
- [ ] Busca correta (incluindo acentos)
- [ ] Edição persiste e volta ao estado limpo
- [ ] Exclusão com confirmação e sem mensagens enganosas
- [ ] Contador de clientes consistente

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |