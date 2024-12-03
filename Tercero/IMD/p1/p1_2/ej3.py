import seaborn as sns
import matplotlib.pyplot as plt
from ucimlrepo import fetch_ucirepo


# Función para crear un scatter plot matricial
def scatter_plot_matricial(X, y=None):
    # Crear un DataFrame que contenga las características y las clases, si se proporcionan
    if y is not None:
        df = X.copy()  # Copiar las características
        df['Clase'] = y  # Añadir las clases al DataFrame
    else:
        df = X  # Solo usar X si no se proporcionan clases

    # Crear el scatter plot matricial
    sns.pairplot(df, hue='Clase' if y is not None else None)
    
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
    scatter_plot_matricial(X, y)
