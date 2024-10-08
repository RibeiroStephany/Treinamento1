import openpyxl
import pandas as pd

def leitura_arquivo(arquivo):
    data_frame = pd.DataFrame
    data_frame = pd.read_excel(arquivo)
    return data_frame

def exibe_resultado(arquivo):
    df = leitura_arquivo(arquivo)
    print(df['Produtos'])
    total = df['Valor'].sum() / df['Valor'].count()
    print(total)