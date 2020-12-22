from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    segiempat = []
    segitiga = []
    lingkaran = []

    for file in os.listdir("segiempat"):
        img = Image.open("segiempat/" + file)
        img = np.array(img)
        img = img.flatten()
        segiempat.append(img)

    for file in os.listdir("segitiga"):
        img = Image.open("segitiga/" + file)
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)

    for file in os.listdir("lingkaran"):
        img = Image.open("lingkaran/" + file)
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    return segiempat, segitiga, lingkaran

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO] Loading Dataset")
    segiempat, segitiga, lingkaran = load_dataset()
    print("[INFO] Loading Model")
    y_segiempat = np.zeros(len(segiempat))
    y_segitiga = np.ones(len(segitiga))
    y_lingkaran = np.ones(len(lingkaran)) * 2

    x = segiempat + segitiga + lingkaran
    y = np.concatenate([y_segiempat, y_segitiga, y_lingkaran])

    model.fit(x, y)
    return model
