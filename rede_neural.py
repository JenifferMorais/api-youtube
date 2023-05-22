import pandas as pd
import numpy as np
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import accuracy_score

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# dados = pd.read_csv("CSV/modelo5-final-media.csv")
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

dados = pd.read_csv("CSV/teste/1-2 e 1-3/dados.csv", delimiter=';',encoding='cp1250')

dados.head()
mapa = {
    "emoji " : "emoji"
}
dados = dados.rename(columns = mapa)
dados.head()

print("Rede Neural")
print("Classificação")

X = dados[["tristeza", "alegria", "medo", "aversao", "raiva", "pontuacao", "resultado"]]
y = dados["dificuldade"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=15)

clf = MLPClassifier(random_state=5, max_iter=10000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)
y_true = clf.predict(X_test)
taxa_de_acerto = accuracy_score(y_test, y_true)
print(f"MLP - Taxa de acerto (Dificuldade) = {round(taxa_de_acerto * 100, 2)}")



X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["densidade semantica"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=15)

clf = MLPClassifier(random_state=5, max_iter=1000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)

y_true = clf.predict(X_test)
taxa_de_acerto = accuracy_score(y_test, y_true)
print(f"MLP - Taxa de acerto (Densidade Semantica) = {round(taxa_de_acerto * 100, 2)}")


print("Regressão")

X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["dificuldade"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=15)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Dificuldade): {erro}")


X = dados[["visualizacoes", "like", "deslikes", "like comentarios", "qtd caracteres"]]
y = dados["densidade semantica"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=15)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Densidade Semantica): {erro}")