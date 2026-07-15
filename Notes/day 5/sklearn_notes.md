# Scikit-learn (sklearn) Notes

## What is Scikit-learn?

Scikit-learn (`sklearn`) is a popular Python library for Machine
Learning. It provides ready-made algorithms for training, testing, and
evaluating ML models.

-   Install package:

``` bash
pip install scikit-learn
```

-   Import in Python:

``` python
import sklearn
```

> **Why `sklearn` instead of `scikit-learn`?**
>
> -   `scikit-learn` is the package name used with `pip`.
> -   `sklearn` is the module name used in Python code.

------------------------------------------------------------------------

## Why use Scikit-learn?

-   Saves time by providing pre-built ML algorithms.
-   Well-tested and optimized.
-   Easy to learn and widely used in industry.
-   Integrates well with NumPy and Pandas.

------------------------------------------------------------------------

## Common Workflow

1.  Import libraries
2.  Load dataset
3.  Split data into training and testing sets
4.  Create a model
5.  Train the model (`fit`)
6.  Make predictions (`predict`)
7.  Evaluate the model

------------------------------------------------------------------------

## Common Imports

``` python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
```

------------------------------------------------------------------------

## Key Concepts

### Dataset

A collection of data used for training a model.

### Features (X)

Input variables used to make predictions.

### Target (y)

The output value the model should predict.

### Train/Test Split

-   Training data teaches the model.
-   Testing data checks model performance.

Example:

``` python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

### Model

``` python
model = LinearRegression()
```

### Training

``` python
model.fit(X_train, y_train)
```

### Prediction

``` python
predictions = model.predict(X_test)
```

------------------------------------------------------------------------

## Popular Algorithms

-   Linear Regression
-   Logistic Regression
-   Decision Tree
-   Random Forest
-   K-Nearest Neighbors (KNN)
-   Support Vector Machine (SVM)
-   K-Means Clustering

------------------------------------------------------------------------

## Evaluation Metrics

For Regression: - MAE (Mean Absolute Error) - MSE (Mean Squared Error) -
R² Score

For Classification: - Accuracy - Precision - Recall - F1 Score

------------------------------------------------------------------------

## Libraries Used Together

    CSV File
        ↓
    Pandas (Read Data)
        ↓
    NumPy (Numerical Operations)
        ↓
    Scikit-learn (Machine Learning)
        ↓
    Matplotlib (Visualization)

------------------------------------------------------------------------

## Quick Revision

-   Install: `pip install scikit-learn`
-   Import: `import sklearn`
-   Train: `model.fit()`
-   Predict: `model.predict()`
-   Evaluate: Use suitable metrics
