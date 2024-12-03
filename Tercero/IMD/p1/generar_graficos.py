import matplotlib.pyplot as plt



def generarGrafico(datasets, precision1, precision2, cadena1, cadena2, titulo, etiqueta):
    # Usar índices en el eje X para representar cada dataset
    x_labels = [i['metadata']['name'] for i in datasets]
    
    # Graficar las precisiones para ambos métodos
    plt.plot(x_labels, precision1, label=cadena1, marker='o')
    plt.plot(x_labels, precision2, label=cadena2, marker='o')
    
    # Etiquetas y título
    plt.xlabel('Datasets')
    plt.ylabel(etiqueta)
    plt.title(titulo)
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()




