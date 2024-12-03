import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import KBinsDiscretizer
from ucimlrepo import fetch_ucirepo
from generar_graficos import generarGrafico

def evaluate_discretization(metodo1, metodo2, X, y, n_bins=5, encode='ordinal'):
    """
    Función que evalúa la discretización de un dataset y calcula la precisión de dos modelos.
    
    :param metodo1: Primer modelo a evaluar
    :param metodo2: Segundo modelo a evaluar
    :param X: Datos de entrada (features)
    :param y: Etiquetas (target)
    :param n_bins: Número de bins para la discretización
    :param encode: Tipo de codificación ('ordinal', 'onehot', 'onehot-dense')
    
    :return: Precisión de los dos modelos
    """
    # Aplicar discretización
    discretizer = KBinsDiscretizer(n_bins=n_bins, encode=encode, strategy='uniform')
    X_discretized = discretizer.fit_transform(X)
    
    # Convertir a matriz densa si es necesario
    if encode == 'onehot':
        X_discretized = X_discretized.toarray()
    
    # Crear DataFrame con los datos discretizados
    X_discretized_df = pd.DataFrame(X_discretized, columns=[f'bin_{i}' for i in range(X_discretized.shape[1])])
    
    # Dividir los datos en conjunto de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X_discretized_df, y, test_size=0.3, random_state=42)
    
    # Entrenar y evaluar el primer modelo
    metodo1.fit(X_train, y_train)
    y_pred_m1 = metodo1.predict(X_test)
    metodo1_precision = metrics.accuracy_score(y_test, y_pred_m1)
    
    # Entrenar y evaluar el segundo modelo
    metodo2.fit(X_train, y_train)
    y_pred_m2 = metodo2.predict(X_test)
    metodo2_precision = metrics.accuracy_score(y_test, y_pred_m2)
    
    return metodo1_precision, metodo2_precision



datasets = []
arboles_precision_ord = []
knn_precision_ord = []
arboles_precision_one = []
knn_precision_one = []


datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))

for dataset in datasets:
    # Data (as pandas dataframes) 
    X = dataset.data.features  # Asegúrate de que esto sea correcto
    y = dataset.data.targets.values.flatten()  # Asegúrate de que esto sea correcto


    # Llamada a la función para evaluar el efecto de la discretización
    arboles_ord, knn_ord = evaluate_discretization(DecisionTreeClassifier(), KNeighborsClassifier(), X, y, n_bins=5, encode='ordinal')
    arboles_one, knn_one = evaluate_discretization(DecisionTreeClassifier(), KNeighborsClassifier(), X, y, n_bins=5, encode='onehot')

    arboles_precision_ord.append(arboles_ord)
    knn_precision_ord.append(knn_ord)
    arboles_precision_one.append(arboles_one)
    knn_precision_one.append(knn_one)


generarGrafico(datasets, arboles_precision_ord, knn_precision_ord, 'Árbol de Decisión', 'KNN', 'Precisión de Modelos con Discretización Ordinal', 'Precisión')
generarGrafico(datasets, arboles_precision_one, knn_precision_one, 'Árbol de Decisión', 'KNN', 'Precisión de Modelos con Discretización One-Hot', 'Precisión')