
# Flask utils
import pickle
import numpy as np
from flask import Flask, redirect, url_for, request, render_template

import joblib

app = Flask(__name__)

import sklearn as sk

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('home.html')


@app.route('/about.html', methods=['GET'])
def about():
    # Main page
    return render_template('about.html')
	
	
	
@app.route('/home.html', methods=['GET'])
def home():
    # Main page
    return render_template('home.html')
	

@app.route('/logout.html', methods=['GET'])
def logout():
    # Main page
    return render_template('login.html',msg="logout")
	


@app.route('/login.html', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		username=request.form['username']
		password=request.form['password']
		
		if username=="admin" and password=="admin":
			return render_template('index.html')
		else:
			return render_template('login.html',msg="failed")
		
	else:
		return render_template('login.html')
		



@app.route('/fetus', methods=['GET', 'POST'])
def predictfetushealth():
    if request.method == 'POST':

        testdata=[]

        for item in request.form.values():
            testdata.append(float(item))
          

        test=np.array( [testdata])
        print("test data is ",test)

       
        objectfile = joblib.load('fetusmodel.pkl')

        testdata = np.array([testdata])
        prediction = objectfile.predict(testdata)
        print(f"Result of prediction = {prediction[0]}")

        index=int(round(prediction[0]))
        # 'Pathological','Suspect','Normal'
        labels={3:"Pathological",2:"Suspect",1:"Normal"}
        
        return render_template('fetusform.html',result=labels[index] )
    else:
        return render_template('fetusform.html')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
