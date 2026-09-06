# Plano de Submissão — SBES 2027 (Trilha de Pesquisa)

> **Criado:** 2026-09-06 · **Estratégia (dossiê §3):** publicar **primeiro no SBES 2027** (peer-reviewed seguro com n=12), depois ampliar amostra → EMSE. Pré-print publicado no Zenodo (`10.5281/zenodo.22551156`) como registro datado anterior.
> **Status:** preparação em andamento. Chamada oficial SBES 2027 ainda não publicada — padrões abaixo são os do SBES 2026 (CBSoft), verificados em 2026-09-06.

---

## 1. Fatos verificados (referência SBES 2026, ciclo CBSoft)

| Item | Regra (2026) |
|---|---|
| Data típica | Registro ~27/abr; submissão ~04/mai (SBES 2027: esperar ~abr/2027; **confirmar na chamada oficial**, deve sair ~fim de 2026) |
| Páginas | **Máx. 10 páginas** (inclui figuras, tabelas, agradecimentos) + **2 páginas** extras de referências |
| Idioma | Português **ou** Inglês (inglês: maior visibilidade; anais ACM DL). Se PT, exigido resumo em EN |
| Template | Modelo da conferência CBSoft (adaptação do ACM `acmart`); **NÃO usar** `ACM_SigConf` original; `\acmConference[SBES XXXX]{...}`; para revisão: `\documentclass[sigconf,anonymous]{acmart}` |
| Revisão | **Duplo-anônima** — ocultar nomes/afiliações; evitar "nós"/"nosso"; citações a trabalho próprio em 3ª pessoa; sem links de artefatos identificáveis; usar `anonymous.4open.science` p/ artefatos |
| Submissão | JEMS 3 (registro do artigo: título, autores, resumo, tópicos, idioma; depois PDF completo) |
| Ciência Aberta | Seção não numerada **"Disponibilidade de Artefatos"** após a Conclusão: link dos artefatos ao comitê (repositório anônimo/upload suplementar) com instruções, **ou** declaração explícita de por quê não; padrão: dados disponíveis após aceite |
| Aceite | ≥1 autor inscrito no CBSoft e **apresentação presencial**; artigo não apresentado não entra nos anais |
| Artefatos (Festival CBSoft) | Após aceite: depósito público com **DOI** + `README` + `LICENSE`; selos *Available* e/ou *Functional* |
| Ética | Conformidade com uso de IA generativa (política SBC; revisão humana dos textos) |

---

## 2. Decisões para a submissão SBES 2027

| # | Decisão | Recomendação | Quem decide |
|---|---|---|---|
| 1 | **Trilha** | Trilha de Pesquisa (principal; publica estudos empíricos completos) | Autor |
| 2 | **Idioma** | **Inglês** (reuso entre SBES, arXiv cs.SE e base EMSE; visibilidade ACM DL) — alternativo: PT (resumo EN obrigatório) | Autor |
| 3 | **Foco / título SBES** | Versão condensada em 10 páginas destacando **RQ6/H3 (aprovação própria ≠ validação independente)** + padrões reincidentes + Ciência Aberta | Autor |
| 4 | **Trabalho anterior (pré-print)** | Não citar o pré-print Zenodo na submissão anônima (revela identidade). Se citado: "[Ref] omitida devido à revisão duplo-anônima". Após aceite, citar normal | Autor |
| 5 | **Artefatos** | Submeter agregados públicos (figuras + `gerar_figuras.py` + sumários) via repositório **anônimo** (anonymous.4open.science) — **não** expor oráculo/`spec`/matriz bruta; pós-aceite: depósito com DOI no Zenodo + badges | Autor |
| 6 | **Amostra n=12** | Manter n=12 (SBES tolera; forte seção de limitações honestas — já temos) | Autor |

---

## 3. Orçamento de páginas (10 páginas alvo)

Estrutura recomendada para o SBES (IMRaD condensado a partir do manuscrito v0.1):

| Seção | Páginas (~) | O que entra |
|---|---|---|
| 1. Introdução (lacuna, problema, contribuições) | 1,5 | §1 do manuscrito condensado (problema de pesquisa + 3 contribuições) |
| 2. Trabalhos relacionados | 1,0 | Tabela-síntese da revisão (25 refs → mapa por dimensão) |
| 3. Método (experimento) | 2,0 | Desenho 4×3=12, oráculo 81 testes, taxonomia Tambon, análise (χ²/Fisher/κ) — com Fig 1 |
| 4. Resultados (RQ1–RQ6) | 2,5 | Figs 2–5 + tabela de defeitos; ênfase RQ6/H3 (0/12 vs 4/4) |
| 5. Discussão + Ameaças à validade | 1,5 | Padrões reincidentes; limitações honestas (n=12, viés Blocking, sem Docker, C1) |
| 6. Conclusão | 0,75 | Implicações e próximos passos (EMSE ampliado) |
| Disponibilidade de Artefatos | 0,25 | Link anônimo + licença |
| Referências | 2 (extras) | Priorizar refs citadas na versão condensada (estimativa ~20) |

> **Redução do manuscrito:** o v0.1 hoje é longo (IMRaD completo + 25 refs). A condensação reescreve, não corta por cima: cada parágrafo vira 1–2 frases; a tabela-síntese substitui os §2 extensos; figs 2–5 completam a mensagem dos §4.

---

## 4. Checklist até o prazo (~abr/2027)

- [ ] **Confirmar chamada SBES 2027** (link do CBSoft 2027) — início 2027 (ativo: autor, com lembrete)
- [x] Gerar **rascunho SBES-10p** (EN) e **arquivo `.tex` acmart anonimizado** pronto para Overleaf — `artigo-sbes-2027-draft-en.md` + `artigo-sbes-2027.tex` (figuras em `pesquisa/figuras/`)
- [ ] **Compilar no Overleaf** com o template acmart do CBSoft 2027; embutir figuras; conferir **contagem de páginas ≤10+2** e ajustar tamanho de figs/tabelas se estourar
- [ ] Redação em EN (reuso do `artigo-manuscrito-en-v0.1.md`); revisão de linguagem
- [ ] **Pacote de artefatos anônimo** (anonymous.4open.science): figs 1–5, `gerar_figuras.py`, README, LICENSE (CC-BY-4.0), sumários agregados — sem dados brutos
- [ ] Checagem de anonimização (nomes, "nós", github, Zenodo, ORCID, DOI do preprint)
- [ ] Revisão dupla interna (par de olhos 2) + checagem de página/template
- [ ] Submeter via JEMS 3 (registro → PDF) dentro do prazo (~abr/2027)
- [ ] Rebuttal (se houver) + versão final + inscrição CBSoft + presença

---

## 5. Pré-requisitos transversais (em paralelo)

- **Pré-registro formal** já existe no repo privado (âncoras git) — ok.
- **ORCID** já vinculado ao pré-print (Works) — ok; usar mesmo ORCID no JEMS.
- **Aprimoramentos possíveis antes da submissão** (não obrigatórios com n=12): rodar validação em Docker em produção; testar 1–2 agentes adicionais.

---

*Plano v0.1 — 2026-09-06. Base nos padrões verificados do SBES 2026 (cbsoft.sbc.org.br). Revisar quando a chamada oficial do SBES 2027 for publicada.*