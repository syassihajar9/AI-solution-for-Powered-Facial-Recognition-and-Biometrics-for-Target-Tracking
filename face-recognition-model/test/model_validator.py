import tensorflow as tf

def validate_model(model_path):
    try:
        # Laden des Modells
        model = tf.saved_model.load(model_path)
        print("Model loaded successfully.")

        # Überprüfen der verfügbaren Signaturen
        signatures = model.signatures
        print("Available signatures:", list(signatures.keys()))

        # Detaillierte Informationen zur Signatur 'serving_default'
        if 'serving_default' in signatures:
            signature = signatures['serving_default']
            print("Inputs:", signature.structured_input_signature)
            print("Outputs:", signature.structured_outputs)
        else:
            print("Signature 'serving_default' not found.")

        print("Model validation completed.")

    except Exception as e:
        print("An error occurred during model validation:", str(e))

if __name__ == "__main__":
    # Pfad zum Modell anpassen
    model_path = 'C:/Users/anass/RiderProjects/dronesurveillance/face-recognition-model/models/face_recognition_model/1'
    
    validate_model(model_path)
