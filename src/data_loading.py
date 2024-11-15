import pandas as pd

def load_data(file_path: str):
    """
    Carga el dataset desde un archivo CSV.
    
    Parámetros:
        file_path (str): Ruta al archivo CSV.
        
    Retorna:
        DataFrame: Datos cargados en un DataFrame de Pandas.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Datos cargados exitosamente desde {file_path}.")
        return df
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None
