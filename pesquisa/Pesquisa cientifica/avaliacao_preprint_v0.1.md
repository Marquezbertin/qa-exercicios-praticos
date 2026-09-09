# Avaliação do Preprint v0.1 (06/09/2026) — Comparação com o Plano de Revisão

## ✅ O que foi genuinamente resolvido

### 1. Reclassificação de H1–H3 como tendências, não conclusões
**Evidência:** O próprio resumo agora diz: *"O poder estatístico é limitado (n=12; células esperadas <5), de modo que H1–H3 são apresentadas como tendências, não conclusões."*
Isso é exatamente o que o plano pedia na Fase 1.2 — e o mais importante: **está no abstract**, não escondido nas limitações. Isso muda a primeira impressão de um revisor de "estudo confirmatório mal executado" para "estudo exploratório honesto". Ganho real de credibilidade.

### 2. Verificação de DOIs
**Evidência:** Seção de referências agora traz: *"DOI verificados via Crossref/DataCite (16 periódico/conferência; 8 preprints; 1 relatório institucional sem DOI)."*
Resolve diretamente o item 0.3 do plano. Bom — isso é o tipo de detalhe que um revisor checa manualmente e que, quando já vem sinalizado, transmite rigor.

### 3. Documentação do processo de resolução de discordância entre avaliadores
**Evidência:** *"As 6 divergências de categoria concentram-se em defeitos de integração de dependências com múltiplas classes plausíveis (ex.: silly_mistake × wrong_input_type no conflito passlib+bcrypt), resolvidas em reunião com registro."*
Isso resolve exatamente o item 2.4 do plano — não só diz que houve resolução, mas explica **por que** o κ=0,54 foi moderado (categorias ambíguas em defeitos de integração) e como foi resolvido (reunião com registro). Essa é uma melhoria de conteúdo real, não só de redação.

### 4. Transparência sobre a condicionante de ambiente (Docker)
**Evidência:** *"Artefatos Docker exigidos na entrega continuam obrigatórios e são validados estruturalmente; serão executados em contêineres na máquina de produção. Essa condicionante é reportada como limitação (§5.3)."* Also: *"cuidamos de não confundir 'defeito' com 'suposição de ambiente'."*
Não resolve o problema (a validação em container ainda não foi executada), mas mostra que vocês perceberam a armadilha metodológica (confundir falha de ambiente com defeito de código) e tomaram uma decisão de design consciente para evitá-la. Isso é maturidade metodológica, mesmo que o item continue pendente como trabalho futuro.

### 5. Reporte granular e não seletivo dos testes de Fisher por categoria
**Evidência:** Vocês agora reportam não só o achado significativo (ultra, p=0,010), mas também os não significativos: *"ling apontou para wrong_input_type (p=0,083), mimo para silly_mistake (p=0,127), lightning sem categoria dominante."*
Isso é importante porque evita a aparência de **cherry-picking** — reportar só o p-valor bonito e esconder os outros. Reportar os três juntos, mesmo os que não "deram certo", é exatamente o comportamento que a seção de neutralidade (C1) promete.

---

## ⚠️ O que ainda está pendente (conforme o plano original)

| Item do plano | Status nesta versão |
|---|---|
| Aumentar réplicas por agente (5-8 execuções) | Não feito — ainda n=3/agente. Corretamente movido para "Trabalhos futuros (i)". |
| Adicionar mais modelos gratuitos | Não feito — ainda 4 agentes. Movido para "Trabalhos futuros (iii)". |
| Validação em Docker | Não feito — apenas planejado ("Trabalhos futuros (ii)"). |
| Mover estudo de laboratório (§5.2) para apêndice | Não feito — ainda no corpo principal, mas com ressalva bem mais forte agora ("Não constitui evidência do experimento controlado"). |
| Publicar artefatos com DOI (Zenodo) | Não visível no texto — há menções a "artefatos de pesquisa" várias vezes, mas nenhum link público citado. |
| Pré-registro formal em plataforma pública (OSF) | Parcial — ver problema novo #2 abaixo. |
| CIs consistentes (Wilson) para todas as proporções | Não implementado de forma sistemática — só densidade de defeitos tem IC de Poisson explícito. |

Nada disso é grave isoladamente — são itens que vocês mesmos já sinalizaram como "trabalhos futuros" de forma honesta. Mas vale ter clareza de que **a versão atual ainda é a mesma evidência empírica (12 execuções, 4 agentes)** — o que mudou foi majoritariamente enquadramento e rigor de relato, não o tamanho da evidência.

---

## 🔴 Problemas novos nesta versão (não existiam, ou eram menores, na versão em inglês)

### 1. Inconsistência entre abstract e corpo do texto sobre H1
**Evidência:** O abstract diz "H1–H3 são apresentadas como tendências, não conclusões" — mas a seção 5.1 ainda traz a frase problemática original: *"H1 não é rejeitada nem aceita com esta amostra."*
**Por que importa:** "Nem rejeitada nem aceita" não é uma conclusão válida em teste de hipótese frequentista (é o mesmo problema que eu já tinha sinalizado na versão em inglês — não foi corrigido, só "contornado" no abstract). Um revisor atento vai notar a mudança de tom entre o resumo e o corpo.
**Sugestão:** Trocar a frase da seção 5.1 para algo como: *"Com este n, o desenho não tem poder para testar H1 formalmente; os dados de densidade são reportados como tendência descritiva (lightning > ultra ≈ mimo > ling), sem inferência confirmatória."*

### 2. "Pré-registro formalizado retrospectivamente" é uma formulação contraditória
**Evidência:** *"...consolidados posteriormente como um pré-registro formalizado retrospectivamente com âncoras temporais verificáveis no histórico de git."*
**Por que importa:** "Pré-registro retrospectivo" é, literalmente, um oxímoro — pré-registro por definição precisa ser público e anterior à coleta/análise, em uma plataforma com timestamp independente (OSF, AsPredicted). O que vocês descrevem — decisões fixadas antes da coleta e evidenciadas por commits do git — é uma evidência legítima e válida de que o plano não foi ajustado post-hoc, mas **chamar isso de "pré-registro"** (mesmo qualificado como "retrospectivo") tende a soar, para um revisor cético, como uma tentativa de emprestar credibilidade formal a algo que não passou pelo processo formal de pré-registro.
**Sugestão:** Reformular para não usar o termo "pré-registro" para essa parte. Algo como: *"As decisões metodológicas foram fixadas antes da coleta de dados, evidenciado por histórico de commits com timestamp no repositório de pesquisa (não constitui pré-registro formal em plataforma pública). Um pré-registro formal em plataforma como OSF está planejado para o desenho ampliado (ver Trabalhos Futuros)."* Isso é mais defensável e evita a acusação de estar "vestindo" uma prática informal com o vocabulário de uma prática formal.

### 3. Label interno vazado no texto: "(D9)"
**Evidência:** *"Ambiente de validação (D9). A máquina de execução é uma VM sem virtualização aninhada..."*
**Por que importa:** "D9" parece ser um código de rastreamento interno (de matriz de artefatos, checklist ou planilha de gestão do projeto) que vazou para o texto final sem contexto — o leitor não sabe o que "D9" significa. É um detalhe pequeno, mas sinaliza revisão editorial incompleta.
**Sugestão:** Remover o "(D9)" ou, se for necessário rastrear internamente, usar uma nota de rodapé/apêndice com a chave de referência interna dos autores.

### 4. Estudo de laboratório complementar (§5.2) menciona modelos pagos, o que pode gerar uma questão de consistência com a restrição de orçamento
**Evidência:** *"realizamos explorações com chat-LLMs (Oreate/Claude/Gemini — modelos diferentes dos 4 tratamentos)..."*
**Por que importa:** Dois pontos aqui:
- **(a)** Claude e Gemini têm camadas gratuitas de uso via chat web, mas também têm camadas pagas — vale deixar explícito no texto que o acesso foi via **interface gratuita/free-tier**, para manter consistência com a mensagem de "sem custo" que você mencionou ser importante para o projeto. Um revisor pode perguntar "isso usou API paga?" — melhor responder isso preventivamente no texto.
- **(b)** "Oreate" parece ser um erro de digitação ou artefato de OCR/exportação (não é um LLM conhecido) — vale conferir se o nome correto era "ChatGPT", "Copilot" ou outro, e corrigir.
**Sugestão:** Adicionar uma frase entre parênteses: *"(acesso via interface web gratuita, sem uso de API paga)"* e corrigir o nome do terceiro modelo.

### 5. Correção para múltiplas comparações mencionada mas não claramente aplicada
**Evidência:** Seção 3.6 declara: *"Nível α=0,05 com correção para múltiplas comparações."* Mas na seção 4.2, os p-valores pontuais de Fisher são reportados sem indicação se já são ajustados: *"p=0,010... p=0,083... p=0,127"*.
**Por que importa:** Se esses são p-valores brutos (não ajustados) sendo comparados a um α que promete correção, há uma inconsistência entre o que foi declarado no método e o que foi reportado nos resultados. Um revisor de estatística vai perguntar qual correção foi usada (Bonferroni? Holm? Benjamini-Hochberg?) e se os p reportados são brutos ou ajustados.
**Sugestão:** Ou (a) aplicar e reportar explicitamente qual correção foi usada e mostrar os p ajustados, ou (b) remover a menção a "correção para múltiplas comparações" da seção 3.6 e ser explícito de que, dado o caráter exploratório (já declarado no abstract), os p-valores pontuais são reportados **brutos, sem ajuste, para fins descritivos** — o que é coerente com o resto do enquadramento "tendência, não conclusão" que vocês já adotaram.

---

## Nota sobre anonimização (mudança de contexto, não um erro)

Esta versão inclui nome completo do autor, ORCID e credenciais — o que é **correto e esperado para um preprint** (arXiv, SSRN, ResearchGate etc. exigem identificação do autor). O item de anonimização do plano original só se aplica se/quando este material for submetido a uma **venue com revisão double-blind** (journal ou conferência). Vale manter duas versões do arquivo: uma com autoria (para preprint/repositório) e uma anonimizada (para submissão double-blind), trocando apenas capa e removendo o ORCID/afiliação do corpo.

---

## Resumo executivo

| Categoria | Avaliação |
|---|---|
| Honestidade estatística e enquadramento | 🟢 Melhoria real e significativa |
| Rigor de relato metodológico (κ, DOIs) | 🟢 Melhoria real e significativa |
| Tamanho/poder da evidência empírica | 🟡 Inalterado (mesmo n=12, mesmos 4 agentes) |
| Consistência interna do texto | 🟠 Novos pequenos problemas (H1 no corpo vs. abstract; "D9"; múltiplas comparações) |
| Terminologia de pré-registro | 🔴 Precisa correção — "retrospectivo" contradiz o conceito |
| Modelos usados no lab complementar | 🟠 Verificar consistência com restrição de custo zero + corrigir nome do modelo |

**Veredito geral:** este preprint é uma evolução real, não cosmética, em relação à versão anterior — especialmente na honestidade estatística e no tratamento da concordância entre avaliadores. Os itens pendentes (mais réplicas, mais modelos, Docker) são corretamente reconhecidos como trabalho futuro. Os problemas novos identificados aqui são pequenos e de fácil correção (nenhum exige nova coleta de dados) — na prática, é uma passada de revisão de texto de algumas horas, não um novo ciclo experimental.
