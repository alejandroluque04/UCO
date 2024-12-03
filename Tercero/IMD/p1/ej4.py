from ucimlrepo import fetch_ucirepo
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from generar_graficos import generarGrafico


def precisionDatasetEstandarizado(dataset,features,label,modelo,n):
     precision =0
     X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.2, random_state=1)
     # Standardize the data
     scaler = StandardScaler()
     scaler.fit(X_train)
     X_train = scaler.transform(X_train)
     X_test = scaler.transform(X_test)
     # Aplicamos PCA de n dimensiones
     pca=PCA(n_components=n)
     pca.fit(X_train)
     # Fit and transform data 2D
     X_train = pca.fit_transform(X_train)
     X_test = pca.transform(X_test)
     # Entrenamos el modelo
     modelo.fit(X_train,y_train)
     # Predicciones del modelo
     y_pred = modelo.predict(X_test)
     # Calculamos la precision del modelo
     precision = metrics.accuracy_score(y_test,y_pred)
     return precision





datasets = []

datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))

arboles_precision = []
knn_precision = []
arboles_precision_3 = []
knn_precision_3 = []
arboles_precision_4 = []
knn_precision_4 = []



for elemento in datasets:
    # data (as pandas dataframes) 
    X = elemento.data.features  # Características
    y = elemento.data.targets.values.flatten()  # Etiquetas como un array

    print(f"Dataset: {elemento ['metadata']['name']}")
    arboles_precision.append(precisionDatasetEstandarizado(elemento,X,y,DecisionTreeClassifier(), 2))
    knn_precision.append(precisionDatasetEstandarizado(elemento,X,y,KNeighborsClassifier(), 2))
    arboles_precision_3.append(precisionDatasetEstandarizado(elemento,X,y,DecisionTreeClassifier(), 3))
    knn_precision_3.append(precisionDatasetEstandarizado(elemento,X,y,KNeighborsClassifier(), 3))
    arboles_precision_4.append(precisionDatasetEstandarizado(elemento,X,y,DecisionTreeClassifier(), 4))
    knn_precision_4.append(precisionDatasetEstandarizado(elemento,X,y,KNeighborsClassifier(), 4))



generarGrafico(datasets, arboles_precision, knn_precision, "Arbol Decision", "KNN", 'Comparación de Precisión entre Métodos con 2 componentes', 'Precisión')
generarGrafico(datasets, arboles_precision_3, knn_precision_3, "Arbol Decision", "KNN", 'Comparación de Precisión entre Métodos con 3 componentes', 'Precisión')
generarGrafico(datasets, arboles_precision_4, knn_precision_4, "Arbol Decision", "KNN", 'Comparación de Precisión entre Métodos con 4 componentes', 'Precisión')
