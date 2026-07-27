# Scikit-learn Chapter 5 Notes
## Model Training & Prediction

# Machine Learning Pipeline

```text
Collect Data
↓
Load Data
↓
Preprocess Data
↓
Split Data
↓
Choose Model
↓
Train Model
↓
Predict
↓
Evaluate
↓
Save Model
```

## What is Model Training?

Training means teaching a machine learning algorithm using historical data so it can learn the relationship between **features (X)** and **target (y)**.

## Importing a Model

```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
```

## Creating a Model

```python
model = LinearRegression()
```

## Training the Model

```python
model.fit(X_train, y_train)
```

## Making Predictions

```python
prediction = model.predict(X_test)
```

Predicting a single value:

```python
model.predict([[5]])
```

## Features vs Target

- **Features (X):** Input variables
- **Target (y):** Output variable

## Complete Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [2,4,6,8],
    "Marks": [35,55,70,90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Marks"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict([[5]])
print(prediction)
```

## Common Algorithms

### Regression
- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet

### Classification
- Logistic Regression
- Decision Tree
- Random Forest
- KNN
- SVM
- Naive Bayes

### Clustering
- K-Means
- DBSCAN
- Agglomerative Clustering

## Important Functions

| Function | Purpose |
|----------|---------|
| `fit()` | Train model |
| `predict()` | Predict output |
| `score()` | Evaluate performance |
| `train_test_split()` | Split dataset |

## Quick Revision

- Import the model.
- Create the model.
- Train using `fit()`.
- Predict using `predict()`.
- Always train before predicting.
- `predict()` expects 2D input (`[[value]]`).
