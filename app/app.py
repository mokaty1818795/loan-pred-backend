import pickle
import numpy as np
from flask import Flask, render_template, json, jsonify, request
import flask
import os
model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/data/test', methods=['GET'])
def getData():
    with open('./data/test.csv', 'r') as f:
        data = f.readlines()[1:5]
        return jsonify(data)


@app.route('/predictloan', methods=['POST'])
def predictLoan():
    print("methos s")
    data = request.get_json()
    print("method call")
    # formInputData(data)
    print("Data Below")
    print(data)
    data1 = [float(x) for x in data.values()]
    print("Data1 Loop")
    print(data1)
    # Predict
    print("Prediction Starts")
    prediction = model.predict(data1)
    prediction = int(prediction.round())
    print("predicted")
    if (prediction == 1):
        prediction = "Yes"
    else:
        prediction = "No"
        prediction = {'prediction': prediction}

    return jsonify(prediction)


def formInputData(input):

    input.pop("Loan_ID")
    # Format the gender
    if (input["Gender"] == 'Female'):
        input["Gender"] = 0
    else:
        input["Gender"] = 1

    # Format Married
    if (input["Married"] == "No"):
        input["Married"] = 0
    else:
        input["Married"] = 1

    # Format Education
    if (input["Education"] == 'Not Graduate'):
        input["Education"] = 0
    else:
        input["Education"] = 1

    # Format Self_Employed
    if (input["Self_Employed"] == 'No'):
        input["Self_Employed"] = 0
    else:
        input["Self_Employed"] = 1

    # Format Property_Area
    if (input["Property_Area"] == 'Rural'):
        input["Property_Area"] = 0
    elif (input["Property_Area"] == 'Semiurban'):
        input["Property_Area"] = 1
    else:
        input["Property_Area"] = 2


@app.route('/accuracy', methods=['GET'])
def accuracy():
    # read content from file
    with open('./data/accuracy.txt', 'r') as modelAccuracy:
        data = modelAccuracy.read().split(':')[1]

        data = int(float(data))
        accuracy = {'ModelAccuracy': data}
        return jsonify(accuracy)


if __name__ == "__main__":
    app.run(debug=True)
