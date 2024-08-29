import tensorflow as tf
import numpy as np

# Pfad zum Modell anpassen
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'
model = tf.saved_model.load(model_path)

# Modell-Signatur abrufen
signature = model.signatures['serving_default']

# Korrekte Beispiel-Daten vorbereiten (160x160 Pixel, 3 Farbkanäle)
example_input = np.random.random((1, 160, 160, 3)).astype(np.float32)

# Vorhersage durchführen
output = signature(inputs=tf.convert_to_tensor(example_input))
print("Predictions:", output)
