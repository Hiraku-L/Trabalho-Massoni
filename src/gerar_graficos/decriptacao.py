import matplotlib.pyplot as mp

def grafico_decriptacao(df):
    mp.figure(figsize=(8, 5))

    for algoritmo in df["Algoritmo"].unique():
        dados = df[df["Algoritmo"] == algoritmo]

        mp.plot(
            dados["Entrada(bytes)"],
            dados["Tempo médio de decriptação(ms)"],
            marker="o",
            label=algoritmo
        )

    mp.xticks(sorted(df["Entrada(bytes)"].unique()))

    mp.xlabel("Entrada (bytes)")
    mp.ylabel("Tempo médio (ms)")
    mp.title("Tempo médio de decriptação")
    mp.grid(True)
    mp.legend()

    mp.savefig("grafico_decriptacao.png", dpi=300)
    mp.close()