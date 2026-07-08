import pandas as pd

def carregar_dataset(caminho):
    """
    Carrega o arquivo CSV e retorna um DataFrame.
    """
    df = pd.read_csv(caminho)
    return df