# 🧪 QA Simulator - Exercícios e Testes Práticos para QA Tester

Repositório de **prática para QA** (Quality Assurance): sites web simulados com bugs intencionais, exercícios para encontrar defeitos em código, perguntas de entrevista, simulados, técnicas de teste, SQL, API e modelos de documentação.

> Todo bug aqui é **intencional** e com objetivos didáticos. Você é o QA dessas empresas fictícias!

---

## 🚀 Comece por aqui

**⭐ Online (GitHub Pages):** https://marquezbertin.github.io/qa-exercicios-praticos/

O site publica o repositório inteiro como um portal navegável:
- **Portal principal:** `index.html` - hub com todos os exercícios, simulados e templates.
- **Sites simulados:** `sites-para-testar/` - 9 sistemas de empresas fictícias com bugs.
- **Visualizador:** qualquer arquivo Markdown/código é exibido na web via `ver.html?arquivo=<caminho>`.

**No GitHub:** faça `git clone https://github.com/Marquezbertin/qa-exercicios-praticos` e abra localmente.

**📄 Trabalho científico:** a pesquisa em andamento sobre qualidade e defeitos em software gerado por IA fica em `pesquisa/` (revisão bibliográfica, matriz de artigos, problema/hipóteses).

**Como rodar com servidor local (recomendado):**
```bash
cd qa-exercicios-praticos
python -m http.server 8000
# abra http://localhost:8000/
```

---

## 📁 Estrutura do repositório

| Pasta | O que tem |
|---|---|
| `pesquisa/` | **Projeto de artigo científico** em andamento: revisão bibliográfica, matriz de artigos e rascunho de problema/hipóteses |
| `sites-para-testar/` | **9 sites simulados** (loja, banco, hotel, delivery, CRM, impostos, saúde, games...) com bugs + roteiros + gabaritos |
| `encontre-o-bug/codigo/` | Códigos com bugs (6 exercícios: calculadora, banco, carrinho, formulário JS, datas, CPF) |
| `encontre-o-bug/gabarito/` | Respostas dos exercícios de código |
| `perguntas-respostas/` | Banco de perguntas de entrevista de QA com respostas |
| `simulados/` | Testes de múltipla escolha com gabarito |
| `tecnicas-de-teste/` | Exercícios: equivalência, valor-limite, tabela de decisão, estados, pairwise |
| `api-testing/` | Exercícios de testes de API (Postman/requests/carga) |
| `sql-para-qa/` | Exercícios de SQL com schema pronto e gabarito |
| `casos-de-teste/` | Exercícios de escrita de casos de teste |
| `simulacoes/` | Cenários de role-play (entrevista e trabalho) |
| `modelos-templates/` | Modelos: bug report, caso de teste, plano, smoke, relatório |

---

## 🖥️ Os Sites Simulado

| Empresa | Sistema | Dificuldade |
|---|---|---|
| **TechStore** | Loja virtual (carrinho, cupons, frete) | ★★☆ |
| **Banco ABC** | Internet banking (transferência, taxa, extrato) | ★★★ |
| **Reserva Fácil** | Reservas de hotel (datas, promoção) | ★★★ |
| **Portal Cliente** | Cadastro e login (validações, duplicidade) | ★★☆ |
| **FoodGo** | Delivery (combos, troco, CEP, horário) | ★★★ |
| **CRM Connect** | Gestão de clientes (CRUD, busca) | ★★☆ |
| **Contabilidade KM** | Calculadora de impostos (regra de negócio!) | ★★★ |
| **Vida+ Saúde** | Agendamento médico (conflitos, domingo) | ★★★ |
| **Momento Matador** | Loja de games (busca, descontos) | ★☆☆ |

---

## 🧠 Como praticar (método sugerido)

1. **Escolha um site** e rode o roteiro de teste completo (sem olhar o gabarito).
2. **Documente tudo** usando o `bug-report.md` (título, passos, esperado x obtido, severidade).
3. **Explore além do roteiro** (tente quebrar com valores inesperados, duplo-clique, DevTools).
4. **Confira o gabarito** e marque quantos bugs você achou.
5. **Classifique os bugs** por severidade e priorize: o que seria lançado e o que bloquearia o release?
6. **Repita** com o próximo site, subindo a dificuldade.

---

## 🔧 Requisitos

- Um navegador moderno (Chrome/Edge/Firefox) -- os sites são 100% estáticos (`file://` ou servidor local).
- Python 3 (para os exercícios de código e `api-testing`).
- Opcional: Postman/Insomnia, ferramenta SQL, DevTools.

---

## 🎯 Para quem é

- **Quem está começando** em QA: comece pelos sites ★☆☆ e pelos perguntas-respostas.
- **QA em busca de emprego**: use `simulados/`, `perguntas-respostas/` e `simulacoes/`.
- **QA já atuando**: `tecnicas-de-teste/`, `api-testing/`, `sql-para-qa/`, e os sites ★★★.
- **Quem ensina QA**: os sites com roteiro + gabarito funcionam como laboratório de aula.

---

## 📌 Regras para ficar ligado

- Bugs são de propósito. Reporte como num trabalho real (não fique só "achando").
- Sempre valide a **regra de negócio**, não só o cálculo.
- Teste os **casos-limite** (bordas) -- são os que mais pegam.
- Documente mesmo que o teste passe (a matriz de resultados é entregável).

---

## 🤝 Contribuindo

Quer adicionar um site/bug/função? Crie seu arquivo em `sites-para-testar/<nome-dura>/` com `index.html` + `roteiro-de-teste.md` + `gabarito-bugs.md`, e adicione o card no `sites-para-testar/index.html`.

---

## ⚖️ Aviso

Todos os sistemas, empresas e nomes são **fictícios** e construídos apenas para estudo. Bugs com fins didáticos não devem ser replicados em software real.