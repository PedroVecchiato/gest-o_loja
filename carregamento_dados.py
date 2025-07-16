import os
import json

def carregar_dados(caminho_arquivo):
    
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)  # Carrega a lista de nomes do arquivo
    else:
        return []  # Lista vazia se o arquivo não existir


def salvar_dados(dados,caminho_arquivo):
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

