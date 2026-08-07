import matplotlib.pyplot as mp

def grafico_tamanho_saida(df):
    mp.figure(figsize=(8, 5))

    for algoritmo in df["Algoritmo"].unique():
        dados = df[df["Algoritmo"] == algoritmo]

        mp.plot(
            dados["Entrada(bytes)"],
            dados["Texto cifrado(bytes)"],
            marker="o",
            label=algoritmo
        )

    mp.xticks(sorted(df["Entrada(bytes)"].unique()))

    mp.xlabel("Entrada (bytes)")
    mp.ylabel("Tamanho (bytes)")
    mp.title("Tamanho do texto cifrado")
    mp.grid(True)
    mp.legend()

    mp.savefig("grafico_tam_texto_cifrado.png", dpi=300)
    mp.close()