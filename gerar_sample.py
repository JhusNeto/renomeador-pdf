#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera PDF de exemplo para testes."""

from pathlib import Path

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
except ImportError:
    print("Instale: pip install reportlab")
    exit(1)

ROOT = Path(__file__).resolve().parent
INPUT_DIR = ROOT / "input"


def main():
    INPUT_DIR.mkdir(exist_ok=True)
    path = INPUT_DIR / "comprovante_aleatorio_12345.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setFont("Helvetica", 12)
    y = 700
    c.drawString(100, y, "COMPROVANTE DE PAGAMENTO")
    y -= 40
    c.drawString(100, y, "Data: 11/02/2026")
    y -= 25
    c.drawString(100, y, "Nome: Joao Silva")
    y -= 25
    c.drawString(100, y, "Valor: R$ 250,00")
    c.save()
    print("Gerado:", path)


if __name__ == "__main__":
    main()
