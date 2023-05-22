import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

from sklearn.neural_network import MLPClassifier


from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree

# dados = pd.read_csv("CSV/modelo5-final-media.csv")
dados = pd.read_csv("CSV/teste/1-2 e 1-3/dados.csv", delimiter=';',encoding='cp1250', index_col=False)

mapa = {
    "emoji " : "emoji"
}
dados = dados.rename(columns = mapa)

print("Árvore de decisão")
print("Classificação")

X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["dificuldade"]


X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.30, random_state=4)

clf = tree.DecisionTreeClassifier().fit(X_train, y_train)

y_true = clf.predict(X_test)
taxa_de_acerto = accuracy_score(y_test, y_true)
print(f"Taxa de acerto (Dificuldade) = {round(taxa_de_acerto * 100, 2)}")



X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["densidade semantica"]


X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.30, random_state=4)

y_true = clf.predict(X_test)
taxa_de_acerto = accuracy_score(y_test, y_true)
print(f"Taxa de acerto (densidade semantica) = {round(taxa_de_acerto * 100, 2)}")

print("Regressão")

X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["dificuldade"].values

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=4)
regr = tree.DecisionTreeRegressor().fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"ERRO QUADÁTICO MÉDIO (Dificuldade): {erro}")


X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["densidade semantica"].values

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=4)
regr = tree.DecisionTreeRegressor().fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"ERRO QUADÁTICO MÉDIO  (Densidade Semantica): {erro}")