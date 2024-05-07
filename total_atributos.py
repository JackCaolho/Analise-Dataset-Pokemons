import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Pokemon.csv')
print(df.head())

#Funçao para boxplot
def plot_boxplot_legendary(df):
    # Tiltros
    df_filtered = df[df['legendary'] == False]

    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_filtered, x='generation', y='total', palette='Set2')
    plt.title('Total de CP por geração (apenas não lendários)')
    plt.xlabel('Geração')
    plt.ylabel('Total de CP')
    plt.show()

#Funçao para heatmap
def plot_heatmap(df):
    # Dados
    columns = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']
    correlation_matrix = df[columns].corr()

    # Cores / Tamanho / Scala
    cmap = sns.diverging_palette(220, 20, as_cmap=True)
    plt.figure(figsize=(10, 8)) 
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.title('Matriz de Correlação das Estatísticas dos Pokémon')
    plt.show()


plot_heatmap(df)
plot_boxplot_legendary(df)


