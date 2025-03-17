import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

# Datos del dataset proporcionado
data = [
    {"NRO": 1, "PESO": 76.0, "TALLA": 175, "HORAS_DE_SUENO": 7},
    {"NRO": 2, "PESO": 56.0, "TALLA": 161, "HORAS_DE_SUENO": 7},
    {"NRO": 3, "PESO": 65.0, "TALLA": 164, "HORAS_DE_SUENO": 7},
    # Añadir más datos aquí según sea necesario...
    {"NRO": 32, "PESO": 73.0, "TALLA": 162, "HORAS_DE_SUENO": 5}
]

# Convertir a DataFrame de pandas
df = pd.DataFrame(data)

# Crear una nueva columna categórica para el peso (por simplicidad)
def categorize_peso(peso):
    if peso < 60:
        return 'bajo'
    elif 60 <= peso < 70:
        return 'medio'
    else:
        return 'alto'

df['CATEGORIA_PESO'] = df['PESO'].apply(categorize_peso)

# Separar las características y la variable objetivo
X = df[['TALLA', 'HORAS_DE_SUENO']]
y = df['CATEGORIA_PESO']

# Codificar las etiquetas de clase como enteros
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Crear el modelo Naive Bayes Gaussiano
model = GaussianNB()

# Entrenar el modelo con los datos de entrenamiento
model.fit(X_train, y_train)

# Realizar predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)

# Generar el reporte de clasificación (especificar explícitamente las clases con labels y zero_division=0)
report = classification_report(y_test, y_pred, labels=[0, 1, 2], target_names=le.classes_, zero_division=0)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
