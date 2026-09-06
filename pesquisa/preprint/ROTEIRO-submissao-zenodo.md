# Roteiro de Submissão — Zenodo (pré-print v0.1)

> **Criado:** 2026-09-06 · **Base:** política/infos Zenodo (zenodo.org) verificadas em 2026-09-06.
> **Por que Zenodo (e não OSF/TechRxiv):** o servidor generalista **OSF Preprints foi suspenso para novas submissões** (aviso oficial de 25/ago/2025 — os preprints existentes permanecem, mas não se cria mais); o **TechRxiv** (IEEE) está **temporariamente fechado** para novas submissões (transição de plataforma, mar/2026). O **Zenodo** (CERN) é o caminho livre e definitivo: **gratuito**, **DOI imediato via DataCite (10.5281)**, aceita **qualquer disciplina** (inclui Engenharia de Software), **sem endosso** e **sem exigir afiliação**, com **login via ORCID** (atualiza o perfil automaticamente). Publicação **instantânea, sem moderação**. arXiv (cs.SE) fica como **etapa seguinte** (endosso + inglês).

---

## 0. O que você precisa antes

- [ ] Conta no Zenodo (`zenodo.org`): login recomendado via **ORCID** (ou Github/e-mail). Grátis.
- [ ] Arquivo de upload pronto: **`pesquisa/preprint/preprint-submissao.pdf`** (preprint v0.1, já com autor + ORCID no cabeçalho).
- [ ] Textos prontos para copiar: **título** (abaixo) e **resumo** integral (seção **Resumo** de `pesquisa/preprint/preprint-submissao.md`).
- [ ] Licença decidida: **CC-BY 4.0** (Creative Commons Attribution 4.0 International).
- [ ] **Suplementos opcionais** preparados (ver §4): figuras 1–5 + `gerar_figuras.py` (apenas agregados públicos — seguros para Ciência Aberta).

---

## 1. Passo a passo (Zenodo)

1. Abrir `zenodo.org` → clicar **Log in** → escolher **ORCID** (recomendado). Autorizar e, na primeira entrada, permitir que o Zenodo **atualize seu perfil ORCID**.
2. Clicar **New upload** (canto superior direito).
3. **Upload files** — arrastar/ou clicar para selecionar **`preprint-submissao.pdf`**.
4. **Resource type** — selecionar **Publication** → subtipo **Preprint**.
5. **Title** — colar o **título integral** (§2).
6. **Description** — colar o **resumo integral** (fonte: `preprint-submissao.md`, seção Resumo; o Zenodo aceita *markdown*). Pode acrescentar as palavras-chave no final e um parágrafo de "[versionamento e DOI]" com o texto de persistência (§6).
7. **Keywords** — colar as palavras-chave (§2).
8. **Access right** — **Public** (permitir acesso imediato, propagação e reutilização). **Embargo:** nenhum (data de hoje).
9. **License** — **Creative Commons Attribution 4.0 International** (CC-BY-4.0).
10. **Creators** — clicar **Add another creator** → nome **Bruno Bertin Marquez** + ORCID `0009-0005-3546-8302` (pode importar direto do seu perfil). Afiliação: **opcional** — como pesquisador independente, pode deixar em branco ou "Pesquisador independente".
11. *(Opcional)* **Additional titles / Language** — preencher **Language** = **Portuguese**.
12. **Save upload** → revisar prévia → **Publish**.
13. **DOI imediato** — na página publicada, anotar:
    - DOI: `https://doi.org/10.5281/zenodo.<ID>` (numeração automática, **instantânea**, sem curadoria);
    - URL da página: `https://zenodo.org/records/<ID>`.
14. Se logou via ORCID, confirmar a opção de **exportar o DOI para o ORCID (Works)** — esse é o "esqueleto" público da sua produção.

> **Importante (política Zenodo/DataCite):** um registro publicado **não pode ser deletado ou sobrescrito**. Erros são corrigidos por **nova versão** (que recebe **novo DOI**; o DOI e o registro da versão original permanecem). Ao publicar, assuma que será **permanentemente público** no CERN.
>
> **Importante (semântica):** o Zenodo é um **repositório generalista** (não um servidor de pré-print com moderação/marcas de curadoria). Depósito de preprint nele é prática padrão e reconhecida; o DOI é **DataCite (10.5281)**, não Crossref — normal em auto-depósito. Se no futuro você preferir um serviço explicitamente de "pré-print" com DOI Crossref, há o **Preprints.org** (fallback; interface e resumo em **inglês** — usar `artigo-manuscrito-en-v0.1.md`).

---

## 2. Metadados prontos para copiar

### Título (cole integralmente)
```
Avaliação Empírica da Qualidade e dos Defeitos em Software Gerado por Agentes de Inteligência Artificial: Um Estudo Comparativo sob Requisitos Controlados
```

### Resumo
Copiar o **resumo integral** da seção **Resumo** de `pesquisa/preprint/preprint-submissao.md` (mesmo texto do pré-print; não usar versão abreviada).

### Palavras-chave (para o campo Keywords)
```
software gerado por IA; agentes de código; qualidade de software; defeitos; oráculo independente; testes de software; Engenharia de Software; experimento controlado
```

### Resource type
`Publication` → `Preprint`

### Licença
`Creative Commons Attribution 4.0 International` (CC-BY-4.0)

### Autores
- **Bruno Bertin Marquez** (autor único) — ORCID: `0009-0005-3546-8302` (`https://orcid.org/0009-0005-3546-8302`); afiliação opcional.

---

## 3. Supressão de informações sensíveis (pré-requisito)

**Antes de publicar, garanta que o arquivo e os suplementos NÃO exponham:**
- o **oráculo** (suíte privada de 81 testes; repo `qa-experimento-oraculo/oracle/`);
- a **especificação** completa privada (`spec/`);
- a **matriz de defeitos bruta** (`results/matriz_defeitos.csv`) — fonte interna com evidências e resoluções;
- credenciais, chaves ou dados de infraestrutura da VM.

**O registro deve conter apenas o texto do manuscrito + figuras derivadas agregadas (números públicos), sem artefatos privados.** Os anexos públicos (script de figuras e PNGs) são seguros (contêm apenas agregados). O pré-registro é institucional/privado — **não** anexar ao registro por ora.

---

## 4. Suplementos (opcional, recomendado — reforça Ciência Aberta)

No Zenodo dá para incluir **arquivos complementares** na mesma submissão (ou numa **nova versão** depois):
- `pesquisa/figuras/fig1_densidade.png` … `fig5_severidade.png`
- `pesquisa/gerar_figuras.py` (script reprodutível)
- (futuro) pré-registro **versão pública** (depende de autorização e de não expor o oráculo)

> Do arquivo maduro: depositar os **agregados** públicos está alinhado à política de Ciência Aberta dos veículos-alvo (SBES/EMSE) — as execuções brutas permanecem privadas.

---

## 5. Depois de publicado

- [ ] Anotar o **DOI** (`10.5281/zenodo.<ID>`) e a **URL persistente** (`zenodo.org/records/<ID>`).
- [ ] Registrar DOI + data no **esqueleto** e no **README** da pesquisa (atualização do artigo).
- [ ] Registrar o DOI no **perfil ORCID** (Works) se o Zenodo não tiver exportado automaticamente.
- [ ] Atualizar o pré-print quando o manuscrito evoluir (nova versão gera **novo DOI**; a URL da versão original permanece).
- [ ] Quando houver orientador/coautor + versão em inglês: submeter ao **arXiv cs.SE** usando o endosso (ver §6).

---

## 6. arXiv — etapa seguinte (por que não agora)

- Endosso: para submissão em novo domínio, o autor precisa de endosso de autor estabelecido em arXiv no mesmo domínio (cs.SE). Não há endosso automático por e-mail institucional desde jan/2026.
- Idioma: desde 11/fev/2026, toda submissão exige **versão completa em inglês** (nossa `artigo-manuscrito-en-v0.1.md` atende).
- Conteúdo: revisões/surveys e *position papers* em cs exigem revisão por pares prévia (nossa pesquisa é **experimental** — não se enquadra, mas endosso e inglês permanecem).

> **Estratégia:** o **Zenodo** é o registro datado **imediato** (DOI + permanência, hoje, em português, sem barreira); o **arXiv** fica como **depósito complementar posterior** quando houver endosso (ex.: futuro coautor com presença em cs.SE). São complementares, não concorrentes.

---

*Fim do roteiro. Pronto para execução manual pela conta Zenodo do autor (não é possível automatizar a criação de conta/submissão daqui).*