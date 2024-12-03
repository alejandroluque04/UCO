import seaborn as sns
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo


# Función para representar la matriz de correlación
def matriz_correlacion(X):
    # Calcular la matriz de correlación
    correlacion = X.corr()

    # Crear el mapa de calor
    plt.figure(figsize=(10, 8))  # Ajustar el tamaño del gráfico
    sns.heatmap(correlacion, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    
    # Añadir título
    plt.title('Matriz de Correlación')
    
    # Mostrar el gráfico
    plt.show()


# Función para representar la matriz de correlación entre instancias
def matriz_correlacion_instancias(X):
    # Calcular la matriz de correlación sobre la matriz transpuesta
    correlacion = X.T.corr()

    # Crear el mapa de calor
    plt.figure(figsize=(10, 8))  # Ajustar el tamaño del gráfico
    sns.heatmap(correlacion, annot=True, fmt='.2f', cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    
    # Añadir título
    plt.title('Matriz de Correlación entre Instancias')
    
    # Mostrar el gráfico
    plt.show()



datasets = []
datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))

for dataset in datasets:
    print(f"Dataset: {dataset['metadata']['name']}")
    # Extraer las características (X) y las etiquetas (y)
    X = dataset.data.features  # DataFrame con las características
    y = dataset.data.targets.values.flatten()  # Array con las etiquetas (aplanado)

    # Llamada de ejemplo a la función
    matriz_correlacion(X)           # ejercicio 4
    matriz_correlacion_instancias(X)    # ejercicio 5