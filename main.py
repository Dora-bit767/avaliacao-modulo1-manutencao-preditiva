from src.carregar_dados import carregar_dataset

# Caminho do dataset
caminho = "data/manutencao_preditiva.csv"

# Carrega o arquivo
df = carregar_dataset(caminho)

print(df.head())