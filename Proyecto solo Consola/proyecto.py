
import pandas as pd
import matplotlib.pyplot as plt
import os

# Variable global para almacenar el DataFrame
df = None

# Menu de opciones
def menu():
    print("\n--- Explorador de Datos Climáticos ---")
    print("1. Leer Datos Climáticos desde CSV")
    print("2. Calcular Promedio de Temperatura Promedio")
    print("3. Encontrar Temperatura Promedio Máxima")
    print("4. Encontrar Temperatura Promedio Mínima")
    print("5. Filtrar registros con Temperatura Promedio mayor a un valor")
    print("6. Filtrar registros con Temperatura Promedio menor a un valor")
    print("7. Generar Histograma de Temperaturas Promedio")
    print("8. Generar un gráfico de dispersión del Día vs. Temperatura Promedio.")
    print("9. Mostrar Datos Ingresados")
    print("0. Salir")
    print("------------------------------------")

# Función Para leer el archivo csv (1)
def cargar_csv():

    global df
    while True:
        ruta_archivo = input("Ingrese la ruta del archivo .csv con los datos climáticos: ")
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe. Por favor, ingrese una ruta válida.")
            continue
        try:
            df = pd.read_csv(ruta_archivo)
            print("Datos cargados exitosamente.")
            break
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            print("Asegúrese de que la ruta es correcta y el archivo es un CSV válido.")

# Función para calcular promedio de temperaturas (2)
def promedio():

    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    promedio = df['AvgTemperature'].mean()
    print(f"Promedio de Temperatura Promedio: {promedio:.2f} °F")

# Función para encontrar la temperatura máxima (3)
def temperatura_max():
    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    maxima = df['AvgTemperature'].max()
    print(f"Temperatura Promedio Máxima registrada: {maxima:.2f} °F")


# Función para encontrar temperatura minima (4)
def temperatura_min():
    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    minima = df['AvgTemperature'].min()
    print(f"Temperatura Promedio Mínima registrada: {minima:.2f} °F")

# Filtrar temperaturas por encima de un valor (5)
def filtrar_u():
    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    try:
        num = float(input("Ingrese el límite de temperatura promedio: "))
        res = df[df['AvgTemperature'] >= num]
        print(f"Registros con Temperatura Promedio mayor a {num:.2f} °F:")
        if not res.empty:
            print(res)
        else:
            print("No se encontraron registros que cumplan el criterio.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Filtrar temperaturas por debajo de un valor (6)
def filtrar_d():
    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    try:
        num = float(input("Ingrese el límite de temperatura promedio: "))
        res = df[df['AvgTemperature'] <= num]
        print(f"Registros con Temperatura Promedio menor a {num:.2f} °F:")
        if not res.empty:
            print(res)
        else:
            print("No se encontraron registros que cumplan el criterio.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")


# Generar historigrama (7)
def plot_h():
    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    plt.hist(df['AvgTemperature'], edgecolor='black')
    plt.title('Historigrama')
    plt.xlabel('Temperatura (°F)')
    plt.ylabel('Frecuencia')
    plt.grid(axis="y", alpha=0.75)
    plt.show()

# Generar gráfico de dispersión (8)
def plot_d():

    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return

    plt.scatter(df['Day'], df['AvgTemperature'])
    plt.title("Gráfico de dispersión")
    plt.xlabel("Dias de Enero")
    plt.ylabel("Temperatura (°F)")
    plt.grid(axis="y", alpha=0.75)
    plt.show()

# Mostrar datos (9)
def ver_csv():

    if df is None:
        print("Primero debe cargar los datos (Opción 1).")
        return
    print("Datos Ingresados: \n")

    print(df)

# Funcion principal del programa 
def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cargar_csv()
        elif opcion == '2':
            promedio()
        elif opcion == '3':
            temperatura_max()
        elif opcion == '4':
            temperatura_min()
        elif opcion == '5':
            filtrar_u()
        elif opcion == '6':
            filtrar_d()
        elif opcion == '7':
            plot_h()
        elif opcion == '8':
            plot_d()
        elif opcion == '9':
            ver_csv()
        # Salir (0)
        elif opcion == '0':
            print("Saliendo del Explorador de Datos Climáticos. ¡Hasta Luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()