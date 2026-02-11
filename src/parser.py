# -*- coding: utf-8 -*-
"""Parser: extrai data, nome e valor do texto com regex."""

import re
from typing import Optional

from .config import REGEX_DATA, REGEX_NOME, REGEX_VALOR, FORMATO_NOME


def _normalizar_texto(s: str) -> str:
    """Remove espaços extras e caracteres problemáticos."""
    if not s:
        return ""
    s = re.sub(r"\s+", " ", str(s).strip())
    return s[:80]  # Limite para nome do arquivo


def extrair_data(texto: str) -> Optional[str]:
    """Extrai data no formato YYYY-MM-DD."""
    for pattern, repl in REGEX_DATA:
        m = pattern.search(texto)
        if m:
            try:
                return m.expand(repl).strip()
            except Exception:
                pass
    # Fallback: primeiro padrão dd/mm/yyyy ou类似
    m = re.search(r"(\d{2})[/\-](\d{2})[/\-](\d{4})", texto)
    if m:
        return f"{m.group(3)}-{m.group(2)}-{m.group(1)}"
    m = re.search(r"(\d{4})[/\-](\d{2})[/\-](\d{2})", texto)
    if m:
        return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
    return None


def extrair_nome(texto: str) -> str:
    """Extrai nome/cliente. Retorna 'Desconhecido' se não encontrar."""
    for pattern in REGEX_NOME:
        m = pattern.search(texto)
        if m:
            return _normalizar_texto(m.group(1))
    return "Desconhecido"


def extrair_valor(texto: str) -> str:
    """Extrai valor formatado (BR: 1.250,00). Retorna '0,00' se não encontrar."""
    for pattern in REGEX_VALOR:
        m = pattern.search(texto)
        if m:
            val = m.group(1).replace(".", "").replace(",", ".")
            try:
                n = float(val)
                return f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")[:20]
            except ValueError:
                return "0,00"
    return "0,00"


def gerar_nome_arquivo(texto: str) -> str:
    """Gera nome estruturado: 2026-02-11 — João Silva — R$ 250,00.pdf"""
    data = extrair_data(texto) or "0000-00-00"
    nome = extrair_nome(texto)
    valor = extrair_valor(texto)
    nome_arquivo = FORMATO_NOME.format(data=data, nome=nome, valor=valor)
    # Sanitizar para filesystem
    nome_arquivo = re.sub(r'[<>:"/\\|?*]', "_", nome_arquivo)
    return nome_arquivo.strip()
