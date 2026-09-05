# Perguntas e Respostas - Entrevistas de QA

Banco de perguntas reais de entrevistas de QA (manual + automação), com gabarito e dicas para responder bem.

---

## 🟢 Nível 1 - Conceitos básicos

### Q1. O que é teste manual e teste automatizado?
**Resposta:** Teste manual é executado por um humano seguindo passos para verificar o comportamento do sistema (exploratório, UX, casos isolados). Teste automatizado usa ferramentas (Selenium, Playwright, Cypress, Postman, etc.) para executar casos repetidamente, ideal para regressão e frequência alta. O ideal é usar ambos: automação para regressão, manual para exploração e UX.

### Q2. Qual a diferença entre erro, defeito e falha?
| Termo | Definição |
|---|---|
| **Erro** | Ação humana que produz resultado incorreto (o programador escreveu errado). |
| **Defeito (bug)** | Resultado do erro no artefato (linha de código, config, documento). |
| **Falha** | Comportamento incorreto observável quando o defeito é executado. |

Ex.: o dev esquece de validar CPF (erro) -> código sem validação (defeito) -> usuário cadastra CPF inválido (falha).

### Q3. Diferencie verificação e validação.
**Resposta:** Verificação = "estamos construindo o produto CORRETamente?" (checa specs, revisão estática). Validação = "construímos o produto CERTO?" (teste dinâmico contra necessidade do cliente).

### Q4. O que é smoke test, regression test e teste de aceitação?
**Smoke:** bateria rápida que confirma que as funções principais funcionam após um build (porta de entrada). **Regressão:** repetir testes existentes para garantir que mudanças não quebram e funcionalidades anteriores. **Aceitação:** validar com o cliente que o software atende aos critérios antes do lançamento.

### Q5. O que é caso de teste? Defina os campos básicos.
**Resposta:** Conjunto de ações/condições para validar um requisito. Campos: ID, título, pré-condições, passos, dados, resultado esperado, resultado obtido, status, prioridade, autor. (Veja `modelos-templates/test-case.md`.)

---

## 🟡 Nível 2 - Técnicas e análise

### Q6. O que é particionamento de equivalência? Dê um exemplo.
**Resposta:** Dividir o domínio de entrada em classes onde o comportamento é o mesmo. Testar 1 representante de cada classe.
**Exemplo (idade de cadastro 18–120):**
- Classe válida: [18–120] -> testar 25
- Classe inválida baixa: [-inf–17] -> testar 10
- Classe inválida alta: [121–+inf] -> testar 130

### Q7. O que é análise de valor-limite (boundary)? Por que é importante?
**Resposta:** Testar os limites exatos das classes: o valor de borda, o imediatamente abaixo e o imediatamente acima. É a técnica que mais encontra erros (erros de operador `<`/`<=`, `+1`/`-1`).
**Exemplo:** regra "desconto acima de R$ 100" -> testar 99,99 | 100,00 | 100,01.

### Q8. O que é tabela de decisão? Quando usar?
**Resposta:** Matriz das combinações de condições e ações. Usar quando a regra tem muitas condições (ex.: cupom + faixa de valor + tipo de cliente). Garante cobertura combinatória gerenciável.

### Q9. Defina teste de caixa-preta e caixa-branca.
**Caixa-preta:** testa sem conhecer o código interno (entrada/saída, comportamento). **Caixa-branca:** testa conhecendo a implementação (cobertura de ramos, condições). QA funcional faz caixa-preta; unitários/caixa-branca ficam com devs (ou QA técnico).

### Q10. O que são testes negativos? Dê exemplos.
**Resposta:** Verificar que o sistema rejeita entradas inválidas/comportamentos não permitidos. Ex.: senha sem número, CPF fajuto, quantidade negativa, desconto 0, SQL injection, campo vazio.

---

## 🔴 Nível 3 - Automação e ferramentas

### Q11. Cite os principais passos para criar uma automação de UI.
1. Analisar requisito e estabilidade (automatizar o que é estável e repetitivo). 2. Escolher ferramenta (Playwright/Selenium/Cypress). 3. Definir seletores robustos (data-testid > id > CSS). 4. Criar Page Objects. 5. Massa de dados. 6. Tratar waits (nunca sleep fixo). 7. Executar em CI com relatório.

### Q12. Seletores: qual a diferença de usar CSS vs XPath? Qual prefere?
**Resposta:** CSS é mais rápido e legível; XPath permite navegar pela árvore (ancestrais, posição) e funciona quando não há classe/id bom. Prefira **CSS + atributos data-testid** (menos quebrável). Use XPath quando for preciso localizar por texto ou relações complexas.

### Q13. Como você trata elementos dinâmicos (load/ajax)?
**Resposta:** Usar espera explícita (`waitForSelector`, `expect(locator).toBeVisible()`, WebDriverWait), esperar o estado desejado (não um tempo fixo), e nunca depender de `sleep(3000)`. Reescrever o `timeout` padrão e usar retry/atômico.

### Q14. O que é Page Object e por que usar?
**Resposta:** Padrão que encapsula os elementos e ações de uma página num objeto reutilizável. Melhora: manutenção centralizada (seletores num só lugar), legibilidade e reuso. Os testes ficam em alto nível ("loginPage.login(user, pass)").

### Q15. Diferença entre `static`, `status code` vs `response body`? (API)
**Resposta:** Código de status diz se a requisição foi processada (200, 400...) mas não garante conteúdo correto. O QA deve validar AMBOS: status + body/schema + tempo de resposta. Ex.: 200 com corpo errado é bug, mesmo com status OK.

### Q16. O que é teste de contrato? (Contract testing)
**Resposta:** Garantir que duas partes (provedor/consumidor) concordam com o contrato da API (schemas, campos obrigatórios). Ferramentas: Pact, Spring Cloud Contract. Evita integrar apps que se "quebram" entre si.

### Q17. Como você testa APIs com autenticação? (token, OAuth)
**Resposta:** Coletar token dinamicamente (login falso/ambiente de teste), usar variáveis de ambiente (nunca token hardcoded), testar ausência/expiração/escopo inválido do token, e validar respostas 401/403.

### Q18. O que é cobertura de requisitos vs cobertura de código?
**Cobertura de requisitos (funcional):** % de requisitos cobertos por casos de teste. **Cobertura de código:** % de linhas/ramos executados pelos testes. Um não substitui o outro.

---

## 🏆 Nível 4 - Cenários e comportamental (AST, situação)

### Q19. "O usuário transfere R$ 1.200 e o sistema mostra saldo errado. O que você faz primeiro?"
**Resposta (fluxo mental):** 1. Reproduzir na base QA (passos exatos). 2. Verificar se é taxa (2% acima de 1000) ou arredondamento. 3. Conferir no banco o registro da transação (valor, taxa, saldo). 4. Classificar severidade (Alta: perda financeira). 5. Reportar com evidências (print, log, dados usados). 6. Cross-check com dev (pode ser regra mal-entendida).

### Q20. "Você encontrou 50 bugs. Como prioriza?"
**Resposta:** Impacto no usuário/negócio > frequência > severidade > bloqueio de fluxos. Usar matriz: Alta severidade + alto impacto primeiro. Criticidade (falha crítica de segurança/financeira) tem prioridade máxima. Documentar e negociar com PO.

### Q21. "Qual a diferença entre bug de UX e bug funcional? Reportaria como?"
**Resposta:** Funcional = comportamento não segue especificação (dá pra escrever repro exato). UX = usabilidade/acessibilidade/consistência visual. Um bug de UX pode ser negociado como melhoria; um funcional é defeito. Ambos são reportados com passos e evidência, mas tratados com prioridades diferentes.

### Q22. Como você estima o tempo de teste?
**Resposta:** Contar casos (incl. Data/ambiente), multiplicar por execução + manutenção + reteste, aplicar fator de complexidade e história (taxa histórica de bugs). Somar tempo de setup e de correção. Estimativa por 3 pontos (otimista/média/pessimista) ajuda.

### Q23. Como você lida com desenvolvedor que disputa o bug ("isso não é bug")?
**Resposta:** 1. Ter SPEC em mãos (documentar com o requisito). 2. Reproduzir com passos exatos de novo. 3. Se a spec for ambígua, chamar o PO para decidir. 4. Manter postura colaborativa. 5. Se nada resolver, escalar a um gerente — nunca "impor".

---

## 📝 Perguntas rápidas (vocabulário padrão)

| Pergunta | Resposta curta |
|---|---|
| Qual o status de um defeito antes de validar no ambiente correto? | `NEW` / `ABERTO` (por confirmar) |
| Ferramenta para gerenciar defeitos? | Jira, Bugzilla, Trello, Azure DevOps |
| `Priority` vs `Severity`? | **Severity** = impacto técnico sobre o sistema; **Priority** = urgência de correção para o negócio. (Pode existir: severidade baixa + prioridade alta.) |
| O que é ambiente homólogo? | Réplica do produção para testes finais. |
| O que é dado de teste (test data)? | Cenários/valores usados como entrada para validar. |
| O que é authorization vs authentication? | **Authn** = quem é você (login). **Authz** = o que você pode fazer (permissões). |
| Code review é teste? | Sim, um tipo de teste estático. |
| O que é traceability matrix? | Mapa requisito <-> caso de teste <-> defeito. |

---

## 💡 Dica de estudo
1. Explique cada termo usando um exemplo (não decore a definição).
2. Treine respondendo em voz alta, com tempo (entrevista real).
3. Monte a "pirâmide de testes": muitos unit (base) -> menos integração -> pouquíssimos E2E.