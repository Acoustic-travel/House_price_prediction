from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Set the exchange rate from USD to INR
USD_TO_INR_RATE = 83  # Update this with the current exchange rate

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        bedrooms = float(request.form['bedrooms'])
        bathrooms = float(request.form['bathrooms'])
        floors = float(request.form['floors'])
        sqft_living = int(request.form['sqft_living'])

        features = np.array([[bedrooms, bathrooms, floors, sqft_living]])
        prediction = model.predict(features)

        predicted_price_inr = int(prediction[0] * USD_TO_INR_RATE)
        formatted_prediction = f"{predicted_price_inr:,}"
        return render_template('index.html', prediction=formatted_prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)