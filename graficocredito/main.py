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

limite_alto = dados['Limite de crédito'].quantile(0.75)
dados['Limite_Alto'] = dados['Limite de crédito'] > limite_alto

plt.figure(figsize=(8,6))
sns.scatterplot(data=dados, x='Salário', y='Limite de crédito', hue='Limite_Alto', palette='coolwarm')
plt.title('Salário vs Limite de Crédito')
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(data=dados, x='Profissão', y='Limite de crédito', ci=None)
plt.title('Média do Limite de Crédito por Profissão')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(data=dados, x='Historico_Inadimplencia', y='Limite de crédito')
plt.title('Limite de Crédito por Histórico de Inadimplência')
plt.xlabel('Histórico de Inadimplência (0 = Nunca, 1 = Já teve)')
plt.show()