import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def diab_prediction(list):
    model = pickle.load(open("models/diabetes_model.sav" ,'rb'))
    inputdata_numpy_array = np.asarray(list)
    final_value = inputdata_numpy_array.reshape(1,-1)
    prediction = model.predict(final_value)
    return prediction
def heart_prediction(list):
    print(list)
    model = pickle.load(open("models/heart_disease_model.sav", 'rb'))
    inputdata_numpy_array = np.asarray(list)
    final_value = inputdata_numpy_array.reshape(1, -1)
    prediction = model.predict(final_value)
    return prediction

# list =[(63,1,3,145,233,1,0,150,0,2.3,0,0,1),(62,0,0,140,268,0,0,160,0,3.6,0,2,2)]
# for i in list:
#    model = heart_prediction(i)[0]
#     print(model)