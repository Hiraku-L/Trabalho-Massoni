import os
import numpy as np
from time import perf_counter
from .resultado import Resultado

def calcula_media_e_desvio_padrao(funcao, repeticoes):
    tempos = []

    for i in range(repeticoes):
        tempo = medir_tempo(funcao)
        tempos.append(tempo)

    media = round(np.mean(tempos), 4)
    desvio_padrao = round(np.std(tempos), 4)

    return media, desvio_padrao

def medir_tempo(funcao):
    inicio = perf_counter()
    funcao()
    fim = perf_counter()

    duracao = fim - inicio

    return round(duracao * 1000, 4)

def comparar(tamanhos, algoritmos, repeticoes):
    resultados = []

    for algoritmo in algoritmos:
        chaves = algoritmo.gerar_chaves()
        tempo_geracao_de_chaves = medir_tempo(lambda: algoritmo.gerar_chaves())

        for tamanho in tamanhos:
            texto = os.urandom(tamanho)

            texto_cifrado = algoritmo.cifrar(texto, chaves.chave_publica)
            tempos_encriptacao = calcula_media_e_desvio_padrao(lambda: algoritmo.cifrar(texto, chaves.chave_publica), repeticoes)
            media_encriptacao, desvio_padrao_encriptacao = tempos_encriptacao

            tempos_decriptacao = calcula_media_e_desvio_padrao(lambda: algoritmo.decifrar(texto_cifrado, chaves.chave_privada), repeticoes)
            media_decriptacao, desvio_padrao_decriptacao = tempos_decriptacao

            tamanho_texto_cifrado = algoritmo.tamanho_texto_cifrado(texto_cifrado, chaves.chave_publica)

            resultados.append(
                Resultado(
                    algoritmo= algoritmo.name,
                    tamanho_entrada= tamanho,
                    tempo_geracao_de_chaves= tempo_geracao_de_chaves,
                    media_encriptacao= media_encriptacao,
                    desvio_padrao_encriptacao= desvio_padrao_encriptacao,
                    media_decriptacao= media_decriptacao,
                    desvio_padrao_decriptacao= desvio_padrao_decriptacao,
                    tamanho_texto_cifrado= tamanho_texto_cifrado,
                )
            )

    return resultados