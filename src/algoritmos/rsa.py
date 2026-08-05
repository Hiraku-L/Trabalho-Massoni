from __future__ import annotations

from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

from .base import AlgorithmAdapter, KeyPair
from ..utils.separador_bytes import iterador_blocos


class Rsa():
    name = "RSA";

    def __init__(self, bits = 1024):
        self.bits = bits

    def gerar_chaves(self) -> KeyPair:
        chave_privada = RSA.generate(self.bits)
        chave_publica = chave_privada.public_key()
        return KeyPair(chave_publica, chave_privada) # chave simétrica
    
    def cifrar(self, texto: bytes, chave_publica : RSA.RsaKey) -> bytes:
        cifra = PKCS1_OAEP.new(chave_publica, hashAlgo=SHA256)
        tamanho_bloco = chave_publica.size_in_bytes() - 2 * SHA256.digest_size - 2
        return b"".join(cifra.encrypt(bloco) for bloco in iterador_blocos(texto, tamanho_bloco))
    
    def decifrar(self, texto_cifrado: bytes, chave_privada: RSA.RsaKey) -> bytes:
        cifra = PKCS1_OAEP.new(chave_privada, hashAlgo=SHA256)
        tamanho_bloco = chave_privada.size_in_bytes()
        return b"".join(cifra.decrypt(bloco) for bloco in iterador_blocos(texto_cifrado, tamanho_bloco))