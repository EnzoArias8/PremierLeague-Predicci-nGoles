
# Predicción del Número de Goles de Jugadores

Este proyecto utiliza diferentes modelos de aprendizaje automático para predecir el número de goles que un jugador podría marcar en función de sus estadísticas de rendimiento, como minutos jugados, asistencias y goles esperados por 90 minutos (`xG_90`).

## Enfoques Utilizados

1. **Regresión Lineal**: Modelo de regresión simple utilizando todos los datos disponibles.
2. **Regresión Polinómica**: Expande las características para capturar relaciones no lineales.
3. **Bosque Aleatorio**: Modelo basado en árboles de decisión para manejar relaciones más complejas.
4. **Análisis PCA**: Reducción de dimensionalidad para visualizar los datos y entender su estructura.

## Requisitos

Para ejecutar este notebook, se requiere:
- Python 3.8 o superior.
- Bibliotecas necesarias:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Estructura del Notebook

1. **Carga de Datos**: Se cargan las estadísticas de jugadores desde un archivo CSV.
2. **Exploración de Datos**: Análisis descriptivo y visualización de las principales características.
3. **Entrenamiento de Modelos**:
   - Regresión Lineal
   - Regresión Polinómica
   - Bosque Aleatorio
4. **Evaluación de Modelos**: Métricas como R² y error cuadrático medio.
5. **Análisis PCA**: Visualización de los datos en componentes principales.

## Cómo Usar Este Notebook

1. Asegúrate de tener las dependencias instaladas.
2. Descarga el archivo `Predicción.ipynb` y el dataset correspondiente.
3. Abre el notebook en Jupyter Notebook o JupyterLab.
4. Ejecuta las celdas en orden para replicar los resultados.

## Contribución

Si deseas contribuir al proyecto, puedes abrir un issue o enviar un pull request con mejoras.

## Licencia

Este proyecto se encuentra bajo la Licencia MIT.
