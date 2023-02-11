# Import main library
import numpy as np
import joblib
import sklearn
# Import Flask modules
from flask import Flask, request, render_template, jsonify

# Load the rent and sale regressor models from the "src" folder
rent_regressor = joblib.load("src/RandomForest_rent.joblib")
sale_regressor = joblib.load("src/RandomForest_sale.joblib")

# Initialize Flask and set the template folder to "template"
app = Flask(__name__, template_folder='template')

# Create the home route using the "index.html" page
@app.route('/')
def home():
    return render_template('index.html')

# Set a post method to yield predictions on the page
@app.route('/', methods=['GET', 'POST'])
def predict():
    # Obtain all form values and place them in an array, convert into integers
    features = ['numRooms', 'livingArea']
    request_dic = dict(request.form.items())
    X_predict = [int(request_dic[key]) for key in features]
    
    if request_dic['rentOrBuy'] == 'rent':
        prediction = rent_regressor.predict([X_predict])
    elif request_dic['rentOrBuy'] == 'buy':
        prediction = sale_regressor.predict([X_predict])
    else:
        print('problem')
        prediction = [100]
        
    # Round the output to 2 decimal places
    output = round(prediction[0], 2)
    
    # Return the prediction
    return render_template('index.html', prediction_text='Predicted Price of the house is: eur{}'.format(output))

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
