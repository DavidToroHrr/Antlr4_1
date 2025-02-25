import pandas as pd

def load_csv(file_path):
    """
    Carga un archivo CSV y devuelve un DataFrame de pandas.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error al cargar el archivo CSV: {e}")
        return None

def load_excel(file_path, sheet_name=0):
    """
    Carga un archivo Excel y devuelve un DataFrame de pandas.
    """
    try:
        return pd.read_excel(file_path, sheet_name=sheet_name)
    except Exception as e:
        print(f"Error al cargar el archivo Excel: {e}")
        return None

def preview_data(df, num_rows=5):
    """
    Muestra una vista previa de los datos (primeras filas).
    """
    if df is not None:
        print(df.head(num_rows))
    else:
        print("No hay datos para mostrar.")