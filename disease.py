import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

model = tf.keras.models.load_model("models/disease_model.h5")
labels = ["Healthy","Leaf Blight","Bacterial Spot","Leaf Mold"]

def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(224,224))
    img = image.img_to_array(img)/255
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return labels[np.argmax(pred)]
