from __future__ import annotations

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from .base import AlgoritmoBase, KeyPair

class Des(AlgoritmoBase):
    name = "DES"

    # está sendo usado o modo ECB afins de comparação com os outros algoritmos, na prática esse metodo não é muito viavel pois mantem os padrões no conteúdo, o que não garante confidencialidade

    def gerar_chaves(self) -> KeyPair:
        chave = get_random_bytes(8)
        return KeyPair(chave, chave) # chave simétrica
    
    def cifrar(self, texto: bytes, chave_publica : bytes) -> bytes:
        cifra = DES.new(chave_publica, DES.MODE_ECB)
        return cifra.encrypt(pad(texto,DES.block_size))
    
    def decifrar(self, texto_cifrado: bytes, chave_privada: bytes) -> bytes:
        cifra = DES.new(chave_privada, DES.MODE_ECB)
        return unpad(cifra.decrypt(texto_cifrado), DES.block_size)