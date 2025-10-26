# train_model.py
# ------------------------------
# Step 1: Train a simple digit recognition model on MNIST dataset
# and save it as model.pkl for Flask app usage.

from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the MNIST-like dataset (handwritten digits 0-9)
digits = load_digits()

X = digits.data
y = digits.target

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
acc = model.score(X_test, y_test)
print(f"✅ Model trained successfully with accuracy: {acc*100:.2f}%")

# Save model as pickle file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("🎉 Model saved as model.pkl")
