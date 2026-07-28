# Chapter 6 – Model Training & Evaluation (Scikit-learn)

## Why Do We Evaluate a Model?

Imagine you're writing an exam.

You don't know whether you passed until you check your marks.

Similarly,

- We train a machine learning model.
- Then we evaluate its performance.
- If the performance is poor, we improve it.

```text
Collect Data
      ↓
Preprocess
      ↓
Split Data
      ↓
Train Model
      ↓
Predict
      ↓
Evaluate Model
```

---

# Train-Test Split

Never test your model using the same data it learned from.

Instead,

```text
Entire Dataset
        │
        ├──────────────┐
        │              │
Training Data      Testing Data
(80%)              (20%)
```

### Training Data

- Used to learn patterns.

### Testing Data

- Used only for checking accuracy.

## Example

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Parameters

### `test_size`

Percentage of testing data.

```text
0.2 → 20%
0.3 → 30%
```

### `random_state`

Controls random shuffling.

```python
random_state = 42
```

Using the same random state gives the same train-test split every time.

Without it:

```text
Run 1 → Different Split

Run 2 → Different Split
```

---

# Model Training

Train the model using the training dataset.

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)
```

### `fit()`

```text
fit()

↓

Learns relationships from training data
```

---

# Prediction

Predict values using the testing data.

```python
y_pred = model.predict(X_test)
```

Workflow

```text
Training Data

↓

fit()

↓

Model Learns

↓

predict()

↓

Predicted Values
```

---

# Accuracy

Accuracy tells us how many predictions are correct.

Formula

```text
Accuracy =
Correct Predictions
-------------------
Total Predictions
```

Example

```text
100 Predictions

90 Correct

Accuracy = 90%
```

Code

```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)

print(accuracy)
```

Output

```text
0.94
```

Meaning

```text
94% Accuracy
```

---

# Confusion Matrix

Used for Classification problems.

Example

```text
                Predicted

              Cat    Dog

Actual Cat     45      5

Actual Dog      2     48
```

### True Positive (TP)

Predicted Positive

Actually Positive

Correct Prediction

---

### True Negative (TN)

Predicted Negative

Actually Negative

Correct Prediction

---

### False Positive (FP)

Predicted Positive

Actually Negative

Wrong Prediction

Also called **Type I Error**

---

### False Negative (FN)

Predicted Negative

Actually Positive

Wrong Prediction

Also called **Type II Error**

Code

```python
from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)

print(cm)
```

---

# Precision

Among all predicted positives,

How many are actually positive?

Formula

```text
Precision =
TP
---------
TP + FP
```

High Precision means fewer False Positives.

Example:

Spam Detection

```text
Email marked as spam

↓

Should actually be spam
```

---

# Recall

Among actual positives,

How many did we correctly identify?

Formula

```text
Recall =
TP
---------
TP + FN
```

High Recall means fewer False Negatives.

Example:

Cancer Detection

Missing a cancer patient is dangerous.

Need High Recall.

---

# F1 Score

Balances Precision and Recall.

Formula

```text
F1 =
2 × Precision × Recall
----------------------
Precision + Recall
```

Used when both Precision and Recall are equally important.

Code

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

Output

```text
precision

recall

f1-score

support
```

---

# Mean Absolute Error (MAE)

Used for Regression.

Formula

```text
MAE = Average |Actual − Predicted|
```

Smaller MAE means a better model.

Code

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, y_pred)
```

---

# Mean Squared Error (MSE)

Squares every prediction error.

Formula

```text
(actual − predicted)²
```

Large errors become much larger.

Example

```text
Error = 10

↓

Squared Error = 100
```

Code

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
```

---

# Root Mean Squared Error (RMSE)

Simply the square root of MSE.

```text
RMSE = √MSE
```

RMSE has the same unit as the target variable.

Code

```python
from sklearn.metrics import root_mean_squared_error

rmse = root_mean_squared_error(y_test, y_pred)
```

If your Scikit-learn version doesn't support it:

```python
from sklearn.metrics import mean_squared_error

rmse = mean_squared_error(y_test, y_pred) ** 0.5
```

---

# R² Score (Coefficient of Determination)

Measures how well the model explains the variance in the data.

Range

```text
1.0  → Perfect Model

0.0  → Same as predicting the average

Negative → Worse than predicting the average
```

Code

```python
from sklearn.metrics import r2_score

score = r2_score(y_test, y_pred)

print(score)
```

---

# Classification vs Regression Metrics

| Classification | Regression |
|---------------|------------|
| Accuracy | MAE |
| Precision | MSE |
| Recall | RMSE |
| F1 Score | R² Score |
| Confusion Matrix | — |

---

# Common Evaluation Functions

| Function | Purpose |
|----------|---------|
| `train_test_split()` | Split data into training and testing sets |
| `fit()` | Train the model |
| `predict()` | Predict unseen data |
| `accuracy_score()` | Classification accuracy |
| `confusion_matrix()` | Display confusion matrix |
| `classification_report()` | Precision, Recall and F1-score |
| `mean_absolute_error()` | Mean Absolute Error |
| `mean_squared_error()` | Mean Squared Error |
| `root_mean_squared_error()` | Root Mean Squared Error |
| `r2_score()` | R² Score |

---

# Complete Machine Learning Workflow

```text
Dataset

↓

Split Data

↓

Train Model

↓

Predict

↓

Evaluate

↓

Improve Model
```

---

# Interview Questions

1. Why do we split data into training and testing sets?
2. What is the purpose of `random_state`?
3. What is the difference between `fit()` and `predict()`?
4. What is overfitting?
5. What is a confusion matrix?
6. Explain TP, TN, FP and FN.
7. Difference between Precision and Recall.
8. When should Recall be preferred over Precision?
9. What is the F1 Score?
10. Explain MAE, MSE, RMSE and R² Score.

---

# Quick Revision

```text
train_test_split()
        │
        ▼
Training Data
        │
        ▼
fit()
        │
        ▼
Model Learns
        │
        ▼
predict()
        │
        ▼
Predictions
        │
        ▼
Evaluate
        │
        ├── Classification
        │      Accuracy
        │      Precision
        │      Recall
        │      F1 Score
        │      Confusion Matrix
        │
        └── Regression
               MAE
               MSE
               RMSE
               R² Score
```