import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Pokemon.csv')

print(df.head())


df_filtered = df[df['legendary'] == False]

plt.figure(figsize=(12, 6))
sns.boxplot(data=df_filtered, x='generation', y='total', palette='Set2')
plt.title('Total de CP por geração (apenas não lendários)')
plt.xlabel('Geração')
plt.ylabel('Total de CP')
plt.show()