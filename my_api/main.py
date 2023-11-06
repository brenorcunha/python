from flask import Flask, jsonify
import pandas as pd
#Diference between a API and a website is that API returns a JSON.

# print(table)
#initialize Flask:
app = Flask(__name__)
#Build the functions:
@app.route('/') #'/' means that this will be the homepage. if you want another to be it, just type its address.
def homepage():
    return 'The API is live'

#these 'pages' ar called 'endpoint' in a API.
@app.route('/results')
def results():
    table = pd.read_csv('./my_api/face_recon_2023-10-24_19-44-28.csv')
    results = table['media'].sum()
    #leaving the response presentable.
    response = {'Data ': results}
    return jsonify(response)

@app.run()