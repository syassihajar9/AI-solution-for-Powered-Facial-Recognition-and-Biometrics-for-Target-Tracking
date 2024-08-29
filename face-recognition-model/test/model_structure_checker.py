import tensorflow as tf

# Pfad zur HDF5-Datei
h5_model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model_re_saved/1.h5'

# Modell laden
try:
    model = tf.keras.models.load_model(h5_model_path)
    print("HDF5 model loaded successfully.")
except Exception as e:
    print(f"Failed to load the HDF5 model: {e}")
    raise

# Modellarchitektur anzeigen
print("Model architecture:")
model.summary()
