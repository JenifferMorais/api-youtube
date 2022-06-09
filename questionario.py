from openpyxl import Workbook
import pandas as pd
print("A")
df = pd.read_excel("Classificação de vídeos.xlsx", sheet_name="Docente - Cleon")
print(df)

