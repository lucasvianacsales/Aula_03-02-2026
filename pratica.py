import pandas as pd

dados = pd.read_excel("vendas.xlsx")

dados["valor_venda"] = dados["preco_unitario"]*dados["quantidade"]

# total_vendas_bruto = dados["valor_venda"].sum()
# media = dados["valor_venda"].mean()
# mediana = dados["valor_venda"].median()
# minimo = dados["valor_venda"].min()
# maximo = dados["valor_venda"].max()

# print(f"""
#     Receita total das vendas: R$ {total_vendas_bruto}
#     Média das vendas: R$ {media:.2f}
#     Menor venda: R$ {minimo}
#     Maior venda: R$ {maximo}
# """)

abaixo_1000 = (dados["valor_venda"] < 1000).sum()
abaixo_1000_per = (dados[dados["valor_venda"] < 1000].shape[0] / dados.shape[0])*100

dados.loc[(dados["valor_venda"] < 1000), "categoria"] = "abaixo"
dados.loc[(dados["valor_venda"] >= 1000) & (dados["valor_venda"] < 10000), "categoria"] = "intermed"
dados.loc[(dados["valor_venda"] >= 10000), "categoria"] = "acima"

print(f"{abaixo_1000} vendas foram abaixo de R$ 1.000,00 e isso representa {abaixo_1000_per}% das vendas")

acima = dados[dados["categoria"]=="acima"]
acima_per = (acima.shape[0] / dados.shape[0])*100

intermed_per = (dados[dados["categoria"]=="intermed"].shape[0] / dados.shape[0])*100

print(f"{acima.shape[0]} vendas foram acima de R$ 10.000,00 e isso representa {acima_per:.2f}% das vendas")

print(f"Vendas entre R$ 1.000,00 e 10.000,00 representam {intermed_per:.1f}% das vendas")

# print(dados.sample(20))

dados.loc[(dados["valor_venda"] >= 5000), "imposto"] = 15
dados.loc[(dados["valor_venda"] < 5000), "imposto"] = 10

dados["valor_liquido"] = (((100-dados["imposto"])*dados["valor_venda"])/100).round(2)

# print(dados[["valor_venda", "imposto", "valor_liquido"]])

dados.loc[(dados["idade"] < 30), "faixa_etaria"] = "Jovem"
dados.loc[(dados["idade"] >= 30) & (dados["idade"] < 50), "faixa_etaria"] = "Adulto"
dados.loc[(dados["idade"] >= 50), "faixa_etaria"] = "Sênior"

# print(dados[["idade", "faixa_etaria"]].sample(20))

total_vendas_bruto = dados["valor_venda"].sum()
total_vendas_liquido = dados["valor_liquido"].sum()

total_imposto = ((dados["valor_venda"]*dados["imposto"])/100).sum()

vendedores_unicos = dados["vendedor"].nunique()
clientes_unicos = dados["cliente"].nunique()

ticket_medio_liquido = dados["valor_liquido"].sum() / clientes_unicos

media = dados["valor_venda"].mean()
mediana = dados["valor_venda"].median()
minimo = dados["valor_venda"].min()
maximo = dados["valor_venda"].max()

faturamento_vendedor = dados.groupby("vendedor").agg(
    valor_venda = ("valor_venda", "sum"),
    valor_liquido = ("valor_liquido", "sum"),
    quantidade_vendas = ("valor_venda", "size")
)

faturamento_categoria = dados.groupby("categoria").agg(
    valor_venda = ("valor_venda", "sum"),
    valor_liquido = ("valor_liquido", "sum"),
    quantidade_vendas = ("valor_venda", "size")
)

faturamento_faixa_etaria = dados.groupby("faixa_etaria").agg(
    valor_venda = ("valor_venda", "sum"),
    valor_liquido = ("valor_liquido", "sum"),
    quantidade_vendas = ("valor_venda", "size")
)

print(f"""
    Receita total de vendas: R$ {total_vendas_bruto}
    Receita total de vendas sem impostos: R$ {total_vendas_liquido}
    Total de impostos: R$ {total_imposto:.2f}
    Número total de vendas: {dados.shape[0]}
    Média do valor de venda: R$ {media:.2f}
    Média do valor de venda liquido por cliente: R$ {ticket_medio_liquido:.2f}
    Menor venda: R$ {minimo}
    Maior venda: R$ {maximo}
""")

print(faturamento_vendedor)
print(faturamento_categoria)
print(faturamento_faixa_etaria)