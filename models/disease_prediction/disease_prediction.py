import numpy as np
import pickle

model = pickle.load(open("C://Users//Nastalique//Desktop//docto//models//disease_prediction//prediction_model.pkl", "rb"))


def predict(id):
    return model.predict(np.array([id], dtype='object'))

