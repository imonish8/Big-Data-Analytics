from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Load Iris target names for decoding
from sklearn.datasets import load_iris
iris = load_iris()
target_names = iris.target_names

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = target_names[prediction[0]]
    return render_template('index.html', prediction_text='Predicted Species: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)

