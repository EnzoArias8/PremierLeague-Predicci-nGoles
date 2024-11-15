from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

def train_models(X_train, y_train):
    """
    Entrena múltiples modelos de clasificación.
    
    Parámetros:
        X_train (array): Características de entrenamiento.
        y_train (array): Etiquetas de entrenamiento.
        
    Retorna:
        dict: Modelos entrenados.
    """
    print("Entrenando modelos...")
    models = {
        'DecisionTree': DecisionTreeClassifier(),
        'KNN': KNeighborsClassifier(),
        'SVM': SVC(),
        'RandomForest': RandomForestClassifier()
    }
    
    trained_models = {name: model.fit(X_train, y_train) for name, model in models.items()}
    print("Modelos entrenados exitosamente.")
    return trained_models

def evaluate_models(models, X_test, y_test):
    """
    Evalúa los modelos entrenados.
    
    Parámetros:
        models (dict): Modelos entrenados.
        X_test (array): Características de prueba.
        y_test (array): Etiquetas de prueba.
        
    Retorna:
        dict: Puntuaciones de cada modelo.
    """
    print("Evaluando modelos...")
    results = {name: model.score(X_test, y_test) for name, model in models.items()}
    for model, score in results.items():
        print(f"{model}: {score:.4f}")
    return results
