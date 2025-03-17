import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Datos de entrenamiento (puedes cambiarlo por tu dataset)
data = "La inteligencia artificial está transformando la forma en que interactuamos con la tecnología. " \
       "Los modelos de lenguaje pueden generar texto coherente y útil en muchas aplicaciones."

# Tokenización del texto
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
word_index = tokenizer.word_index

# Convertir texto en secuencias
sequences = []
words = data.split()
for i in range(1, len(words)):
    seq = words[:i+1]
    sequences.append(tokenizer.texts_to_sequences([" ".join(seq)])[0])

# Padding de secuencias
max_seq_length = max(len(seq) for seq in sequences)
sequences = pad_sequences(sequences, maxlen=max_seq_length, padding='pre')

# Datos de entrada y salida
X, y = sequences[:, :-1], sequences[:, -1]
y = keras.utils.to_categorical(y, num_classes=len(word_index) + 1)

# Construcción del modelo LSTM
model = keras.Sequential([
    keras.layers.Embedding(input_dim=len(word_index) + 1, output_dim=50, input_length=max_seq_length - 1),
    keras.layers.LSTM(100, return_sequences=True),
    keras.layers.LSTM(100),
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(len(word_index) + 1, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X, y, epochs=100, verbose=1)

# Función para generar texto
def generar_texto(seed_text, num_words):
    for _ in range(num_words):
        sequence = tokenizer.texts_to_sequences([seed_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_seq_length - 1, padding='pre')
        predicted = np.argmax(model.predict(sequence, verbose=0))
        for word, index in word_index.items():
            if index == predicted:
                seed_text += " " + word
                break
    return seed_text

# Prueba de generación de texto
print(generar_texto("Los modelos", 10))
