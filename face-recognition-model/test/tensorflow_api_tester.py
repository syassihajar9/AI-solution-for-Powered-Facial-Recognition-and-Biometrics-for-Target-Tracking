import tensorflow as tf
import numpy as np

# Pfad zum Modell anpassen
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'
model = tf.saved_model.load(model_path)

# Modell-Signatur abrufen
signature = model.signatures['serving_default']

# Beispiel-Daten vorbereiten
example_input = np.array([[[[0.1, 0.2, 0.3],
                            [0.4, 0.5, 0.6]],
                           [[0.7, 0.8, 0.9],
                            [0.1, 0.2, 0.3]]]], dtype=np.float32)

# Vorhersage durchführen
output = signature(inputs=tf.convert_to_tensor(example_input))
print("Predictions:", output)
