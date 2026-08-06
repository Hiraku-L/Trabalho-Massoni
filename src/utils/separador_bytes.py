from __future__ import annotations


def iterador_blocos(data: bytes, bloco_bytes: int):
    if bloco_bytes <= 0:
        raise ValueError("o tamanho do bloco de bytes precisa ser maior que zero.")

    for index in range(0, len(data), bloco_bytes):
        yield data[index : index + bloco_bytes]