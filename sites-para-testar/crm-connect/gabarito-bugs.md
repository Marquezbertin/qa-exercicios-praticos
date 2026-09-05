# CRM Connect - Gabarito de Bugs Intencionais

> Consulte APENAS depois de fazer seus testes.

## Bugs presentes no site

### BUG 1 - Busca não normaliza acentos (Severidade: Média)
- **Onde:** `render()` usa `toLowerCase()` apenas; "João" não combina com "joao".
- **Esperado:** Busca por "joao" encontra "João".
- **Obtido:** Nenhum resultado.
- **Como testar:** CT-08.

### BUG 2 - Salvar edição de registro já excluído dá mensagem de sucesso falsa (Severidade: Alta)
- **Onde:** `salvar()` com `editandoId` de um cliente excluído: `findIndex` retorna -1, mas a mensagem "Cliente atualizado com sucesso!" aparece mesmo assim.
- **Esperado:** Nunca confirmar uma atualização que não ocorreu.
- **Obtido:** O usuário acredita que salvou, mas o registro não existe mais.
- **Como testar:** CT-12.

### BUG 3 - Exclusão permite apagar registro em edição sem proteção (Severidade: Média)
- **Onde:** Editar um cliente e logo em seguida excluir o mesmo cliente (linha da tabela) mantém o estado de edição pendente.
- **Esperado:** A exclusão deveria invalidar o estado de edição (ou bloquear), evitando o BUG 2.
- **Como testar:** etapas do CT-12.

---

## Principais lições deste exercício
- UX/consistência de estados: excluir/alvo em edição deve ser protegido.
- Pesquisa de texto exige normalização de acentuação.
- Nunca exibir sucesso sem verificar se a operação realmente ocorreu.
- Testar fluxos "mistos": editar + excluir + salvar, em sequências diferentes.