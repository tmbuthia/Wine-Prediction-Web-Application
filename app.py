from flask import Flask,render_template, jsonify, request, redirect
import pickle
import numpy as np

# create flask app
app = Flask(__name__)

# Load the pickle model
model= pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Collecting all the 13 features
    float_features = [float(request.form['alcohol']),
                      float(request.form['malic_acid']),
                      float(request.form['ash']),
                      float(request.form['alcalinity_of_ash']),
                      float(request.form['magnesium']),
                      float(request.form['total_phenols']),
                      float(request.form['flavanoids']),
                      float(request.form['nonflavanoid_phenols']),
                      float(request.form['proanthocyanins']),
                      float(request.form['color_intensity']),
                      float(request.form['hue']),
                      float(request.form['od280/od315_of_diluted_wines']),
                      float(request.form['proline'])]

    features = [np.array(float_features)]  # Convert to numpy array
    prediction_proba = model.predict_proba(features)  # Get probabilities
    predicted_class = np.argmax(prediction_proba)     # Get class with highest probability
    
    # Define class names for easier understanding
    class_names = ['Class 0: Wine A', 'Class 1: Wine B', 'Class 2: Wine C']
    
    # Get the most likely class label and its probability
    predicted_label = class_names[predicted_class]
    confidence = prediction_proba[0][predicted_class]

    return render_template('index.html', 
                           prediction_text="The predicted wine type is {} with a confidence of {:.2f}%"
                           .format(predicted_label, confidence * 100))


if __name__ == "__main__":
    app.run(debug=True)