import tensorflow as tf

# Pfad zu Ihrem Keras-Modell
model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'

# Laden des Keras-Modells
model = tf.keras.models.load_model(model_path)

# Anzeigen der Modellvariablen
print("Model Variables:")
for var in model.trainable_variables:
    print(var.name, var.shape)
