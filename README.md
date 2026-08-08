# Trabalho Massoni

Projeto desenvolvido para análise e comparação de algoritmos de criptografia, utilizando **DES, RSA e Goldwasser-Micali (GM)**.

O programa realiza testes de desempenho dos algoritmos para diferentes tamanhos de entrada, medindo os tempos de geração de chaves, encriptação e decriptação, além do tamanho do texto cifrado. Os resultados são armazenados em uma tabela e utilizados para gerar gráficos comparativos.

# Como executar

### Gerar os resultados e gráficos

Para executar os benchmarks, gerar a tabela com os resultados e criar os gráficos, basta executar:

```bash
python3 main.py
```

O programa irá gerar/atualizar o arquivo `benchmark.csv` e os gráficos de:

* Tempo de encriptação;
* Tempo de decriptação;
* Tamanho do texto cifrado.

### Criptografar um texto

Também é possível utilizar o programa para criptografar uma mensagem diretamente pela linha de comando:

```bash
python3 cifrador.py nomeDoAlgoritmo "mensagem desejada"
```

Por exemplo:

```bash
python3 cifrador.py DES "projeto de massoni"
```

O programa irá exibir o **texto criptografado**, a **chave pública** e a **chave privada** utilizadas pelo algoritmo.

## Algoritmos

O projeto possui implementações dos seguintes algoritmos:

* **DES**
* **RSA**
* **Goldwasser-Micali (GM)**
