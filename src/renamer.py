# -*- coding: utf-8 -*-
"""Lógica de renomeação de arquivos."""

from pathlib import Path
from typing import List, Tuple

from .extractor import extrair_texto
from .parser import gerar_nome_arquivo


def processar_pasta(pasta: Path, dry_run: bool = False) -> List[Tuple[Path, Path]]:
    """
    Processa todos os PDFs na pasta.
    Retorna lista de (original, novo_caminho).
    Se dry_run=True, não renomeia de fato.
    """
    resultados = []
    pasta = Path(pasta)
    if not pasta.is_dir():
        return resultados

    for pdf in sorted(pasta.glob("*.pdf")):
        try:
            texto = extrair_texto(pdf)
            novo_nome = gerar_nome_arquivo(texto)
            novo_path = pdf.parent / novo_nome
            if novo_path.resolve() != pdf.resolve():
                alvo = novo_path
                cont = 1
                while alvo.exists() and alvo.resolve() != pdf.resolve():
                    stem = novo_path.stem
                    alvo = pdf.parent / f"{stem} ({cont}).pdf"
                    cont += 1
                resultados.append((pdf, alvo))
                if not dry_run:
                    pdf.rename(alvo)
        except Exception:
            pass
    return resultados
