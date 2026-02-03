import pandas as pd

dados = pd.read_excel("vendas.xlsx")

dados["valor_total"] = dados["preco_unitario"]*dados["quantidade"]

total = dados["valor_total"].sum()

media = dados["valor_total"].mean()

mediana = dados["valor_total"].median()

minimo = dados["valor_total"].min()

maximo = dados["valor_total"].max()

print(f"""
    Receita total das vendas: R$ {total}
    Média das vendas: R$ {media:.2f}
    Menor venda: R$ {minimo}
    Maior venda: R$ {maximo}
""")

abaixo_1000 = (dados["valor_total"] < 1000).sum()
abaixo_1000_per = (dados[dados["valor_total"] < 1000].shape[0] / dados.shape[0])*100

print(f"{abaixo_1000} das vendas foram abaixo de R$ 1.000,00 e isso representa {abaixo_1000_per}% das vendas")

print(dados)