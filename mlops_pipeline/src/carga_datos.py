import pandas as pd
import os

def cargarDatos():

    # 1. Ruta absoluta del directorio donde está este script (src)
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    print(ruta_actual)

    # 2. Subir un nivel para llegar a la carpeta donde está la base de datos
    ruta_proyecto = os.path.dirname(ruta_actual)
    print(ruta_proyecto)




    # 3. Contruir la ruta completa al archivo Excel
    ruta_excel = os.path.join(ruta_proyecto, "Base_de_datos.xlsx")
    print(ruta_excel)
    
cargarDatos()
    # 4. Leemos los datos y los imprimimos
#    df = pd.read_excel(ruta_excel)
#    print(df.head())
#    return df

#if __name__ == "__main__":
#    datos = cargarDatos()
#    print(datos.head())
#    print(datos.columns)