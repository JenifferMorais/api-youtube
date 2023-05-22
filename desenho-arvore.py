import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib
from sklearn.neural_network import MLPClassifier


from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree

# dados = pd.read_csv("CSV/modelo5-final-media.csv")
dados = pd.read_excel("CSV/teste/1-2 e 1-3/dados.xlsx")

mapa = {
    "emoji " : "emoji"
}
dados = dados.rename(columns = mapa)

print("Árvore de decisão")
print("Classificação")

X = dados[["tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]]

y = dados["dificuldade"]



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.80, random_state=5)
clf = tree.DecisionTreeClassifier(max_depth=3).fit(X_train, y_train)

y_true = clf.predict(X_test)
taxa_de_acerto = accuracy_score(y_test, y_true)
print(f"Taxa de acerto (Dificuldade) = {round(taxa_de_acerto * 100, 2)}")

fn=["tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]
fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (14,14), dpi=600)
tree.plot_tree(clf,feature_names=fn,class_names=["Fácil", "Médio ou Difícil"]);
fig.savefig('imagename2.png')
