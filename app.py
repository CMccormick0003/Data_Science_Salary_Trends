# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model.pkl','rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    # Get the data from the POST request.
    if request.method == "POST":
        #data = request.get_json(force=True)
        print(request.form['exp'])
        exp = float(request.form['exp'])
        job = float(request.form['job'])
        remote = float(request.form['remote'])
        size = float(request.form['size'])
        print("Data", model.predict([[exp, job, remote, size]]))
        # Make prediction using model loaded from disk as per the data.
        prediction = model.predict([[exp, job, remote, size]])

        # Take the first value of prediction
        output = prediction[0]
        results = ""
        if output == 1:
            results = "$0 - $100K"
        elif output == 2:
            results = "$101K - $200K"
        elif output == 3:
            results = "$201K - $300K"
        elif output == 4:
            results = "Over $300K"
        else:
            results = "Not working"



        return render_template("results.html", output=output, results=results)

if __name__ == '__main__':
    app.run(debug=True)
