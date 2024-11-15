from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(df, target_column, test_size=0.2, random_state=42):
    """
    Divide los datos en conjuntos de entrenamiento y prueba, y los escala.
    
    Parámetros:
        df (DataFrame): Conjunto de datos.
        target_column (str): Nombre de la columna objetivo.
        test_size (float): Tamaño del conjunto de prueba.
        random_state (int): Semilla para reproducibilidad.
        
    Retorna:
        tuple: Conjuntos X_train, X_test, y_train, y_test escalados.
    """
    print("Iniciando preprocesamiento...")
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"Datos divididos en entrenamiento ({len(X_train)}) y prueba ({len(X_test)}).")
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
