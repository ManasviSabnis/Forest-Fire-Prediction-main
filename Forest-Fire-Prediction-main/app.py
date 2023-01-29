from flask import Flask,request, url_for, redirect, render_template
import numpy as np
import joblib
import pandas as pd
from bs4 import BeautifulSoup as Soup
import csv, js
import io
import json
import os
from werkzeug.datastructures import ResponseCacheControl
from werkzeug.utils import secure_filename
from flask import Flask, render_template, url_for, request, session, redirect, flash, Response


from flask_pymongo import PyMongo
import bcrypt
from pymongo import MongoClient, ssl_support
mongo = MongoClient('mongodb+srv://forestfire:forestfire@cluster0.dv0krch.mongodb.net/test')
app = Flask(__name__)
app.secret_key = "man"

model=joblib.load('forestfiremodel.pkl')
#model = open("D:\sabni\Documents\GitHub\Forest-Fire-Prediction-main\Forest-Fire-Prediction-main\forestfiremodel.pkl", 'rb')
#codedata = pickle.load(model)
#model.close()
#model=open(r"D:\sabni\Documents\GitHub\Forest-Fire-Prediction-main\Forest-Fire-Prediction-main\forestfiremodel.pkl")

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/insert_sheet', methods=['GET','POST'])
def insert_sheet():
    return render_template('insert_sheet.html')

@app.route('/show', methods=['GET','POST'])
def show():
        # features="lxml"
        #a = pd.read_csv(request.form['usernameid'] + ".csv")
    
        
        # print(b)
        # print (request.form["seat_no"])
        return render_template('show.html')


@app.route('/create', methods=['POST'])

def create():
    if 'upload_file' in request.files:
        upload_file = request.files['upload_file']
        # print('dirname:     ', os.path.dirname(__file__))
        upload_file.save(os.path.join( os.path.dirname(__file__), secure_filename(request.form['usernameid'] +  ".csv")))

        #df = pd.read_csv(upload_file.filename)

        #df.fillna('', inplace = True)

        #json_object=df.to_json()
        #print(json_object)

        csvFilePath = request.form['usernameid'] +  ".csv"

        
        # print(a)


        dict1 ={}

        corrected_dict = {}

        with open(csvFilePath,  encoding='utf-8-sig') as csvf:
            csvReader = csv.DictReader(csvf)

           
                # print(rows)
             
            # Assuming a column named 'No' to
            # be the primary key
               
                #print(corrected_dict)
                #mongo.test[request.form['usernameid']].insert({'upload_file': corrected_dict})
                # print(corrected_dict)
    # return (request.form['Year'], request.form['Semester'], request.form['Branch'])
    # return redirect('/dashboard') 
    #mongo.test[request.form['usernameid']].insert({'usernameid':request.form['usernameid'],'upload_file': corrected_dict})
    #flash("Successfully Uploaded File!")
    return render_template('index.html',pred='Successfully Uploaded File!')


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[float(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output))
    else:
        return render_template('index.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
