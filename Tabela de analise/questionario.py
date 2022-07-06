from openpyxl import Workbook
import pandas as pd
print("A")
df = pd.read_excel("Tabela de analise/Classificação de vídeos.xlsx", sheet_name="Docente - Cleon")
print(df)

