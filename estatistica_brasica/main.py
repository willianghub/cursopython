import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("MODULO7_PROJETOFINAL_BASE_SUPERMERCADO - MODULO7_PROJETOFINAL_BASE_SUPERMERCADO.csv.csv")

df.head(10)

#1 - Traga a média e a mediana dos preços - coluna Preco_Normal - por categoria de produto.
#Identifique as categorias que parecem ter um valor de média abaixo ou acima da mediana.

media_por_categoria = df.groupby("Categoria")["Preco_Normal"].mean()
print("Média por categoria:")
print(media_por_categoria)

mediana_por_categoria = df.groupby("Categoria")["Preco_Normal"].median()
print("\nMediana por categoria:")
print(mediana_por_categoria)

##2 - Traga o desvio padrão por categoria de produto.
##Qual o comportamento da média e mediana nas categorias com maior desvio?

desvio_padrao = df.groupby("Categoria")["Preco_Normal"].std()
print("Desvio padrão por categoria:")
print(desvio_padrao)

##3 - Plot um boxplot da distribuição do Preco_Normal para a categoria que você identificou que tem o maior desvio padrão.
##Como é a distribuição desses dados segundo o boxplot? Você identifica muitos outliers?

categoria_mais_dispersao = desvio_padrao.idxmax()

df_categoria = df[df["Categoria"] == categoria_mais_dispersao]

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 5))
plt.boxplot(df_categoria["Preco_Normal"])
plt.title(f"Boxplot do Preço Normal - Categoria: {categoria_mais_dispersao}")
plt.ylabel("Preço Normal")
plt.grid(True)
plt.show()

##4 - Plote um gráfico de barras onde temos a média de descontos por categoria.

media_desconto = df.groupby("Categoria")["Desconto"].mean().sort_values()

media_desconto.plot(kind="barh", figsize=(8, 6), title="Média de Desconto por Categoria")
plt.xlabel("Desconto Médio")
plt.ylabel("Categoria")
plt.grid(True)
plt.tight_layout()
plt.show()

##5 - Plote um gráfico de mapa interativo agrupando os dados por
##categoria, marca e trazendo a média de desconto.


grupo = df.groupby(["Categoria", "Marca"], as_index=False)["Desconto"].mean()


fig = px.sunburst(grupo, path=["Categoria", "Marca"], values="Desconto",
                  title="Média de Desconto por Categoria e Marca")
fig.show()