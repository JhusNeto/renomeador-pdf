# Renomeador Inteligente de PDFs

Sistema que lê PDFs, extrai texto e renomeia automaticamente baseado em data, nome e valor detectados via regex.

## Formato gerado

`2026-02-11 — João Silva — R$ 250,00.pdf`

## Uso

```bash
pip install -r requirements.txt

# Renomear PDFs na pasta
python renamer.py input/

# Simular (não renomeia)
python renamer.py input/ --dry-run
```

## Regex configuráveis

Edite `src/config.py` para ajustar os padrões:
- `REGEX_DATA` – captura de datas
- `REGEX_NOME` – captura de nome/cliente
- `REGEX_VALOR` – captura de valores em R$

## Exemplos

- `examples/antes_comprovante_aleatorio.pdf` – antes
- `examples/2026-02-11 — Joao Silva — R$ 250,00.pdf` – depois
