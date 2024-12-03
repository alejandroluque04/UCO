from sklearn.impute import SimpleImputer, IterativeImputer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from ucimlrepo import fetch_ucirepo
from generar_graficos import generarGrafico

def PrecisionImputer(metodo1, metodo2, X, y, imputador='simple'):
    """
    Función que calcula la precisión de dos modelos después de imputar valores perdidos en el dataset.
    
    :param metodo1: Primer modelo a evaluar
    :param metodo2: Segundo modelo a evaluar
    :param X: Datos de entrada (features) con posibles valores perdidos
    :param y: Etiquetas (target)
    :param imputador: Tipo de imputador a usar ('simple' o 'iterative')
    
    :return: Precisión de los dos modelos
    """

    # Identificar columnas numéricas y categóricas
    numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Crear transformadores para columnas numéricas y categóricas
    if imputador == 'simple':
        numeric_transformer = SimpleImputer(strategy='mean')
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])
    elif imputador == 'iterative':
        numeric_transformer = IterativeImputer(max_iter=10, random_state=0)
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),  # Usar SimpleImputer para categóricas
            ('encoder', OneHotEncoder(handle_unknown='ignore'))
        ])
    else:
        raise ValueError("El parámetro 'imputador' debe ser 'simple' o 'iterative'")

    # Crear un preprocesador para aplicar imputación
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ]
    )

    # Crear un pipeline que primero impute y luego ajuste el modelo
    pipeline1 = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', metodo1)])
    pipeline2 = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', metodo2)])

    # Split data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

    # Entrenamos el modelo 1
    pipeline1.fit(X_train, y_train)
    y_pred_m1 = pipeline1.predict(X_test)
    metodo1_precision = metrics.accuracy_score(y_test, y_pred_m1)

    # Entrenamos el modelo 2
    pipeline2.fit(X_train, y_train)
    y_pred_m2 = pipeline2.predict(X_test)
    metodo2_precision = metrics.accuracy_score(y_test, y_pred_m2)

    return metodo1_precision, metodo2_precision



datasets = []
arbol_precision_simple, knn_precision_simple = [], []
arbol_precision_iterative, knn_precision_iterative = [], []

# Fetch datasets
datasets.append(fetch_ucirepo(id=14))
datasets.append(fetch_ucirepo(id=336))
datasets.append(fetch_ucirepo(id=46))

for elemento in datasets:
    # Data (as pandas dataframes) 
    X = elemento.data.features  # Asegúrate de que esto sea correcto
    y = elemento.data.targets.values.flatten()  # Asegúrate de que esto sea correcto

    # Llamada a la función (puedes especificar el imputador si lo deseas)
    arbol_simple, knn_simple = PrecisionImputer(DecisionTreeClassifier(), KNeighborsClassifier(), X, y, imputador='simple')  # o 'iterative'
    arbol_iterative, knn_iterative = PrecisionImputer(DecisionTreeClassifier(), KNeighborsClassifier(), X, y, imputador='iterative')  # o 'iterative'
    arbol_precision_simple.append(arbol_simple)
    knn_precision_simple.append(knn_simple)
    arbol_precision_iterative.append(arbol_iterative)
    knn_precision_iterative.append(knn_iterative)


generarGrafico(datasets, arbol_precision_simple, knn_precision_simple, 'Árbol de Decisión', 'KNN', 'Precisión de modelos con imputación simple', 'Precisión')
generarGrafico(datasets, arbol_precision_iterative, knn_precision_iterative, 'Árbol de Decisión', 'KNN', 'Precisión de modelos con imputación iterativa', 'Precisión')