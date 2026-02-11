# -*- coding: utf-8 -*-
"""Extração de texto de PDF."""

from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    from PyPDF2 import PdfReader


def extrair_texto(path: str | Path, max_paginas: int = 3) -> str:
    """
    Extrai texto das primeiras páginas do PDF.
    Usa pypdf (ou PyPDF2). max_paginas limita para performance.
    """
    path = Path(path)
    reader = PdfReader(path)
    textos = []
    for i, page in enumerate(reader.pages):
        if i >= max_paginas:
            break
        text = page.extract_text()
        if text:
            textos.append(text)
    return "\n".join(textos)
