#Kütüphaneler
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np


np.set_printoptions(suppress=True)
def get_class(image_path,model_path="keras_model.h5",label_path="labels.txt"):
    #Model Belirleniyor
    model = load_model(model_path, compile=False)

    #Sınıf İsimleri Alınıyor
    class_names = open(label_path, "r").readlines()

    #Görsel Analiz edilip tahminleri değişkenlere yazılıyor
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    #Yapay zekanın tahmin ettiği sınıfı ve değeri yazdırıyoruz
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)
    return class_name[2:].strip() , confidence_score