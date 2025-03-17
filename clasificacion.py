import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Crear un ejemplo de dataset
data = {
    "idProd": [1, 2, 3, 4, 5],
    "nomProd": ["Producto A", "Producto B", "Producto C", "Producto D", "Producto E"],
    "categoria": ["Electrónica", "Hogar", "Ropa", "Alimentos", "Electrónica"],
    "descripcion": ["Un dispositivo electrónico", "Decoración para el hogar", "Moda juvenil", "Alimento saludable", "Gadget moderno"],
    "precio": [150, 300, 50, 100, 200]
}

# Crear el DataFrame
df = pd.DataFrame(data)

# Vectorización de texto (descripcion)
vectorizer = TfidfVectorizer()
X_text = vectorizer.fit_transform(df["descripcion"])

# Combinar características: texto y precio
X = np.hstack([X_text.toarray(), df["precio"].values.reshape(-1, 1)])

# Etiquetas (categoría)
y = df["categoria"]

# Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de predicción (Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Hacer predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo: {accuracy:.2f}")

# Función para predecir nuevas categorías
def predecir_categoria(descripciones, precios):
    nuevos_datos_texto = vectorizer.transform(descripciones)
    nuevos_datos_features = np.hstack([nuevos_datos_texto.toarray(), np.array(precios).reshape(-1, 1)])
    predicciones = model.predict(nuevos_datos_features)
    return predicciones

# Ejemplo de predicción con múltiples nuevos datos
nuevas_descripciones = ["Un nuevo gadget electrónico", "Ropa casual de moda", "Electrodoméstico para la cocina"]
nuevos_precios = [250, 60, 150]

categorias_predichas = predecir_categoria(nuevas_descripciones, nuevos_precios)
for descripcion, precio, categoria in zip(nuevas_descripciones, nuevos_precios, categorias_predichas):
    print(f"Descripción: {descripcion} | Precio: {precio} | Categoría predicha: {categoria}")
