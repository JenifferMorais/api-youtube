import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def inicio():
    df = pd.read_csv("ExcelFinal/resultadoSemMedia.csv", delimiter=';', encoding='cp1250')
    df.head()


    # df2 = df.loc[:, 'Densidade semântica 1:':'Resumo']
    df2 = df;
    df2.head()


    df2.corr()



    df2.corr().style.background_gradient(cmap='Blues')
    sns.heatmap(df2.corr())

    df2.corr().style.background_gradient(cmap='Blues')
    fig, ax = plt.subplots(figsize=(15,18))

    ax = (sns.heatmap(df2.corr(), cmap='Blues', linewidth=0.5, annot=True))

    fig = ax.get_figure()
    fig.savefig('mapa-modelo3.png')

if __name__ == '__main__':
    inicio()

