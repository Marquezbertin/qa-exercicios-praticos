# Portal Cliente - Roteiro de Testes

**Empresa:** Portal Cliente (fictício)
**Sistema:** Cadastro e login
**QA responsável:** __________
**Data:** __________

---

## Casos de Teste

### CT-01 - Cadastro com todos os campos válidos
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Nome "Maria da Silva", CPF "529.982.247-25", e-mail "maria@email.com", senha "abc123", confirmar "abc123" |
| Resultado esperado | Mensagem de sucesso; conta criada |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-02 - Cadastro com nome curto
| Campo | Valor |
|---|---|
| Passos | Nome "Jo" com o resto válido |
| Resultado esperado | Erro "nome deve ter pelo menos 3 caracteres" |

Status: [ ] Passou [ ] Falhou

### CT-03 - Cadastro com CPF inválido
| Campo | Valor |
|---|---|
| Passos | Teste os CPFs: `111.111.111-11`, `123.456.789-00`, `5299822` (incompleto) |
| Resultado esperado | Todos rejeitados (dígitos verificadores) |

Status: [ ] Passou [ ] Falhou

### CT-04 - Cadastro com CPF válido
| Campo | Valor |
|---|---|
| Passos | `529.982.247-25` e `123.456.789-09` |
| Resultado esperado | Ambos aceitos |

Status: [ ] Passou [ ] Falhou

### CT-05 - Cadastro com e-mail inválido
| Campo | Valor |
|---|---|
| Passos | `maria@`, `@email.com`, `maria@site`, `maria email.com` |
| Resultado esperado | Todos rejeitados |

Status: [ ] Passou [ ] Falhou

### CT-06 - Senha sem letra OU sem número
| Campo | Valor |
|---|---|
| Passos | Senha `123456` (só números) e `abcdef` (só letras) |
| Resultado esperado | Rejeitadas (regra: letra e número) |

Status: [ ] Passou [ ] Falhou

### CT-07 - Confirmação de senha diferente
| Campo | Valor |
|---|---|
| Passos | Senha `abc123`, confirme `abc124` |
| Resultado esperado | Erro "as senhas não coincidem" |

Status: [ ] Passou [ ] Falhou

### CT-08 - CADASTRO do MESMO CPF duas vezes (e-mails diferentes)
| Campo | Valor |
|---|---|
| Pré-condição | Cadastre o usuário do CT-01 (CPF 529.982.247-25) |
| Passos | Cadastre novamente com CPF `529.982.247-25`, mas e-mail `outra@email.com` |
| Resultado esperado | Rejeitado -- CPF deve ser ÚNICO no sistema |

Status: [ ] Passou [ ] Falhou

### CT-09 - Login com senha correta (após cadastrar)
| Campo | Valor |
|---|---|
| Pré-condição | Conta criada no CT-01 |
| Passos | Login com maria@email.com / abc123 |
| Resultado esperado | Mensagem de boas-vindas nomeando o usuário |

Status: [ ] Passou [ ] Falhou

### CT-10 - Login com senha errada
| Campo | Valor |
|---|---|
| Passos | maria@email.com / senha "errada1" |
| Resultado esperado | Erro "e-mail ou senha incorretos" |

Status: [ ] Passou [ ] Falhou

### CT-11 - Login variando MAIÚSCULAS no e-mail
| Campo | Valor |
|---|---|
| Passos | Cadastre maria@email.com. Depois faça login com `MARIA@email.com` e `Maria@Email.com` |
| Resultado esperado | Login deve funcionar (e-mail não deve ser case-sensitive) |

Status: [ ] Passou [ ] Falhou

### CT-12 - Cadastro duplicado variando MAIÚSCULAS no e-mail
| Campo | Valor |
|---|---|
| Passos | Cadastre `ana@email.com`. Depois cadastre `ANA@email.com` com outro CPF |
| Resultado esperado | Rejeitado (mesmo e-mail, independente de maiúsculas) |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] CPF validado com dígitos verificadores
- [ ] CPF único no cadastro
- [ ] E-mail validado e ÚNICO (sem diferenciar maiúsculas)
- [ ] Senha atende à política (min 6, letra e número)
- [ ] Confirmação de senha consistente
- [ ] Login funciona com conta criada
- [ ] Login com senha errada é bloqueado

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |