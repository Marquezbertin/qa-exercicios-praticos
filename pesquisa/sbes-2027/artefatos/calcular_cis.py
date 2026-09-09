#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Calcula intervalos de confianca de Wilson (95%) para as proporcoes do estudo
e projecoes da Fase 2. Apenas stdlib (sem scipy) — artefato reproduzivel.

Uso: python calcular_cis.py
Fonte dos numeros atuais: preprint/artigo Fase 2 (n=12 execucoes).
Fonte das projecoes: plano de expansao Fase 2 (taxa de boot 25% assumida).
"""
import math

Z = 1.96  # 95%


def wilson(x, n, z=Z):
    """Retorna (limite_inferior, limite_superior) de Wilson para x sucessos em n."""
    if n == 0:
        return (0.0, 1.0)
    p = x / n
    denom = 1.0 + z * z / n
    center = (p + z * z / (2.0 * n)) / denom
    half = z * math.sqrt(p * (1.0 - p) / n + z * z / (4.0 * n * n)) / denom
    return (max(0.0, center - half), min(1.0, center + half))


def linha(rotulo, x, n):
    lo, hi = wilson(x, n)
    print(f"{rotulo:52} {x:3d}/{n:<3d}  IC95% [{lo:.3f} - {hi:.3f}]  largura {hi - lo:.3f}")


print("=" * 92)
print("FASE 1 — valores atuais do estudo (n=12)")
print("=" * 92)
linha("RQ1 bootabilidade", 3, 12)
linha("RQ4 Blocker", 8, 12)
linha("RQ4 Critical", 4, 12)
linha("RQ6 deteccao pelos testes do agente", 0, 12)

print()
print("=" * 92)
print("FASE 2 — projecoes RQ1 (taxa de boot 25% mantida)")
print("=" * 92)
for total, per_agent in [(12, 3), (32, 8), (40, 10), (80, 20)]:
    boot = round(total * 0.25)
    linha(f"RQ1 {total} total ({per_agent}/agente)", boot, total)

print()
print("=" * 92)
print("FASE 2 — projecoes RQ6 (0 detectados pelo agente, N cresce)")
print("=" * 92)
for n in [12, 20, 40, 80]:
    linha(f"RQ6 N={n} defeitos avaliados", 0, n)

print()
print("=" * 92)
print("REGRA DE PARADA — largura-alvo <= 0,30 (RQ1/RQ6/RQ7/RQ8)")
print("=" * 92)
for total in [12, 32, 40]:
    lo, hi = wilson(round(total * 0.25), total)
    print(f"RQ1 n={total:<3d} largura {hi - lo:.3f}  {'ATINGE' if hi - lo <= 0.30 else 'nao atinge'}")
print("OK - calculos concluidos")
