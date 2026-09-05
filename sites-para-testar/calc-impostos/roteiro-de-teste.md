# Contabilidade KM - Roteiro de Testes (Calculadora de Impostos)

**Empresa:** Contabilidade KM (fictícia)
**Sistema:** Calculadora de IRPF/INSS
**QA responsável:** __________
**Data:** __________

**Referência legal para conferência: tabela IRPF mensal 2024/2025 e INSS 2024 (teto R$ 7.786,02).**

---

## Casos de Teste

### CT-01 - Renda vazia / zero
| Campo | Valor |
|---|---|
| Passos | Deixe renda em branco e calcule; depois coloque 0 |
| Resultado esperado | Calcula normalmente: 0 de renda = INSS 0, IR isento, CPMF 0, líquido 0. Sem erro |

Status: [ ] Passou [ ] Falhou

### CT-02 - Renda negativa
| Campo | Valor |
|---|---|
| Passos | Renda **-500** |
| Resultado esperado | Erro claro, sem cálculo |

Status: [ ] Passou [ ] Falhou

### CT-03 - Dependentes inválidos
| Campo | Valor |
|---|---|
| Passos | Dependentes **-1** |
| Resultado esperado | Erro (número inteiro >= 0) |

Status: [ ] Passou [ ] Falhou

### CT-04 - Isento (até R$ 2.259,20)
| Campo | Valor |
|---|---|
| Passos | Renda 2.000,00, 0 dependentes |
| Resultado esperado | INSS = 150,00 (7,5% de 2.000). Base IR = 1.850,00 -> alíquota 0%. Líquido = 2.000 - 150 - 0 - CPMF(7,60) = **R$ 1.842,40** |

Status: [ ] Passou [ ] Falhou

### CT-05 - Limite exato da isenção (R$ 2.259,20)
| Campo | Valor |
|---|---|
| Passos | Renda 2.259,20, 0 dependentes |
| Resultado esperado | INSS 169,44 (7,5% até 1.412 + 9% no restante). Base IR = 2.089,76 -> isento (faixa 1). Confirmar com a calculadora oficial |

Status: [ ] Passou [ ] Falhou

### CT-06 - Faixa de 7,5% (ex.: R$ 2.400,00)
| Campo | Valor |
|---|---|
| Passos | Renda 2.400,0 |
| Resultado esperado | Conferir cálculo na tabela oficial (7,5% com dedução 169,44) |

Status: [ ] Passou [ ] Falhou

### CT-07 - Faixa de 27,5% (R$ 5.000,00)
| Campo | Valor |
|---|---|
| Passos | Renda 5.000, 0 dependentes |
| Resultado esperado | INSS = 105,90 + 112,92 + 160,00 + 139,99 = R$ 528,81 (até 4.000,03) *(confira a tabela 2024)*. Base IR = 5.000 - 528,81 = 4.471,19 -> cai na faixa de **22,5%**? Não: 4.471,19 < 4.664,68 -> 22,5% (dedução 662,77). IR = 4.471,19*0,225 - 662,77 = R$ 343,25. **Confira todos os valores com fonte oficial** |
| Resultado obtido:  |  |

Status: [ ] Passou [ ] Falhou

### CT-08 - INSS com salário ACIMA do teto (R$ 8.000,00)
| Campo | Valor |
|---|---|
| Passos | Renda 8.000, 0 dependentes |
| Resultado esperado | A contribuição INSS NÃO pode passar do teto calculado (máximo sobre R$ 7.786,02). Conferir valor exibido |

Status: [ ] Passou [ ] Falhou

### CT-09 - Desconto de dependentes
| Campo | Valor |
|---|---|
| Passos | Renda 3.000, 1 dependente (dedução 189,59) |
| Resultado esperado | Base = salário - INSS - 189,59 |

Status: [ ] Passou [ ] Falhou

### CT-10 - Alíquota e dedução exibidas por faixa
| Campo | Valor |
|---|---|
| Passos | Renda 5.000 (27,5%?) e renda 3.000 (15%) |
| Resultado esperado | A alíquota e a parcela dedutível exibidas batem com a tabela oficial da base de cálculo efetiva (NÃO do salário bruto) |

Status: [ ] Passou [ ] Falhou

### CT-11 - Existência da contribuição "CPMF / Contrib."
| Campo | Valor |
|---|---|
| Passos | Procure na legislação atual o que é "CPMF" |
| Resultado esperado | **Verificar requisito/pergunta-chave:** O sistema desconta 0,38% (CPMF) de todo salário bruto. A legislação brasileira **extinguiu o CPMF em 2007**. A presença desse desconto é suspeita e deve ser reportada como BUG de regra de negócio |

Status: [ ] Passou [ ] Falhou

### CT-12 - Arredondamento
| Campo | Valor |
|---|---|
| Passos | Renda 2.500,00 e 2.500,01 |
| Resultado esperado | Diferenças de centavo coerentes; valores exibidos com 2 casas sempre |

Status: [ ] Passou [ ] Falhou

---

## Checklist

- [ ] Validação de entrada (vazia, negativa, inválida)
- [ ] Faixas IRPF e deduções corretas (conferidas com fonte oficial)
- [ ] INSS progressivo e teto respeitado
- [ ] Desconto de dependentes correto
- [ ] **CPMF questionado** (legislação)
- [ ] Arredondamento de centavos consistente

---

## Bugs encontrados (resumo)

| # | Descrição | Passos | Esperado | Obtido | Severidade |
|---|---|---|---|---|---|
| 1 |  |  |  |  | [ ] Alta [ ] Média [ ] Baixa |