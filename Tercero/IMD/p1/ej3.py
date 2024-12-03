from sklearn import preprocessing
from ucimlrepo import fetch_ucirepo
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from generar_graficos import generarGrafico




def precisionDataset(features, label, modelo):
     precision =0
     X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=1)
     modelo.fit(X_train,y_train)
     y_pred = modelo.predict(X_test)
     precision = accuracy_score(y_test,y_pred)
     return precision




datasets=[]
# Creamos el modelo del árbol de decisión 

datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))

arbol_error_norm =[];knn_error_norm = []; X_norm = []
arbol_error_estand =[];knn_error_estand = []; X_estand = []

# Normalizacion de los datos
for elemento in datasets:
    X = elemento.data.features  # Características
    y = elemento.data.targets.values.flatten()  # Etiquetas como un array

    X_norm = (preprocessing.normalize(X))
    X_estand = (preprocessing.scale(X))

    arbol_error_norm.append(1-precisionDataset(X_norm, y, DecisionTreeClassifier()))
    knn_error_norm.append(1-precisionDataset(X_norm, y, KNeighborsClassifier()))

    arbol_error_estand.append(1-precisionDataset(X_estand, y, DecisionTreeClassifier()))
    knn_error_estand.append(1-precisionDataset(X_estand, y, KNeighborsClassifier()))

generarGrafico(datasets, arbol_error_estand, knn_error_estand, "ArbolDecision", "KNN", "Comparacion de errores con datos estandarizados", "Error")
generarGrafico(datasets, arbol_error_norm, knn_error_norm, "ArbolDecision", "KNN", "Comparacion de errores con datos normalizados", "Error")

# funciona correctamente