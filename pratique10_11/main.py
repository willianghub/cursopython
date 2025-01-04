#Leia o arquivo ‘ecommerce.csv’ dentro de um dataframe .

#Faça uma análise detalhada dos dados, descubra quais dados gostaria de destacar e crie
#os seguintes gráficos:

#Gráfico de Histograma

#Gráfico de dispersão

#Mapa de calor

#Gráfico de barra

#Gráfico de pizza

#Gráfico de densidade

#Gráfico de Regressão

#Adicione títulos nos gráficos e nos eixos para ficar claro os objetivos dos gráficos#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('ecommerce.csv')

mapa_genero = {
    'masculino': 'masculino',
    'bebês': 'bebês',
    'meninos': 'meninos',
    'menino': 'meninos',
    'bermuda feminina brilho blogueira': 'feminino',
    'meninas': 'meninas',
    'roupa para gordinha pluss p ao 52': 'feminino',
    'short menina verao look mulher': 'feminino',
    'feminino': 'feminino',
    'mulher': 'feminino',
    'sem gênero': 'sem gênero',
    'unissex': 'sem gênero',
    'sem gênero infantil': 'sem gênero'
}

df['Gênero'] = df['Gênero'].replace(mapa_genero)

sns.set(style="whitegrid")

plt.figure(figsize=(10,6))
sns.scatterplot(x='N_Avaliações', y='Nota', data=df, alpha=0.7)
plt.xscale('log')  # Adicionar escala logarítmica
plt.title('Gráfico de Dispersão - Nota vs. Número de Avaliações (Escala Log)', fontsize=14)
plt.xlabel('Número de Avaliações (Escala Logarítmica)', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.regplot(x='N_Avaliações', y='Nota', data=df, scatter_kws={"alpha":0.3}, line_kws={"color":"red"})
plt.xscale('log')  # Adicionar escala logarítmica
plt.title('Gráfico de Regressão - Nota vs. Número de Avaliações', fontsize=14)
plt.xlabel('Número de Avaliações (Escala Logarítmica)', fontsize=12)
plt.ylabel('Nota', fontsize=12)
plt.tight_layout()
plt.show()

numeric_df = df.select_dtypes(include=['float64', 'int64'])

plt.figure(figsize=(12,8))
heatmap = sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5, vmin=-1, vmax=1)
heatmap.set_title('Mapa de Calor - Correlação das Variáveis Numéricas', fontsize=16)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12,6))
df['Marca'].value_counts().head(10).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Marcas mais Comuns', fontsize=14)
plt.xlabel('Marca', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,8))

genero_counts = df['Gênero'].value_counts()

generos_desejados = ['feminino', 'masculino', 'bebês', 'sem gênero', 'meninos', 'meninas']

for genero in generos_desejados:
    if genero not in genero_counts:
        genero_counts[genero] = 0

genero_filtrado = genero_counts[generos_desejados]

genero_filtrado.plot(
    kind='pie',
    autopct='%1.1f%%',
    startangle=90,
    colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'][:len(genero_filtrado)],
    explode=[0.05] * len(genero_filtrado),  # Adicionar explode para todas as fatias
    pctdistance=0.85  # Ajuste a distância do percentual
)

plt.title('Distribuição por Gênero (Filtrado)', fontsize=16)

plt.ylabel('')

plt.tight_layout()

plt.show()

df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')

plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'].dropna(), fill=True, color="green", bw_adjust=0.5)  # Substituir 'shade' por 'fill'
plt.title('Gráfico de Densidade - Notas dos Produtos', fontsize=14)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Densidade', fontsize=12)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df['Nota'].dropna(), bins=20, kde=False, color="purple")
plt.title('Histograma - Distribuição das Notas', fontsize=14)
plt.xlabel('Nota', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()
