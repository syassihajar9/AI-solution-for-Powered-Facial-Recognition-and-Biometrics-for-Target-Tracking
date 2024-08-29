import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Pfade definieren
train_dir = '/app/data/train'
validation_dir = '/app/data/validation'
model_save_path = '/app/model/model.keras'

# ImageDataGenerator für Trainings- und Validierungsdaten
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(128, 128),
    batch_size=16,  # Reduce this number
    class_mode='binary'
)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(128, 128),
    batch_size=16,  # Reduce this number
    class_mode='binary'
)

# Modell erstellen
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modell trainieren
model.fit(
    train_generator,
    epochs=10,
    validation_data=validation_generator
)

# Modell speichern
model.save(model_save_path)
print(f"Model saved to: {model_save_path}")
