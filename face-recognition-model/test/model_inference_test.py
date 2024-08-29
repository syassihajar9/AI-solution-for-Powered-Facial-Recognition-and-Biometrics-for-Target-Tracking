import tensorflow as tf
import numpy as np

# Pfad zum Modell anpassen
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'

# Modell laden
loaded_model = tf.saved_model.load(model_path)

# Zugriff auf die 'serving_default'-Signatur
serving_default = loaded_model.signatures['serving_default']

# Beispiel-Eingabedaten (passen Sie die Formate an Ihre Anforderungen an)
input_data = np.random.random([1, 160, 160, 3]).astype(np.float32)

# Modellvorhersage
input_tensor = tf.convert_to_tensor(input_data)
predictions = serving_default(input_tensor)
print("Predictions:", predictions)
