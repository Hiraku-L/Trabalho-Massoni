import argparse
import csv
from dataclasses import asdict
from .utils.constantes import TAMANHOS, RSA, GM, ALGORITMOS
from .comparador.comparador import comparar

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
        default=20
    )
    
    args = parser.parse_args(argv)

    print(args.sizes, args.rsa_bits, args.gm_bits, ALGORITMOS, args.repetitions)

    resultados = comparar(args.sizes, args.rsa_bits, args.gm_bits, ALGORITMOS, args.repetitions)

    __salvar_resultado(resultados)

def __salvar_resultado(resultados):
    with open("benchmark.csv", "w", newline="") as arquivo:
        wr = csv.DictWriter(arquivo, fieldnames=asdict(resultados[0]).keys())

        wr.writeheader()

        for resultado in resultados:
            wr.writerow(asdict(resultado))