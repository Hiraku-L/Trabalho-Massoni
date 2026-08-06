import json

from src.algoritmos import Des, Rsa, Gm
from src.utils.codificador import serializar_chave, serializar_cifrado

ALGORITMOS_DISPONIVEIS = {
    "DES": lambda **kwargs: Des(),
    "RSA": lambda rsa_bits=1024, **kwargs: Rsa(bits=rsa_bits),
    "GM": lambda gm_bits=512, **kwargs: Gm(bits=gm_bits),
}


def cifrar(algoritmo_nome: str, texto: str, rsa_bits: int = 1024, gm_bits: int = 512) -> dict:
    if algoritmo_nome not in ALGORITMOS_DISPONIVEIS:
        raise ValueError(
            f"algoritmo '{algoritmo_nome}' desconhecido. "
            f"Use um de: {', '.join(ALGORITMOS_DISPONIVEIS)}"
        )

    algoritmo = ALGORITMOS_DISPONIVEIS[algoritmo_nome](rsa_bits=rsa_bits, gm_bits=gm_bits)

    texto_bytes = texto.encode("utf-8")

    chaves = algoritmo.gerar_chaves()
    texto_cifrado = algoritmo.cifrar(texto_bytes, chaves.chave_publica)

    return {
        "algoritmo": algoritmo.name,
        "texto_original": texto,
        "mensagem_cifrada": serializar_cifrado(algoritmo.name, texto_cifrado),
        "chave_publica": serializar_chave(algoritmo.name, chaves.chave_publica),
        "chave_privada": serializar_chave(algoritmo.name, chaves.chave_privada),
    }


if __name__ == "__main__":
    import sys

    algoritmo_nome = sys.argv[1] if len(sys.argv) > 1 else "RSA"
    texto = sys.argv[2] if len(sys.argv) > 2 else "mensagem de teste"

    resultado = cifrar(algoritmo_nome, texto)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))