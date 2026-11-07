import os
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load Iris Dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train Model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

# Create models folder
os.makedirs("models", exist_ok=True)

# Save Model
joblib.dump(model, "models/iris_model.pkl")
print("Model trained and saved successfully!")
