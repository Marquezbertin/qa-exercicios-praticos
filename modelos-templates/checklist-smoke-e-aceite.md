# Checklist de Smoke Test

> Rode em TODO deploy/build. Se um item falhar, o release é bloqueado.

**Projeto:** __________ **Versão:** __________ **Data:** __________

## Fluxos principais
- [ ] A página principal carrega sem erro de console/JS
- [ ] Login funciona (credenciais válidas)
- [ ] Navegação entre as telas principais funciona
- [ ] Módulo de listagem carrega dados esperados
- [ ] Criar registro (novo cliente/pedido) funciona
- [ ] Excluir um registro funciona
- [ ] Logout funciona
- [ ] Voltar (botão voltar) não quebra o app

## Técnico
- [ ] Sem erro 4xx/5xx no tráfego (F12 -> Network)
- [ ] Console livre de erros JS
- [ ] Banco acessível pelo app
- [ ] Métricas (p95) dentro do SLA básico
- [ ] Versão/deploy tag correta exibida

## Resultado
- [ ] PASS - Smoke verde, liberado para testes completos
- [ ] FAIL - (listar os bloqueios abaixo)

**Bloqueios encontrados:**
1.

---

## Checklist de aceite (release)

- [ ] Nenhum bug **Blocker** aberto
- [ ] Bug de **Alta** severidade: corrigido OU risco formalmente aceito pelo PO
- [ ] Casos críticos verdes (100%)
- [ ] Matriz de rastreabilidade atualizada
- [ ] Dados sensíveis não expostos (logs, configs)
- [ ] Rollback/plano de contingência documentado