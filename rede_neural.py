import pandas as pd
import numpy as np

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# dados = pd.read_csv("CSV/modelo5-final-media.csv")
dados = pd.read_csv("CSV/modelo5-final-media (4).csv", delimiter=';',encoding='cp1250')

dados.head()
mapa = {
    "emoji " : "emoji"
}
dados = dados.rename(columns = mapa)
dados.head()

print("Rede Neural")
print("Classificação")

X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres", "codigo", "opiniao", "emoji","tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]]
y = dados["dificuldade"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=10000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)
clf.predict_proba(X_test)

clf.predict(X_test)

clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"Taxa de acerto (Dificuldade) = {round(taxa_de_acerto * 100, 2)}")



X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres", "codigo", "opiniao", "emoji","tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]].values
y = dados["densidade semantica"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=1000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)

clf.predict_proba(X_test)

jenn = clf.predict(X_test)

clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"Taxa de acerto (Densidade Semantica) = {round(taxa_de_acerto * 100, 2)}")


print("Regressão")

X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres", "codigo", "opiniao", "emoji","tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]]
y = dados["dificuldade"].values


X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.70, random_state=5)
regr = MLPRegressor(random_state=1, max_iter=1000000).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"ERRO QUADÁTICO MÉDIO (Dificuldade): {erro}")


X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres", "codigo", "opiniao", "emoji","tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]]
y = dados["densidade semantica"].values

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.70, random_state=5)
regr = MLPRegressor(random_state=1, max_iter=1000000).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"ERRO QUADÁTICO MÉDIO (Densidade Semantica): {erro}")