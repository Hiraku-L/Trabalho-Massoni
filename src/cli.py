import argparse
import csv
from dataclasses import asdict
from .utils.constantes import TAMANHOS, RSA, GM
from .comparador.comparador import comparar
from .algoritmos.des import Des
from .algoritmos.rsa import Rsa
from .algoritmos.gm import Gm

def main(argv: list[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sizes",
        help="Tamanhos das entradas a serem testadas em bytes",
        type=int,
        nargs="+",
        default=TAMANHOS
    )
    parser.add_argument(
        "--rsa-bits",
        help="Tamanho da chave rsa em bits",
        default=RSA
    )
    parser.add_argument(
        "--gm-bits",
        help="Tamanho da chave GM em bits",
        default=GM
    )
    parser.add_argument(
        "--repetitions",
        help="Quantidade de vezes que cada algoritmo roda para cada tamanho de entrada",
        type=int,
        default=20
    )
    
    args = parser.parse_args(argv)

    algoritmos = [
        Des(),
        Gm(args.gm_bits),
        Rsa(args.rsa_bits)
    ]

    resultados = comparar(args.sizes, algoritmos, args.repetitions)

    __salvar_resultado(resultados)

def __salvar_resultado(resultados):
    with open("benchmark.csv", "w", newline="", encoding="utf-8") as arquivo:
        wr = csv.writer(arquivo)

        wr.writerow([
            "Algoritmo",
            "Entrada(bytes)",
            "Tempo de geração de chaves(ms)",
            "Tempo médio de encriptação(ms)",
            "Desvio padrão de encriptação(ms)",
            "Tempo médio de decriptação(ms)",
            "Desvio padrão da decriptação(ms)",
            "Texto cifrado(bytes)"
        ])

        for resultado in resultados:
            wr.writerow(asdict(resultado).values())