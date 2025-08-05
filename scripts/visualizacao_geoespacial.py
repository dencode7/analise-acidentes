import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 1. Carregar os dados
# O dataset é grande, então vamos carregar apenas as colunas necessárias e uma amostra.
# file_path = '/home/daniel/Documentos/ProjetosPython/analise-acidentes/data/US_Accidents_March23.csv'
# df = pd.read_csv(file_path, usecols=['Start_Lat', 'Start_Lng', 'Severity', 'Start_Time', 'City'])

# Para facilitar, vamos usar o caminho relativo, pois é uma boa prática
file_path = '../data/US_Accidents_amostra.csv'
df = pd.read_csv(file_path, usecols=['Start_Lat', 'Start_Lng', 'Severity', 'Start_Time', 'City'])

# Exibir os dados originais
print("Dados originais (amostra):")
print(df.head())
print("-" * 50)
print("Informações sobre os dados:")
print(df.info())
print("-" * 50)


# 2. Limpeza de dados de localização
# Remover linhas com valores ausentes de Latitude e Longitude
df.dropna(subset=['Start_Lat', 'Start_Lng'], inplace=True)


# 3. Criar um mapa base
# O mapa será centralizado em um ponto médio dos dados dos EUA
mapa_acidentes = folium.Map(location=[df['Start_Lat'].mean(), df['Start_Lng'].mean()], zoom_start=4)


# 4. Plotar uma amostra dos acidentes no mapa
# Vamos usar uma amostra menor para que a renderização seja rápida
amostra_df = df.sample(n=10000)

# Usar MarkerCluster para agrupar os marcadores e evitar a poluição visual
marker_cluster = MarkerCluster().add_to(mapa_acidentes)

for index, row in amostra_df.iterrows():
    folium.Marker(
        location=[row['Start_Lat'], row['Start_Lng']],
        popup=f"Severidade: {row['Severity']}<br>Cidade: {row['City']}"
    ).add_to(marker_cluster)


# 5. Salvar o mapa em um arquivo HTML
output_file = '../reports/mapa_acidentes.html'
mapa_acidentes.save(output_file)

print(f"Mapa geoespacial criado com sucesso e salvo em '{output_file}'.")