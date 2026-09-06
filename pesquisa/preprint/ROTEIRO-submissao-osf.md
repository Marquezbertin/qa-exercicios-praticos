# Roteiro de Submissão — OSF Preprints (pré-print v0.1)

> **Criado:** 2026-09-06 · **Base:** instruções oficiais OSF (help.osf.io) e CASRAI, verificadas em 2026-09-06.
> **Decisão:** depósito imediato em **OSF Preprints** (sem barreira de endosso, DOI via Crossref, aceita português, gratuito). arXiv (cs.SE) fica como **etapa seguinte**, após conseguir endosso (ex.: futuro orientador autor em cs.SE) e versão em inglês.

---

## 0. O que você precisa antes

- [ ] Conta no OSF (grátis, em `osf.io`): email válido; vincular **ORCID** (recomendado para metadados).
- [ ] Arquivo de upload pronto: **`pesquisa/preprint/preprint-submissao.md`** (versão limpa, sem bloco interno).
  - *Opcional, recomendado:* converter para **PDF** (ex.: pandoc, `md → pdf`) para máxima compatibilidade de leitura. O OSF também aceita MD.
- [ ] Decidir **licença** (recomendado: **CC-BY 4.0** — permite reuso com atribuição; ou CC-BY-SA se quiser share-alike; padrão do campo de licenças).
- [ ] **Suplementos opcionais** preparados (ver §5): script de figuras, figuras, pré-registro (privado — atenção: **não** expor oráculo/matriz privada).

---

## 1. Passo a passo (OSF Preprints)

1. **Logar** em `osf.io/preprints` com a conta criada.
2. Clicar **“Add a Preprint”** (no topo da página de discover) → selecionar **OSF Preprints** (serviço generalista — adequado a qualquer disciplina) → clicar **Select** e **Create preprint**.
3. **Upload do arquivo** — “Upload from your computer” → selecionar o arquivo `preprint-submissao.md` (ou o PDF gerado) → **Next**.
4. **Title** — **cole o título exato** (ver §2). Obrigatório (min. 1 caractere; use o título completo).
5. **Abstract** — **cole o resumo** (§2) na caixa *Abstract* (min. 20 caracteres). **Atenção:** o resumo é digitado/colado **no formulário**; NÃO é carregado como arquivo.
6. **Discipline** — selecionar (o generalista aceita livre; para CS usar, ex.: *Computer Science* > *Software Engineering*). Campo obrigatório em alguns provedores.
7. **Authors** — adicionar seu **nome** (e vincular ORCID). Ordem conforme decidido com coautores (hoje: autor único, se for o caso).
8. **License** — escolher licença (ex.: **CC-BY 4.0**).
9. **Supplements (opcional)** — conectar um **projeto OSF** (ver §5), se quiser disponibilizar figuras/scripts/artefatos públicos.
10. **Author assertions** (alguns provedores) — confirmar disponibilidade de dados públicos, pré-registros e conflitos de interesse.
11. **Review & Submit** — revisar → **Submit** (ou **Create**). Após curadoria (pre-check rápida), o pré-print fica **público com DOI via Crossref** (pode levar até ~24h para "amarrar" o DOI).

> **Importante (direto da política OSF):** um pré-print publicado **não pode ser deletado** — pode ser atualizado/versionado. Cada nova versão recebe novo DOI. Ao publicar, assuma que será **permanentemente público**.

---

## 2. Metadados prontos para copiar

### Título (cole integralmente)
```
Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados
```

### Resumo (cole na caixa Abstract)
```
Software de código-fonte gerado por modelos de linguagem de grande escala (LLMs) tornou-se rotina no ciclo de Engenharia de Software (ES). A literatura demonstrou, em fragmentos isolados, que esse código apresenta defeitos com padrões característicos, vulnerabilidades de segurança frequentes, acúmulo de dívida técnica, testes com efetividade limitada e reprodutibilidade imperfeita. Contudo, nenhum estudo revisado combina, na mesma cadeia experimental controlada, a geração de sistemas completos por diferentes agentes de IA a partir do mesmo requisito, sob múltiplas execuções, avaliados por um oráculo independente com cobertura simultânea de funcionalidade, defeitos, segurança, manutenibilidade e reprodutibilidade. Este artigo apresenta um experimento controlado, prospectivo e reproduzível que preenche essa lacuna: quatro agentes (modelos distintos executados no mesmo framework de agente opencode, 2x Nemotron, Ling e Mimo) produziram, cada um, três execuções independentes de um sistema completo (API REST de gerenciamento de tarefas em Python/FastAPI/PostgreSQL), totalizando 12 entregas avaliadas por uma suíte oráculo independente de 81 testes, mais verificações não funcionais (segurança, manutenibilidade, reprodutibilidade, performance) e uma matriz de defeitos classificada segundo a taxonomia de Tambon et al. com severidades e concordância inter-avaliador. Resultados: apenas 3 das 12 entregas foram bootáveis; os 12 defeitos Tambon foram 100% Blocker ou Critical; os testes gerados pelos próprios agentes não detectaram nenhum dos defeitos (0/12), enquanto o oráculo detectou 4/4 dos alcançáveis; padrões reincidentes (dependência ausente; incompatibilidade passlib+bcrypt; configuração de migração; versão fantasma) concentram a maioria dos defeitos e se repetem entre modelos free, sugerindo um vale comum de qualidade no momento da coleta. O estudo sustenta, descritivamente, que a aprovação pelos próprios testes do agente não é substituta da validação independente, e que um índice único colapsaria dimensões de qualidade (funcional != global). O poder estatístico é limitado (n=12; células esperadas <5), de modo que H1-H3 são apresentadas como tendências, não conclusões; um estudo complementar de laboratório (não evidenciário) reforça a separação entre detectar e testar.
```

### Palavras-chave (para tags)
```
software gerado por IA; agentes de código; qualidade de software; defeitos; oráculo independente; testes de software; Engenharia de Software; experimento controlado
```

### Disciplina sugerida
`Computer Science` → `Software Engineering` (o generalista aceita qualquer; use a mais específica disponível).

### Licença recomendada
`CC-BY 4.0` (atribuição; ampla reutilização). Alternativa: `CC-BY-SA 4.0`.

### Autores
- [SEU NOME] (autor único) — e-mail de conta; ORCID se tiver.

---

## 3. Supressão de informações sensíveis (pré-requisito)

**Antes de publicar, garanta que o arquivo e os suplementos NÃO exponham:**
- o **oráculo** (suíte privada de 81 testes; repo `qa-experimento-oraculo/oracle/`);
- a **especificação** completa privada (`spec/`);
- a **matriz de defeitos bruta** (`results/matriz_defeitos.csv`) — é fonte interna com evidências e resoluções;
- credenciais, chaves ou dados de infraestrutura da VM.

**O pré-print deve conter apenas texto do manuscrito + figuras derivadas agregadas (números públicos), sem artefatos privados.** Os anexos públicos (script de figuras e figuras PNG) são seguros (contêm apenas agregados). O pré-registro é institucional/privado — **não** anexar ao pré-print por ora.

---

## 4. Suplementos (opcional, recomendado — reforça Ciência Aberta)

Crie um **projeto OSF** e conecte ao pré-print. Conteúdo público seguro:
- `pesquisa/figuras/fig1_densidade.png` … `fig5_severidade.png`
- `pesquisa/gerar_figuras.py` (script reprodutível)
- (futuro) pré-registro **versão pública** (depende de autorização e de não expor o oráculo)

> Do arquivo maduro: depositar os **agregados** públicos está alinhado à política de Ciência Aberta dos veículos-alvo (SBES/EMSE) — as execuções brutas permanecem privadas.

---

## 5. Depois de publicado

- [ ] Anotar o **DOI Crossref** e a **URL persistente** do pré-print.
- [ ] Registrar DOI + data no `esqueleto` e no README da pesquisa (atualização do artigo).
- [ ] Atualizar o pré-print quando o manuscrito evoluir (cada nova versão gera novo DOI; URL do preprint permanece).
- [ ] Quando houver orientador + versão em inglês: submeter ao **arXiv cs.SE** usando o endosso do orientador (Ver §6).

---

## 6. arXiv — etapa seguinte (por que não agora)

- Endosso: para submissão em novo domínio, o autor precisa de endosso de autor estabelecido em arXiv no mesmo domínio (cs.SE). Não há endosso automático por e-mail institucional desde jan/2026.
- Idioma: desde 11/fev/2026, toda submissão exige **versão completa em inglês** (tradução automática fiel é aceita).
- Conteúdo: revisões/surveys e *position papers* em cs exigem revisão por pares prévia (nossa pesquisa é **experimental** — não se enquadra nessa restrição, mas o endosso e o inglês permanecem).

> **Estratégia:** use o OSF como registro datado imediato; quando tiver orientador (ou co-autor com presença em arXiv cs.SE), depositar a versão em inglês no arXiv. Isso é complementar, não concorrente.

---

*Fim do roteiro. Pronto para execução manual pela conta OSF do autor (não é possível automatizar a criação de conta/submissão daqui).*