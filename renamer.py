#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Renomeador Inteligente de PDFs.
Lê PDFs, extrai texto, detecta data/nome/valor e renomeia.
Uso:
  python renamer.py input/
  python renamer.py input/ --dry-run
"""

import argparse
from pathlib import Path

from src.renamer import processar_pasta


def main() -> None:
    parser = argparse.ArgumentParser(description="Renomeia PDFs baseado em texto extraído")
    parser.add_argument("pasta", type=Path, help="Pasta com PDFs")
    parser.add_argument("--dry-run", action="store_true", help="Apenas mostra o que seria feito")
    args = parser.parse_args()

    if not args.pasta.is_dir():
        print(f"Erro: pasta não encontrada: {args.pasta}")
        return

    resultados = processar_pasta(args.pasta, dry_run=args.dry_run)

    if not resultados:
        print("Nenhum PDF para renomear.")
        return

    if args.dry_run:
        print("Modo simulação (--dry-run):")
        for orig, novo in resultados:
            print(f"  {orig.name}")
            print(f"  → {novo.name}")
    else:
        for orig, novo in resultados:
            print(f"  {orig.name} → {novo.name}")


if __name__ == "__main__":
    main()
