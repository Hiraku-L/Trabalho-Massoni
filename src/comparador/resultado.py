from dataclasses import dataclass

@dataclass
class Resultado:
    algoritmo: str
    tamanho_entrada: int
    tempo_geracao_de_chaves: float
    media_encriptacao: float
    desvio_padrao_encriptacao: float
    media_decriptacao: float
    desvio_padrao_decriptacao: float
    tamanho_texto_cifrado: int