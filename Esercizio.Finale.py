import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = 'C:/Users/sergi/OneDrive/Desktop/VSC_Python_Sergio/owid-covid-data.csv'

# Step 1

df = pd.read_csv(file_path)

# Verifica delle dimensioni e metadati del dataset
print("Dimensioni del dataset:", df.shape)
print("Metadati del dataset:")
print(df.info())
print("Prime righe del dataset:")
print(df.head())

# Step 2

# Filtraggio per continenti definiti
df_continents = df[df['continent'].notna()]

#  numero totale di casi per continente
total_cases_per_continent = df_continents.groupby('continent')['total_cases'].sum()
print("Numero totale di casi per continente:")
print(total_cases_per_continent)

# Step 3 comparazione

def compare_continents(continent1, continent2):

    data_cont1 = df_continents[df_continents['continent'] == continent1]
    data_cont2 = df_continents[df_continents['continent'] == continent2]

    # max e media per il primo continente
    max_cases_cont1 = data_cont1['total_cases'].max()
    mean_cases_cont1 = data_cont1['total_cases'].mean()
    sum_cases_cont1 = data_cont1['total_cases'].sum()

    # max e media per il secondo continente
    max_cases_cont2 = data_cont2['total_cases'].max()
    mean_cases_cont2 = data_cont2['total_cases'].mean()
    sum_cases_cont2 = data_cont2['total_cases'].sum()

    #  numero totale di casi nel mondo
    total_cases_world = df['total_cases'].sum()

    # Percentuali sul totale mondiale
    perc_cases_cont1 = (sum_cases_cont1 / total_cases_world) * 100
    perc_cases_cont2 = (sum_cases_cont2 / total_cases_world) * 100

    # risultati
    print(f"\\nConfronto tra {continent1} e {continent2}:")
    print(f"{continent1} - Massimo: {max_cases_cont1}, Media: {mean_cases_cont1}, Percentuale sul totale mondiale: {perc_cases_cont1:.2f}%")
    print(f"{continent2} - Massimo: {max_cases_cont2}, Media: {mean_cases_cont2}, Percentuale sul totale mondiale: {perc_cases_cont2:.2f}%")

# confronto
compare_continents('Europe', 'Asia')

# Step 4 cosa accade in Italia

# Filtraggio dei dati italiani nel 2022
italy_data_2022 = df[(df['location'] == 'Italy') & (df['date'].str.startswith('2022'))]

# ordiniamo date
italy_data_2022 = italy_data_2022.sort_values(by='date')

# Grafico dell'evoluzione dei casi totali
sns.set(style="darkgrid")
sns.lineplot(data=italy_data_2022, x='date', y='total_cases')
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Casi Totali')
plt.title('Evoluzione dei Casi Totali in Italia nel 2022')
plt.show()

# Grafico del numero di nuovi casi
sns.lineplot(data=italy_data_2022, x='date', y='new_cases')
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Nuovi Casi')
plt.title('Numero di Nuovi Casi in Italia nel 2022')
plt.show()

# Somma cumulativa dei nuovi casi
italy_data_2022['cumulative_new_cases'] = italy_data_2022['new_cases'].cumsum()

# Grafico dell'andamento cumulativo dei nuovi casi
sns.lineplot(data=italy_data_2022, x='date', y='cumulative_new_cases')
plt.xticks(rotation=45)
plt.xlabel('Data')
plt.ylabel('Cumulativo Nuovi Casi')
plt.title('Andamento Cumulativo dei Nuovi Casi in Italia nel 2022')
plt.show()

# Step 5

# Filtraggio dei dati da Maggio 2022 a Aprile 2023
icu_data = df[(df['location'].isin(['Italy', 'Germany', 'France'])) & 
              (df['date'] >= '2022-05-01') & 
              (df['date'] <= '2023-04-30')]

# Boxplot per il numero di pazienti in terapia intensiva
sns.boxplot(data=icu_data, x='location', y='icu_patients')
plt.xlabel('Nazione')
plt.ylabel('Pazienti in Terapia Intensiva')
plt.title('Confronto dei Pazienti in Terapia Intensiva (Maggio 2022 - Aprile 2023)')
plt.show()