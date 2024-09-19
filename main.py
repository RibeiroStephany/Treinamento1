import openpyxl
import pandas as pd

data_frame = pd.DataFrame
data_frame = pd.read_excel('produtos.xlsx')
print(data_frame['Produto'])
total = data_frame['Valor'].sum() / data_frame['Valor'].count()
print(total)