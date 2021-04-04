# import numpy as np
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd

# import pickle

app = Flask(__name__)

import xgboost  as xgb
# load the model and predict
from xgboost import Booster
boost_flask = Booster({'nthread':4})
boost_flask.load_model("/Users/ocean/PycharmProjects/vehicle_accident_prediction/models/xgb_accident_flask.mod")
#model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1,-1)
    prediction = boost_flask.predict(xgb.DMatrix(final_features))

    #output = round(prediction[0][0])
    output = round(float(prediction[0][1]*100),2)

    return render_template('index.html', prediction_text='The Likelihood of Vehicle Accident is: {}%'.format(output))

@app.route('/predict_file',methods=['POST'])
def predict_file_accident():
    accident_df = pd.read_csv(request.files.get("file"))
    prediction = boost_flask.predict(xgb.DMatrix(accident_df.values))
    output = list(prediction[:,1])
    return 'The Likelihood of Vehicle Accident is: {}%'.format(output)


@app.route('/predict_api',methods=['GET'])
def predict_api():
    driver_age=  request.args.get('driver_age')
    is_driver_alcholic= request.args.get('is_driver_alcholic')
    driver_license_age= request.args.get( 'driver_license_age')
    vehicle_age= request.args.get('vehicle_age')
    vehicle_mileage = request.args.get( 'vehicle_mileage')
    int_features = np.array([driver_age, is_driver_alcholic, driver_license_age, vehicle_age, vehicle_mileage]).reshape(1,-1)
    prediction = boost_flask.predict(xgb.DMatrix(int_features))
    return 'The Likelihood of Vehicle Accident is: {} '.format(prediction[:,1])

if __name__ == "__main__":
    app.run(debug=True)