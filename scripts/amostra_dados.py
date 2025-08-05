import pandas as pd

file_path = '../data/US_Accidents_March23.csv'
output_path = '../data/US_Accidents_amostra.csv'

# Carregar apenas 100,000 linhas do arquivo grande
# A amostra será aleatória e o tamanho do arquivo será reduzido
df_amostra = pd.read_csv(file_path, nrows=100000)

# Salvar a amostra em um novo arquivo CSV
df_amostra.to_csv(output_path, index=False)

print(f"Amostra de dados criada com sucesso em '{output_path}'.")