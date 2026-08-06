from __future__ import annotations

from Crypto.Random import random
from Crypto.Util.number import GCD, getPrime

def primo_de_blum(bits):
    while True:
        resp = getPrime(bits)
        if resp % 4 == 3:
            return resp

def simbolo_legendre(a, p):
    valor = pow(a, (p-1) // 2, p)
    if valor == p-1:
        return -1
    return valor


def nao_residuo_quadratico(p, q, n):
    while True:
        resp = random.randrange(2,n-1)
        if GCD(resp, n) != 1:
            continue
        if simbolo_legendre(resp, p) == -1 and simbolo_legendre(resp, q) == -1:
            return resp


def random_unit(n):
    while True:
        y = random.randrange(2, n-1)
        if GCD(y,n) == 1:
            return y


def bytes_para_bits(data):
    bits = []
    for byte in data:
        for shift in range(7, -1, -1):
            bits.append((byte >> shift) & 1)
    return bits


def bits_para_bytes(bits: list[int]):
    if len(bits) % 8 != 0:
        raise ValueError("A quantidade de bits precisa ser múltipla de 8.")

    resp = bytearray()
    for i in range(0, len(bits), 8):
        valor = 0
        for bit in bits[i : i+ 8]:
            valor = (valor << 1) | bit
        resp.append(valor)
    return bytes(resp)