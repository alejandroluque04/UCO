from ucimlrepo import fetch_ucirepo
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np
from generar_graficos import generarGrafico





def generarMatrizConfusion(dataset, modelo, features, label):
     X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=1)
     modelo.fit(X_train,y_train)
     y_pred = modelo.predict(X_test)
     print(confusion_matrix(y_test,y_pred))



def crear_arbol_y_knn_simple(X, y, n_neighbors=3, normalizar=False, estandarizar=False):
    # Dividir el dataset en conjuntos de entrenamiento y prueba (70% entrenamiento, 30% prueba)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Normalizar a [0, 1] si se indica
    if normalizar:
        escala = MinMaxScaler()
        X_train = escala.fit_transform(X_train)
        X_test = escala.transform(X_test)

    # Estandarizar si se indica
    if estandarizar:
        escala = StandardScaler()
        X_train = escala.fit_transform(X_train)
        X_test = escala.transform(X_test)

        # Comprobación de media y desviación estándar después de la estandarización
        print("Media de cada característica después de la estandarización:")
        print(np.mean(X_train, axis=0))  # Debería estar cerca de 0

        print("\nDesviación estándar de cada característica después de la estandarización:")
        print(np.std(X_train, axis=0))  # Debería estar cerca de 1

    # 1. Árbol de Decisión
    clf_tree = DecisionTreeClassifier(random_state=42)
    clf_tree.fit(X_train, y_train)
    y_pred_tree = clf_tree.predict(X_test)
    accuracy_tree = accuracy_score(y_test, y_pred_tree)
    
    # 2. k-Vecinos Más Cercanos
    clf_knn = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf_knn.fit(X_train, y_train)
    y_pred_knn = clf_knn.predict(X_test)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    
    # Retornar las precisiones de ambos métodos
    return accuracy_tree, accuracy_knn




datasets = []
arboles_precision = []
knn_precision = []
arboles_error_norm = []
knn_error_norm = []
arboles_precision_estand = []
knn_precision_estand = []

datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))

for elemento in datasets:
    # data (as pandas dataframes) 
    X = elemento.data.features  # Características
    y = elemento.data.targets.values.flatten()  # Etiquetas como un array

    print(f"Dataset: {elemento ['metadata']['name']}")
    print("Matriz de Confusión para Arbol de Decisión")
    generarMatrizConfusion(elemento, DecisionTreeClassifier(), X, y)
    print("\nMatriz de Confusión para KNN")
    generarMatrizConfusion(elemento, KNeighborsClassifier(), X, y)

    arbol, knn = crear_arbol_y_knn_simple(X, y)      
    arboles_precision.append(arbol)
    knn_precision.append(knn)

generarGrafico(datasets, arboles_precision, knn_precision, "Arbol Decision", "KNN", 'Comparación de Precisión entre Métodos', 'Precisión')
