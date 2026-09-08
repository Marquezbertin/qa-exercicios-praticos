#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converte o preprint MD em HTML estilizado (A4) para impressao em PDF via Edge/Chrome."""
import os
import markdown

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "preprint-submissao.md")
OUT = os.path.join(BASE, "preprint-submissao.html")

with open(SRC, encoding="utf-8") as f:
    md = f.read()

html_body = markdown.markdown(
    md,
    extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
)

css = """
@page { size: A4; margin: 2.0cm 2.2cm; }
body { font-family: Georgia, 'Times New Roman', serif; font-size: 11pt;
       line-height: 1.45; color: #111; text-align: justify; }
h1 { font-size: 16pt; text-align: left; border-bottom: 1px solid #ccc; padding-bottom: 6px; }
h2 { font-size: 13pt; text-align: left; margin-top: 18px; }
h3 { font-size: 11.5pt; text-align: left; }
code { font-family: 'Courier New', monospace; font-size: 9.5pt;
       background: #f3f3f3; padding: 1px 3px; border-radius: 2px; }
pre { background: #f6f6f6; border: 1px solid #ddd; padding: 8px; font-size: 9.5pt;
      overflow-wrap: break-word; white-space: pre-wrap; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
th, td { border: 1px solid #999; padding: 4px 6px; text-align: left; }
th { background: #efefef; }
strong { color: #000; }
img { max-width: 100%; }
"""

html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Preprint</title>
<style>{css}</style>
</head>
<body>
{html_body}
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_doc)

print("HTML gerado:", OUT)