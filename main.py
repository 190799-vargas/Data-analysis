from mean_var_std import calculate


def main():
    # Ejemplo de lista de entrada
    input_list = [0, 2, 2, 4, 6, 5, 6, 9, 8]

    # Llamar a la función calculate y obtener los resultados
    results = calculate(input_list)

    # Imprimir los resultados
    print("Resultados:")
    for key, value in results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
