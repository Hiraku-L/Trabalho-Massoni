import matplotlib.pyplot as mp

def grafico_encriptacao(df):
    mp.figure(figsize=(8, 5))

    for algoritmo in df["Algoritmo"].unique():
        dados = df[df["Algoritmo"] == algoritmo]

        mp.plot(
            dados["Entrada(bytes)"],
            dados["Tempo médio de encriptação(ms)"],
            marker="o",
            label=algoritmo
        )

    mp.xticks(sorted(df["Entrada(bytes)"].unique()))

    mp.xlabel("Entrada (bytes)")
    mp.ylabel("Tempo médio (ms)")
    mp.title("Tempo médio de encriptação")
    mp.grid(True)
    mp.legend()

    mp.savefig("grafico_encriptacao.png", dpi=300)
    mp.close()