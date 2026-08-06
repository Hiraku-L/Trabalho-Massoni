from __future__ import annotations

from dataclasses import dataclass

from ..utils import teoria_dos_numeros as tn
from .base import AlgoritmoBase, KeyPair


@dataclass(frozen=True)
class ChavePublicaGm:
    n: int
    x: int


@dataclass(frozen=True)
class ChavePrivadaGm:
    p: int
    q: int

class Gm(AlgoritmoBase):
    name = "GM"

    def __init__(self, bits: int = 512) -> None:
        self.bits = bits

    def gerar_chaves(self) -> KeyPair:
        metade_bits = max(32, self.bits // 2)
        p = tn.primo_de_blum(metade_bits)
        q = tn.primo_de_blum(metade_bits)
        while p == q:
            q = tn.primo_de_blum(metade_bits)
        n = p * q
        x = tn.nao_residuo_quadratico(p,q,n)
        return KeyPair(ChavePublicaGm(n,x), ChavePrivadaGm(p,q))
    
    def cifrar(self, texto: bytes, chave_publica : ChavePublicaGm) -> list[int]:
        bits = tn.bytes_para_bits(texto)
        texto_cifrado = []
        for bit in bits:
            y = tn.random_unit(chave_publica.n)
            c = pow(y, 2, chave_publica.n)
            if bit:
                c = (c*chave_publica.x) % chave_publica.n

            texto_cifrado.append(c)
        return texto_cifrado
        
    def decifrar(self, texto_cifrado: bytes, chave_privada: ChavePrivadaGm) -> bytes:
        bits = []
        for c in texto_cifrado:
            eh_residuo_p = tn.simbolo_legendre(c, chave_privada.p) == 1
            eh_residuo_q = tn.simbolo_legendre(c, chave_privada.q) == 1
            if eh_residuo_p and eh_residuo_q:
                bits.append(0)
            else:
                bits.append(1)
        return tn.bits_para_bytes(bits)


    def tamanho_texto_cifrado(self, texto_cifrado: list[int], chave_publica: ChavePublicaGm | None = None):
        if chave_publica is None:
            raise ValueError("GM precisa de uma chave pública para calcular o tamanho do texto codificado")
        return len(texto_cifrado) * max(1, (chave_publica.n.bit_length() + 7) // 8)