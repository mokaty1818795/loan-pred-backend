import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, json, jsonify, request
import flask
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

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
    print("methoss")
    json_data1 = request.get_json()

   # return data
   # train_data=pd.DataFrame(data)

   ## data1 = [float(x) for x in data.values()]
   ## print("Data1 Loop")
    # print(data1)
    # Predict

    ##sc_X = StandardScaler()
    ##X_scaled = pd.DataFrame(sc_X.fit_transform(json_data1), columns=json_data1.columns)
    # print(X_scaled)
    # print(data)

    json_data1['Self_Employed'].replace({'Yes': 1, 'No': 0}, inplace=True)
    json_data1['Married'].replace({'Yes': 1, 'No': 0}, inplace=True)
    json_data1['Gender'].replace({'Male': 1, 'Female': 0}, inplace=True)
    json_data1['Education'].replace({'Graduate': 1, 'Not Graduate': 0}, inplace=True)
    json_data1['Property_Area'].replace({'Urban': 2, 'Semiurban': 1, 'Rural': 0}, inplace=True)
    json_data1['Loan_Status'].replace({'Y': 1, 'N': 0}, inplace=True)

    y = json_data1['Loan_Status']  # target
    X = json_data1.drop('Loan_Status', axis=1) 
    
  


    sc_X = StandardScaler()
    X_scaled = pd.DataFrame(sc_X.fit_transform(X), columns=X.columns)
   


    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0)  
    # prediators

    new_model = model.fit(X_train, y_train)
    ypred = new_model.predict(X_test)

    ##prediction = model.predict(np.array(json_data1))

    ##prediction_round = int(prediction.round())

    # print("predicted")
    # if (prediction == 1):
    #     prediction = "Yes"
    # else:
    #     prediction = "No"
    #     prediction = {'prediction': prediction}

    return jsonify(ypred)


def formInputData(input):

    # input.pop("Loan_ID")
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
