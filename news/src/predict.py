from .transform import encode
from tensorflow.keras.models import load_model
import numpy as np

def predict_class(str):
    encoded = encode(str)
    model = load_model('./model/LTSM/model')
    encoded_arr = np.array(encoded)
    label = int(model.predict_classes(encoded_arr))
    return label
