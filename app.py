from flask import Flask,render_template,url_for,request
import numpy as np
import os
import pickle
model = pickle.load(open('decision.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index1.html',title='Home')

@app.route('/predict',methods=['POST'])
def predict():
    '''For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    int_features = np.array(int_features).reshape(1,-1)
    prediction = model.predict(int_features)
    output = prediction 
    if output > 0:
        output="Genuine"
        return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person.')
    else:
        output = "Fraud"
        return render_template('prediction.html', prediction_text=f'Prediction For Applied Person is {output} Person!!')
   
port = int(os.environ.get('PORT',5000))
if __name__ == "__main__":
    app.run(debug=1,host='0.0.0.0',port=port) # or True             
