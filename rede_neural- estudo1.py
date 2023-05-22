import pandas as pd
import numpy as np
from sklearn.linear_model import SGDRegressor

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# dados = pd.read_csv("CSV/modelo5-final-media.csv")
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

dados = pd.read_csv("Mapa de calor/ExcelFinal/ResultadoMedia2 - TESTE.csv", delimiter=';',encoding='cp1250')

dados.head()
mapa = {
    "emoji " : "emoji"
}
dados = dados.rename(columns = mapa)
dados.head()

print("Rede Neural")
print("Classificação")

X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Dificuldade 1"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=10000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)
clf.predict_proba(X_test)

clf.predict(X_test)


clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"MLP - Taxa de acerto (Dificuldade 1) = {round(taxa_de_acerto * 100, 2)}")



X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Densidade semântica 1"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=1000000).fit(X_train, y_train)
# clf = MLPClassifier(alpha=1e-05, hidden_layer_sizes=(5, 2), random_state=1,
#               solver='lbfgs').fit(X_train, y_train)

clf.predict_proba(X_test)

clf.predict(X_test)

clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"MLP - Taxa de acerto (Densidade Semantica 1) = {round(taxa_de_acerto * 100, 2)}")


X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Dificuldade 2"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=10000000).fit(X_train, y_train)
clf.predict_proba(X_test)
clf.predict(X_test)
clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"MLP - Taxa de acerto (Dificuldade 2) = {round(taxa_de_acerto * 100, 2)}")


X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Densidade semântica 2"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=5)

clf = MLPClassifier(random_state=5, max_iter=1000000).fit(X_train, y_train)
clf.predict_proba(X_test)
clf.predict(X_test)
clf.score(X_test, y_test)

taxa_de_acerto = clf.score(X_test, y_test)
print(f"MLP - Taxa de acerto (Densidade Semantica 2) = {round(taxa_de_acerto * 100, 2)}")


print("Regressão")

X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Dificuldade 1"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=5)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Dificuldade 1): {erro}")


X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Densidade semântica 1"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=5)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Densidade Semantica 1): {erro}")


X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]]
y = dados["Dificuldade 2"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=5)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Dificuldade 2): {erro}")


X = dados[["Tristeza", "Alegria", "Medo", "Aversao", "Raiva", "Pontuacao", "Resumo"]].values
y = dados["Densidade semântica 2"]

X_train, X_test, y_train, y_test = train_test_split(X, y,  test_size=0.30, random_state=5)
regr = make_pipeline(StandardScaler(), SGDRegressor(max_iter=1000, tol=1e-3)).fit(X_train, y_train)
label = regr.predict(X_test)
a = y_test - label
diferenca = np.absolute(a)
erro = np.square(np.subtract(y_test, label)).mean()
print(f"SGD - ERRO QUADÁTICO MÉDIO (Densidade Semantica 2): {erro}")