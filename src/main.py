from data_loading import load_data
from eda import visualize_data, plot_correlation_matrix
from preprocessing import preprocess_data
from models import train_models, evaluate_models

def main():
    # Ruta al archivo de datos
    file_path = 'C:/Users/Usuario/Documents/PremierLeague-PrediccónGoles/data/premier-player-23-24.csv'  
    
    # Cargar los datos
    df = load_data(file_path)
    if df is None:
        return
    
    # Análisis exploratorio de datos
    visualize_data(df)
    plot_correlation_matrix(df)
    
    # Preprocesamiento
    target_column = 'Pos_'  # Cambiar según la columna objetivo real
    X_train, X_test, y_train, y_test = preprocess_data(df, target_column)
    
    # Entrenamiento de modelos
    models = train_models(X_train, y_train)
    
    # Evaluación de modelos
    results = evaluate_models(models, X_test, y_test)
    print("Resultados de la evaluación:", results)

if __name__ == '__main__':
    main()
