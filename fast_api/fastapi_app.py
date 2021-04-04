# import library
import uvicorn
from fastapi import FastAPI
from accident_schema_fastapi import vehicleAccident
import numpy as np
import pandas as pd
import pickle
import xgboost  as xgb

# create the app object
app = FastAPI()

# load the model and predict
from xgboost import Booster
boost_flask = Booster({'nthread':4})
boost_flask.load_model("/Users/ocean/PycharmProjects/vehicle_accident_prediction/models/xgb_accident_flask.mod")

#Index route , open automatically on local host
@app.get('/')
def index():
    return {'message':"Hello Reddit"}
#2nd api
@app.get('/welcome')
def get_name(name:str):
    return {'message': f'Hello,{name}'}
#3 Prediction api
@app.post('/predict')
def predict_accident(data:vehicleAccident):
    data = data.dict()
    driver_age =data['driver_age']
    is_driver_alcholic=data['is_driver_alcholic']
    driver_license_age=data['driver_license_age']
    vehicle_age=data['vehicle_age']
    vehicle_mileage=data['vehicle_mileage']
    int_features = np.array([driver_age, is_driver_alcholic, driver_license_age,
                             vehicle_age, vehicle_mileage]).reshape(1,-1)

    prediction = boost_flask.predict(xgb.DMatrix(int_features))
    prediction = float(round(prediction[0][1] * 100, 2))
    prediction = 'The Likelihood of Vehicle Accident is: {} percent'.format(prediction)
    return prediction

host = '127.0.0.1'
port =8000
if __name__ == '__main__':
    uvicorn.run(app, host = host, port = port)
