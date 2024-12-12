# Wine-Prediction-Web-Application
This project is a Flask web application that allows users to predict the type of wine based on key chemical properties. The model utilizes a trained Random Forest classifier to classify wines into three categories based on user-specified inputs.
# Features

    a. User-Friendly Interface: Input wine parameters through dropdown menus on a simple web interface.
    b. Machine Learning Backend: A trained Random Forest classifier predicts the wine class.
    c. Prediction Confidence: Displays the confidence percentage for the predicted class.

Project Structure
````
├── app.py                # Main Flask application
├── model.pkl             # Trained Random Forest model
├── Rfmodel.py            # Script to train the model
├── templates/
│   └── index.html        # Frontend HTML template
````
# How It Works
Model Training:
````
The Rfmodel.py script trains a Random Forest model using the scikit-learn wine dataset.
Features include chemical properties such as alcohol content, flavanoids, and color intensity.
After training, the model is serialized and saved as model.pkl using Python's pickle module. This file stores the trained model so it can be reused without retraining.
````
#### Web Interface:
````
index.html is the frontend of the application. It provides a user-friendly interface to input wine parameters.
It contains dropdown menus for all the required features and submits user input to the Flask application.
Parameters include values like Alcohol, Malic Acid, Color Intensity, and others.
````
#### Prediction:
````
User inputs are sent to the Flask backend (app.py), where they are preprocessed.
The Random Forest model (model.pkl) predicts the wine class and confidence score.

This is the main Flask application file that integrates all components:
  a. Loads model.pkl to access the trained model.
  b. Serves the index.html file when the user accesses the root URL.
  c. Handles form submissions from index.html, processes the input, and uses the model to predict the wine type.
  d. Sends the prediction and confidence back to index.html to display results to the user.
Results are displayed on the same webpage.
````
### Installation and Setup
#### Prerequisites
Python 3| Flask | scikit-learn| NumPy| pandas|

Installation Steps
Clone the repository:
````
git clone https://github.com/your-repository/wine-prediction.git
cd wine-prediction
````
Install dependencies:
````
pip install flask scikit-learn numpy pandas
````
Run the application:
````
python app.py
Open the application in your browser at http://127.0.0.1:5000.
````
### Usage
````
Navigate to the web interface.
Select values for the wine parameters from the dropdown menus.
Click the Predict button.
View the predicted wine class and the confidence score.
````
### Example Parameters
Feature	Example Values

| Feature        | Example Values                        |
|----------------|---------------------------------------|
| Alcohol        | Low (12.0), Medium (13.0), High (14.0) |
| Malic Acid     | Low (1.0), Medium (2.0), High (3.0)    |
| Color Intensity| Low (4.0), Medium (6.0), High (8.0)    |
| Proline        | Low (500), Medium (800), High (1000)   |

### Results
Predicted Wine Types:
| Predicted Wine Types |
|----------------------|
| Class 0: Wine A      |
| Class 1: Wine B      |
| Class 2: Wine C      |

Confidence level is displayed alongside the prediction.
#### Future Enhancements
````
  a. Expand the dataset to include real-world wine data.
  b. Add more visualizations to display feature importance.
  c. Deploy the application on a cloud platform like AWS or Heroku for public access.
````
#### License
This project is licensed under the MIT License.

#### Acknowledgments
scikit-learn for the wine dataset and machine learning library.
Flask for making web application development easy and efficient.
