import argparse
from utils.constantes import TAMANHOS, RSA, GM

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--sizes",
        help="Tamanhos das entradas a serem testadas em bytes",
        default=TAMANHOS
    )
    parser.add_argument(
        "--rsa-bits",
        help="Tamnho da chave rsa em bits",
        default=RSA
    )
    parser.add_argument(
        "--gm-bits",
        help="Tamanho da chave GM em bits",
        default=GM
    )
    args = parser.parse_args(argv)