# Banco ABC - Roteiro de Testes

**Empresa:** Banco ABC S.A. (fictício)
**Sistema:** Internet Banking
**QA responsável:** __________
**Data:** __________

## Credenciais demo informadas no sistema
- Agência: `0001` | Conta: `12345-6` | Senha: `qatest123`

---

## Casos de Teste

### CT-01 - Login com campos vazios
| Campo | Valor |
|---|---|
| Pré-condição | Tela de login |
| Passos | Clique em "Entrar" sem preencher nada |
| Resultado esperado | Mensagem "Preencha todos os campos" |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-02 - Login com senha curta
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Agência 0001, Conta 12345-6, senha "123" |
| Resultado esperado | Mensagem de senha muito curta, sem acesso |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-03 - Login com as credenciais demo
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Digite agência 0001, conta 12345-6 e senha qatest123 |
| Resultado esperado | Acesso liberado para a conta. **Atente** para o campo de senha (verifique o atributo maxlength e se a senha demo tem 9 caracteres) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-04 - Login com credenciais erradas
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Agência 9999, conta 99999-9, senha 12345678 |
| Resultado esperado | Mensagem de acesso negado (se a senha usada for diferente da senha "correta", o acesso deve ser negado) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-05 - Depósito com valor válido
| Campo | Valor |
|---|---|
| Pré-condição | Logado, saldo R$ 5.000,00 |
| Passos | Deposite R$ 500,00 |
| Resultado esperado | Saldo = R$ 5.500,00. Extrato registra depósito |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-06 - Depósito com vírgula (formato brasileiro)
| Campo | Valor |
|---|---|
| Pré-condição | Logado |
| Passos | No campo de depósito digite **1000,50** (usando vírgula) e confirme |
| Resultado esperado | Depósito de R$ 1.000,50 (valores com centavos devem ser preservados) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-07 - Depósito acima do limite
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Deposite R$ 10.001,00 |
| Resultado esperado | Mensagem de limite excedido (máximo R$ 10.000,00) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-08 - Transferência normal (sem taxa)
| Campo | Valor |
|---|---|
| Pré-condição | Saldo suficiente |
| Passos | Transfira R$ 500,00 para a conta 53421-0 |
| Resultado esperado | Saldo debitado em R$ 500,00. Extrato registra transferência |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-09 - Transferência com taxa de 2% (acima de R$ 1.000)
| Campo | Valor |
|---|---|
| Pré-condição | Saldo suficiente |
| Passos | Transfira R$ 2.000,00 para 65432-1 |
| Resultado esperado | Débito total = R$ 2.040,00 (valor + 2%). Taxa cobrada do REMETENTE. Mensagem informa a taxa |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-10 - Transferência para a própria conta
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Transfira R$ 100,00 para a conta 12345-6 (a mesma) |
| Resultado esperado | Rejeitado com mensagem clara |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-11 - Transferência com saldo insuficiente
| Campo | Valor |
|---|---|
| Pré-condição | Anote o saldo atual |
| Passos | Tente transferir um valor maior que o saldo + taxa |
| Resultado esperado | Rejeitado, saldo permanece intacto |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-12 - Transferência para conta inexistente
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Transfira R$ 50,00 para 88888-8 (não cadastrada) |
| Resultado esperado | Mensagem "conta não encontrada" e NENHUM débito |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-13 - Transferência para conta com formato inválido
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Transfira para os formatos: 123, 12345, 123456, 12-34, abcde-1 |
| Resultado esperado | Todos rejeitados com mensagem de formato |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-14 - Transferência com vírgula
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | No valor, digite 1200,50 (vírgula) |
| Resultado esperado | Valor tratado como R$ 1.200,50 (e taxa de 2% aplicada) |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-15 - Limite da taxa (exatamente R$ 1.000,00)
| Campo | Valor |
|---|---|
| Pré-condição | — |
| Passos | Transfira exatamente R$ 1.000,00 |
| Resultado esperado | Sem taxa (regra só vale para ACIMA de R$ 1.000). Débito exato R$ 1.000,00 |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-16 - Botão ocultar saldo
| Campo | Valor |
|---|---|
| Pré-condição | Logado |
| Passos | Clique em "Ocultar" e depois novamente para mostrar |
| Resultado esperado | Saldo some (R$ ••••) e volta corretamente |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

### CT-17 - Extrato após operações
| Campo | Valor |
|---|---|
| Pré-condição | Execute depósito e transferência |
| Passos | Verifique a coluna "Saldo após" de cada linha |
| Resultado esperado | Saldo após de cada linha é consistente com a sequência de operações |

Resultado obtido:
Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Login valida todos os campos e credenciais
- [ ] Senha demo informada funciona como documentado
- [ ] Depósito preserva centavos (vírgula ou ponto)
- [ ] Taxa de 2% calculada corretamente e informada
- [ ] Transferência para conta inexistente NÃO debita
- [ ] Saldo nunca negativo
- [ ] Extrato coerente com as operações realizadas

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |
| 2 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |