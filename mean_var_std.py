import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("La lista debe contener nueve números")

    # Convertir la lista en una matriz 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calcular las estadísticas
    mean_axis1 = np.mean(matrix, axis=0).tolist()
    mean_axis2 = np.mean(matrix, axis=1).tolist()
    mean_flattened = np.mean(matrix).tolist()

    variance_axis1 = np.var(matrix, axis=0).tolist()
    variance_axis2 = np.var(matrix, axis=1).tolist()
    variance_flattened = np.var(matrix).tolist()

    std_dev_axis1 = np.std(matrix, axis=0).tolist()
    std_dev_axis2 = np.std(matrix, axis=1).tolist()
    std_dev_flattened = np.std(matrix).tolist()

    max_axis1 = np.max(matrix, axis=0).tolist()
    max_axis2 = np.max(matrix, axis=1).tolist()
    max_flattened = np.max(matrix).tolist()

    min_axis1 = np.min(matrix, axis=0).tolist()
    min_axis2 = np.min(matrix, axis=1).tolist()
    min_flattened = np.min(matrix).tolist()

    sum_axis1 = np.sum(matrix, axis=0).tolist()
    sum_axis2 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix).tolist()

    # Crear el diccionario con los resultados
    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_dev_axis1, std_dev_axis2, std_dev_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations


# Ejemplo de uso
print(calculate([0, 2, 2, 4, 6, 5, 6, 9, 8]))
