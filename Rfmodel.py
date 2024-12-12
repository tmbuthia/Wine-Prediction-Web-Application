import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
from sklearn.datasets import load_wine

# Load the dataset
wine_data = load_wine()

# Access the features and target variable
X = wine_data.data
y = wine_data.target

# Print the feature names
print(wine_data.feature_names)

#Split the dataset into train and test
# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(X_train, y_train)

# Make pickle file of our model
# pickle.dump(classifier, open("model.pkl", "wb"))
pickle.dump(classifier, open("/Users/wanjirungugi/Desktop/projects/codebasics/Flask_ml1/model.pkl", "wb"))

