from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load dataset
X, y = load_iris(return_X_y=True)

# Create model
model = KNeighborsClassifier()

# Train model
model.fit(X, y)

# Predict
predict = model.predict(X)

# Plot
plt.scatter(y, predict)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()