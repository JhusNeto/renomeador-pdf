# -*- coding: utf-8 -*-
"""Regex configuráveis para extração de campos."""

import re
from typing import Pattern

# Padrões para data (dd/mm/yyyy, dd-mm-yyyy, yyyy-mm-dd)
REGEX_DATA: list[tuple[Pattern, str]] = [
    (re.compile(r"data[:\s]*(\d{2})[/\-](\d{2})[/\-](\d{4})", re.I), r"\3-\2-\1"),
    (re.compile(r"(\d{2})[/\-](\d{2})[/\-](\d{4})"), r"\3-\2-\1"),
    (re.compile(r"(\d{4})[/\-](\d{2})[/\-](\d{2})"), r"\1-\2-\3"),
]

# Padrões para nome/cliente
REGEX_NOME: list[Pattern] = [
    re.compile(r"nome[:\s]+([A-Za-zÀ-ÿ\s]+?)(?=\n|valor|data|R\$|$)", re.I),
    re.compile(r"cliente[:\s]+([A-Za-zÀ-ÿ\s]+?)(?=\n|valor|data|R\$|$)", re.I),
    re.compile(r"favorecido[:\s]+([A-Za-zÀ-ÿ\s]+?)(?=\n|valor|data|R\$|$)", re.I),
    re.compile(r"benefici[aá]rio[:\s]+([A-Za-zÀ-ÿ\s]+?)(?=\n|valor|data|R\$|$)", re.I),
]

# Padrões para valor em reais
REGEX_VALOR: list[Pattern] = [
    re.compile(r"R\$\s*([\d.,]+)", re.I),
    re.compile(r"valor[:\s]*R?\$?\s*([\d.,]+)", re.I),
    re.compile(r"([\d]{1,3}(?:\.[\d]{3})*(?:,[\d]{2}))(?=\s|$)"),
]

# Formato final do nome: {data} — {nome} — R$ {valor}.pdf
FORMATO_NOME = "{data} — {nome} — R$ {valor}.pdf"
