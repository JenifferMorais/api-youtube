import os
import folium
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from folium.plugins import HeatMap
from geopy.geocoders import Nominatim
def inicio():
    # with open('resultado.csv') as f:
    #     print(f)

    df = pd.read_csv("resultado.csv", encoding='cp1250', nrows=5)
    df.head()

    df_2 = df.select_dtypes(exclude='object')
    df_2.head()

    sns.heatmap(df_2.corr())



    fig, ax = plt.subplots(figsize=(12, 8))

    _ = sns.heatmap(df_2.corr(), cmap='Blues', linewidth=0.5, annot=True)

if __name__ == '__main__':
    inicio()

