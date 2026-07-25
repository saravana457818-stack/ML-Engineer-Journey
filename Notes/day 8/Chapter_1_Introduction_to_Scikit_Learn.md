# Chapter 1: Introduction to Scikit-learn

> Learning Goal: Understand what Scikit-learn is, why it is used, and
> the standard ML workflow.

## Table of Contents

1.  What is Machine Learning?
2.  What is Scikit-learn?
3.  Why Scikit-learn?
4.  Features
5.  Installation
6.  ML Workflow
7.  Estimator API
8.  Scikit-learn Modules
9.  First Program
10. Real-world Examples
11. Best Practices
12. Common Mistakes
13. Interview Questions
14. Practice Exercises
15. Summary

## 1. What is Machine Learning?

Machine Learning (ML) is a branch of AI that enables computers to learn
patterns from data and make predictions without being explicitly
programmed for every rule.

### Traditional Programming

    Rules + Data
          ↓
       Program
          ↓
        Output

### Machine Learning

    Data + Labels
          ↓
     Train Model
          ↓
    Learns Patterns
          ↓
     Predictions

## 2. What is Scikit-learn?

Scikit-learn is a Python library that provides ready-to-use machine
learning algorithms built on NumPy, SciPy, and pandas.

Example:

``` python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

## 3. Why Use Scikit-learn?

-   Beginner-friendly
-   Consistent API
-   Efficient implementations
-   Rich documentation
-   Industry standard

## 4. Features

-   Regression
-   Classification
-   Clustering
-   Preprocessing
-   Model Evaluation
-   Hyperparameter Tuning
-   Pipelines

## 5. Installation

``` bash
pip install scikit-learn
```

Verify:

``` python
import sklearn
print(sklearn.__version__)
```

## 6. Machine Learning Workflow

    Collect Data
        ↓
    Load Data
        ↓
    Preprocess
        ↓
    Train-Test Split
        ↓
    Choose Model
        ↓
    Train (fit)
        ↓
    Predict
        ↓
    Evaluate
        ↓
    Deploy

## 7. Estimator API

``` python
model.fit(X_train, y_train)
pred = model.predict(X_test)
```

## 8. Important Modules

  Module                    Purpose
  ------------------------- ------------------------------
  sklearn.datasets          Built-in datasets
  sklearn.model_selection   Train/Test split
  sklearn.preprocessing     Scaling & Encoding
  sklearn.linear_model      Linear & Logistic Regression
  sklearn.tree              Decision Trees
  sklearn.ensemble          Random Forest
  sklearn.metrics           Evaluation
  sklearn.pipeline          Pipelines

## 9. First Program

``` python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(accuracy_score(y_test, pred))
```

## 10. Real-world Examples

-   Spam Detection
-   Recommendation Systems
-   Disease Prediction
-   Fraud Detection

## 11. Best Practices

-   Clean data
-   Split data correctly
-   Use random_state
-   Start with simple models
-   Evaluate properly

## 12. Common Mistakes

-   Training and testing on same data
-   Ignoring missing values
-   Skipping feature scaling
-   Using only accuracy

## 13. Interview Questions

1.  What is Scikit-learn?
2.  Difference between fit() and predict()?
3.  Why use train_test_split()?
4.  What is an estimator?
5.  What is random_state?

## 14. Practice

-   Install Scikit-learn
-   Load Iris dataset
-   Split data
-   Train Decision Tree
-   Measure accuracy

## 15. Summary

-   Scikit-learn is a powerful ML library.
-   Standard workflow: Load → Preprocess → Train → Predict → Evaluate.
-   Most estimators use fit() and predict().
