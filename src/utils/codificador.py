from __future__ import annotations

import base64
import json

from Crypto.PublicKey.RSA import RsaKey

from ..algoritmos.gm import ChavePrivadaGm, ChavePublicaGm

def serializar_cifrado(algoritmo_nome: str, cifrado) -> str:
    if algoritmo_nome == "GM":
        return json.dumps(cifrado)
    return base64.b64encode(cifrado).decode("ascii")

def desserializar_cifrado(algoritmo_nome: str, texto: str):
    if algoritmo_nome == "GM":
        return json.loads(texto)
    return base64.b64decode(texto)

def serializar_chave(algoritmo_nome: str, chave) -> str:
    if isinstance(chave, RsaKey):
        return chave.export_key().decode("ascii") 

    if isinstance(chave, ChavePublicaGm):
        return json.dumps({"n": chave.n, "x": chave.x})

    if isinstance(chave, ChavePrivadaGm):
        return json.dumps({"p": chave.p, "q": chave.q})

    if isinstance(chave, (bytes, bytearray)):
        return base64.b64encode(chave).decode("ascii")

    raise TypeError(f"não sei serializar chave do tipo {type(chave)!r}")