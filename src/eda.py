import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    """
    Realiza visualizaciones básicas del conjunto de datos.
    
    Parámetros:
        df (DataFrame): Conjunto de datos.
    """
    print("Generando visualización de datos...")
    sns.pairplot(df, diag_kind='kde')
    plt.show()

def plot_correlation_matrix(df):
    """
    Genera un heatmap de la matriz de correlación.
    
    Parámetros:
        df (DataFrame): Conjunto de datos.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matriz de Correlación")
    plt.show()
