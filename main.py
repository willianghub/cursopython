import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.DataFrame({
    'Nome': ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda'],
    'Idade': [25, 40, 35, 28, 50, 32],
    'Profissão': ['Analista', 'Gerente', 'Vendedor', 'Analista', 'Diretor', 'Vendedor'],
    'Salário': [3000, 8000, 4000, 3500, 15000, 4500],
    'Limite de crédito': [5000, 12000, 6000, 5500, 25000, 7000],
    'Historico_Inadimplencia': [0, 1, 0, 0, 1, 0],
    'Estado civil': ['Solteiro', 'Casado', 'Casado', 'Solteiro', 'Casado', 'Solteiro'],
    'Imovel_Proprio': [0, 1, 0, 0, 1, 0]
})

dados['Limite_Alto'] = dados['Limite de crédito'] > dados['Limite de crédito'].quantile(0.75)

# Gráfico 1: Scatterplot Salário vs Limite de Crédito
# Justificativa: Este gráfico mostra visualmente a relação entre salário e limite de crédito,
# destacando quem está acima do 3º quartil (Limite_Alto). A coloração facilita a identificação
# de padrões e possíveis impulsionadores do crédito elevado.
plt.figure(figsize=(8,6))
sns.scatterplot(data=dados, x='Salário', y='Limite de crédito', hue='Limite_Alto', palette='coolwarm')
plt.title('Salário vs Limite de Crédito')
plt.show()

# Gráfico 2: Barplot da Média de Limite de Crédito por Profissão
# Justificativa: Permite comparar as médias de limite de crédito entre diferentes profissões.
# Identifica categorias que, possivelmente, têm maior acesso ao crédito por status ou renda.
plt.figure(figsize=(8,6))
sns.barplot(data=dados, x='Profissão', y='Limite de crédito', ci=None)
plt.title('Média do Limite de Crédito por Profissão')
plt.xticks(rotation=45)
plt.show()

# Gráfico 3: Boxplot de Limite de Crédito por Histórico de Inadimplência
# Justificativa: Mostra a dispersão dos limites entre quem teve ou não inadimplência.
# Útil para verificar se o histórico negativo influencia a concessão de crédito.
plt.figure(figsize=(8,6))
sns.boxplot(data=dados, x='Historico_Inadimplencia', y='Limite de crédito')
plt.title('Limite de Crédito por Histórico de Inadimplência')
plt.xlabel('Histórico de Inadimplência (0 = Nunca, 1 = Já teve)')
plt.show()