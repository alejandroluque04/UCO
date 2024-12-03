import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

def boxplot_por_clase(X, y, columna_interes):
    # Crear un DataFrame combinando X con las clases (y)
    df = X.copy()  # Hacemos una copia de X
    df['Clase'] = y  # Añadimos las clases al DataFrame

    # Crear el boxplot de la columna de interés agrupada por clases
    sns.boxplot(x='Clase', y=columna_interes, data=df)
    
    # Añadir título y mostrar gráfico
    plt.title(f'Box Plot de {columna_interes} por Clase')
    plt.show()



datasets = []
datasets.append(fetch_ucirepo(id=53))
datasets.append(fetch_ucirepo(id=109))
datasets.append(fetch_ucirepo(id=519))
datasets.append(fetch_ucirepo(id=42))
datasets.append(fetch_ucirepo(id=292))


for dataset in datasets:
    # Extraer las características (X) y las etiquetas (y)
    X = dataset.data.features  # DataFrame con las características
    y = dataset.data.targets.values.flatten()  # Array con las etiquetas (aplanado)

    print(f"Dataset: {dataset ['metadata']['name']}")
    # Si quieres crear un boxplot de todas las características (X)
    sns.boxplot(data=X)
    plt.title(f'Box Plot de las características del dataset {dataset["metadata"]["name"]}')
    plt.show()

# Si quieres crear un boxplot de una característica específica de X
# sns.boxplot(data=X, y='nombre_de_la_columna')
# plt.title('Box Plot de una característica específica')
# plt.show()

    # Imprimir el nombre de todas las columnas
    print("Columnas disponibles en el dataset:")
    for col in X.columns:
        print(col)

    # Pedir al usuario que introduzca el nombre de una columna
    columna_interes = input("Introduce el nombre de una columna para el boxplot: ")

    # Verificar si la columna de interés está en el DataFrame
    if columna_interes not in X.columns:
        print(f"La columna '{columna_interes}' no se encuentra en el DataFrame. Por favor, introduce un nombre de columna válido.")
    else:
        # Llamar a la función con el nombre de la columna introducida por el usuario
        boxplot_por_clase(X, y, columna_interes)

