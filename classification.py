import cv2
import numpy as np
import requests
import datetime
from io import BytesIO
import tensorflow as tf

class WasteClassifier:
    def __init__(self, model_path="model.h5"):
        self.model = tf.keras.models.load_model(model_path, custom_objects={"SparseCategoricalCrossentropy": tf.keras.losses.SparseCategoricalCrossentropy()})
        self.classes = ["Aluminium", "Carton", "Glass", "Organic Waste", "Other Plastics", "Paper and Cardboard", "Plastic", "Textiles", "Wood"]
        self.nonbio = ["Aluminium", "Carton", "Glass", "Other Plastics", "Plastic"]

    def classify_frame(self, camera_url):
        response = requests.get(camera_url)
        image_data = response.content
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"image_{timestamp}.jpg"
        with open(filename, "wb") as f:
            f.write(image_data)
        
        frame = cv2.imdecode(np.frombuffer(response.content, dtype=np.uint8), -1)
        img = cv2.resize(frame, (256, 256))
        img_array = np.expand_dims(img, axis=0)
        predictions = self.model.predict(img_array)
        predicted_class = self.classes[np.argmax(predictions)]
        category = "Non-Biodegradable" if predicted_class in self.nonbio else "Biodegradable"
        print(category)
        return category

    def dump_biodegradable_waste(self):
        requests.get("http://192.168.25.147/rotate?direction=left")
        print("Dumping Biodegradable Waste")

    def dump_non_biodegradable_waste(self):
        requests.get("http://192.168.25.147/rotate?direction=right")
        print("Dumping Non-Biodegradable Waste")
