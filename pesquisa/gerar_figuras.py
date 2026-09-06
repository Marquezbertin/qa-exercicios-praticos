#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Gera as figuras do artigo a partir dos resultados agregados da Fase 2
(experimento controlado; fonte: qa-experimento-oraculo/results, commit 4b23601).

Reprodutibilidade: este script contém apenas números agregados PUBLICÁVEIS
(ver analise_estatistica.md e kappa_interavaliador.md). As execuções brutas
permanecem no repositório experimental privado.

Saídas: pesquisa/figuras/*.png (dpi=200, formato para artigo).
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = os.path.join(os.path.dirname(__file__), "figuras")
os.makedirs(OUT, exist_ok=True)

BASE = 0.62

def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print("figura ->", path)

# ---------------------------------------------------------------------------
# Dados agregados (Fase 2, n=12 execuções, 4 agentes x 3) — fonte: analise_estatistica.md
AGENTS = ["ultra", "lightning", "ling", "mimo"]
KLOC = {"ultra": 4.30, "lightning": 2.93, "ling": 1.83, "mimo": 3.27}
DEF = {"ultra": 4, "lightning": 4, "ling": 1, "mimo": 3}
DENS = {a: DEF[a] / KLOC[a] for a in AGENTS}

CATS = ["incomplete_generation", "silly_mistake", "wrong_input_type",
        "non_prompted_consideration", "hallucinated_object", "wrong_attribute"]
# defeitos x categoria Tambon (pós-resolução) — fonte: matriz_defeitos.csv / seção 2
MAT = np.array([
    [4, 0, 0, 0, 0, 0],   # ultra  -> incomplete_generation
    [0, 1, 0, 1, 1, 1],   # lightning
    [0, 0, 1, 0, 0, 0],   # ling   -> wrong_input_type
    [1, 2, 0, 0, 0, 0],   # mimo   -> incomplete_generation, silly_mistake
])

SEV = ["Blocker", "Critical", "Major", "Minor"]
SEV_MAT = np.array([
    [4, 0, 0, 0],  # ultra
    [2, 2, 0, 0],  # lightning
    [1, 0, 0, 0],  # ling
    [1, 2, 0, 0],  # mimo
])

# Bootabilidade (RQ1): 3/12 bootáveis
BOOT = {"ultra": 0, "lightning": 1, "ling": 0, "mimo": 2}
BOOT_TOTAL = 3

# ---------------------------------------------------------------------------
# Figura 1 — Densidade de defeitos Tambon por agente (RQ2/H1)
fig, ax = plt.subplots(figsize=(6.4, 4.0))
colors = ["#c0392b", "#2980b9", "#27ae60", "#8e44ad"]
bars = ax.bar(AGENTS, [DENS[a] for a in AGENTS], color=colors, alpha=0.85,
              edgecolor="black", linewidth=0.8)
for b, a in zip(bars, AGENTS):
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 0.02,
            f"{DENS[a]:.2f}\n({DEF[a]} defeitos / {KLOC[a]:.2f} KLOC)",
            ha="center", va="bottom", fontsize=8.5)
ax.set_ylabel("Defeitos Tambon por KLOC")
ax.set_ylim(0, 1.6)
ax.grid(axis="y", linestyle=":", alpha=0.5)
ax.set_title("Densidade de defeitos por agente (n=12 execuções)")
save(fig, "fig1_densidade.png")

# ---------------------------------------------------------------------------
# Figura 2 — Heatmap defeito x categoria x agente (RQ3/H2)
fig, ax = plt.subplots(figsize=(8.0, 3.6))
im = ax.imshow(MAT, cmap="YlOrRd", aspect="auto")
ax.set_xticks(range(len(CATS)))
ax.set_xticklabels(CATS, rotation=30, ha="right", fontsize=8)
ax.set_yticks(range(len(AGENTS)))
ax.set_yticklabels(AGENTS)
for i in range(MAT.shape[0]):
    for j in range(MAT.shape[1]):
        v = MAT[i, j]
        ax.text(j, i, str(v) if v else "", ha="center", va="center",
                color="black" if v < 3 else "white", fontsize=10)
cbar = fig.colorbar(im, ax=ax, fraction=0.046)
ax.set_title("Distribuição de defeitos: categoria Tambon x agente")
save(fig, "fig2_heatmap_categoria_agente.png")

# ---------------------------------------------------------------------------
# Figura 3 — Bootabilidade (RQ1): bootavel x nao-bootavel por agente
fig, ax = plt.subplots(figsize=(6.4, 4.0))
x = np.arange(len(AGENTS))
boot_vals = [BOOT[a] for a in AGENTS]
noboot = [3 - BOOT[a] for a in AGENTS]
p1 = ax.bar(x, noboot, BASE, label="Não bootável", color="#e74c3c", edgecolor="black", linewidth=0.8)
p2 = ax.bar(x, boot_vals, BASE, bottom=noboot, label="Bootável", color="#2ecc71", edgecolor="black", linewidth=0.8)
ax.set_xticks(x)
ax.set_xticklabels(AGENTS)
for xi, bv, nv in zip(x, boot_vals, noboot):
    ax.text(xi, nv + 0.05, f"{nv}/3", ha="center", va="bottom", fontsize=9)
    if bv:
        ax.text(xi, nv + bv + 0.05, f"boot {bv}", ha="center", va="bottom", fontsize=9)
ax.set_ylabel("Número de execuções (de 3)")
ax.set_ylim(0, 3.6)
ax.set_title(f"Bootabilidade por agente — total {BOOT_TOTAL}/12 bootáveis")
ax.legend()
ax.grid(axis="y", linestyle=":", alpha=0.5)
save(fig, "fig3_bootabilidade.png")

# ---------------------------------------------------------------------------
# Figura 4 — Concordância inter-avaliador (kappa) categoria vs severidade
fig, ax = plt.subplots(figsize=(5.2, 4.0))
labels = ["Categoria\n(Tambon)", "Severidade"]
kappa = [0.54, 0.91]
bands = [("Sem concordância", -1, 0, "#cccccc"),
         ("Leve", 0, 0.2, "#d9d9d9"),
         ("Razoável", 0.2, 0.4, "#f6f6f6"),
         ("Moderada", 0.4, 0.6, "#fff3cd"),
         ("Substancial", 0.6, 0.8, "#d4edda"),
         ("Quase perfeita", 0.8, 1.0, "#c3e6cb")]
for lab, lo, hi, c in bands:
    ax.axhspan(lo, hi, color=c, zorder=0)
bars = ax.bar(labels, kappa, color=["#f39c12", "#2980b9"], edgecolor="black", width=0.55, zorder=3)
for b, k in zip(bars, kappa):
    ax.text(b.get_x() + b.get_width()/2, k + 0.02, f"κ={k:.2f}", ha="center", va="bottom", fontsize=10)
ax.set_ylim(0, 1.15)
ax.set_ylabel("κ de Cohen")
ax.set_title("Concordância inter-avaliador (Dr. A x Dr. B, n=18)")
ax.grid(axis="y", linestyle=":", alpha=0.4, zorder=2)
save(fig, "fig4_kappa.png")

# ---------------------------------------------------------------------------
# Figura 5 — Severidade dos defeitos por agente (RQ4)
fig, ax = plt.subplots(figsize=(7.2, 3.8))
y = np.arange(len(AGENTS))
left = np.zeros(len(AGENTS))
colors_sev = {"Blocker": "#c0392b", "Critical": "#e67e22", "Major": "#f1c40f", "Minor": "#95a5a6"}
for k, sev in enumerate(SEV):
    vals = SEV_MAT[:, k]
    ax.barh(y, vals, 0.55, left=left, label=sev, color=colors_sev[sev],
            edgecolor="black", linewidth=0.6)
    for yi, v in enumerate(vals):
        if v:
            ax.text(left[yi] + v/2, yi, str(v), ha="center", va="center", color="white", fontsize=9)
    left += vals
ax.set_yticks(y)
ax.set_yticklabels(AGENTS)
ax.set_xlabel("Número de defeitos")
ax.set_xlim(0, 5)
ax.set_title("Severidade dos defeitos Tambon por agente (12/12 Blocker ou Critical)")
ax.legend(loc="lower right", fontsize=8)
save(fig, "fig5_severidade.png")

print("OK — figuras geradas em", OUT)
