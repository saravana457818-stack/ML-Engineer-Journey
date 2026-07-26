# Scikit-learn Notes – Chapter 4
# Data Preprocessing

> **Goal:** Learn how to clean and prepare data before training a Machine Learning model.

---

# Table of Contents

1. What is Data Preprocessing?
2. Why Data Preprocessing?
3. Types of Data
4. Missing Values
5. Handling Missing Values
6. Encoding Categorical Data
7. Label Encoding
8. One-Hot Encoding
9. Feature Scaling
10. StandardScaler
11. MinMaxScaler
12. Train-Test Split
13. Complete Preprocessing Workflow
14. Best Practices
15. Interview Questions
16. Quick Revision Cheat Sheet

---

# What is Data Preprocessing?

Data Preprocessing is the process of converting raw, messy data into a clean and understandable format before training a Machine Learning model.

Real-world datasets usually contain:

- Missing values
- Duplicate data
- Incorrect values
- Different scales
- Text values
- Outliers

These issues must be fixed before training a model.

---

# Why Data Preprocessing?

Imagine a teacher checking exam papers.

If some papers have:
- Missing answers
- Wrong roll numbers
- Torn pages

The teacher cannot evaluate them correctly.

Similarly, Machine Learning models cannot learn correctly from dirty data.

---

# Machine Learning Pipeline

```
Collect Data
      ↓
Load Data
      ↓
Exploratory Data Analysis (EDA)
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Prediction
```

---

# Types of Data

## Numerical Data

Contains numbers.

Examples

```
Age
Height
Weight
Salary
Marks
Temperature
```

Example

```python
age = 20
salary = 50000
```

---

## Categorical Data

Contains labels or text.

Examples

```
Male
Female

Yes
No

Red
Blue
Green
```

Example

```python
gender = "Male"
```

Machine Learning algorithms cannot directly understand text.

---

# Missing Values

A missing value means data is unavailable.

Example

| Name | Age | Salary |
|------|-----|--------|
| Ram | 21 | 40000 |
| Sam | NaN | 50000 |
| Hari | 24 | NaN |

NaN means

```
Not a Number
```

---

# Detect Missing Values

```python
df.isnull()
```

Output

```
True
False
```

True → Missing

False → Present

---

# Count Missing Values

```python
df.isnull().sum()
```

Example

```
Age       3
Salary    2
```

---

# Total Missing Values

```python
df.isnull().sum().sum()
```

---

# Handling Missing Values

## Method 1 – Remove Rows

```python
df.dropna()
```

Removes every row containing missing values.

Example

Before

| Age |
|-----|
|20|
|NaN|
|25|

After

| Age |
|-----|
|20|
|25|

Use only if very few rows contain missing values.

---

## Method 2 – Remove Columns

```python
df.dropna(axis=1)
```

Removes columns containing missing values.

---

## Method 3 – Fill Missing Values

### Fill with Zero

```python
df.fillna(0)
```

---

### Fill with Mean

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

Best for numerical data.

---

### Fill with Median

```python
df["Age"] = df["Age"].fillna(df["Age"].median())
```

Best when outliers exist.

---

### Fill with Mode

```python
df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
```

Best for categorical data.

---

# Encoding Categorical Data

Machine Learning cannot understand

```
Male

Female

Red

Blue
```

Convert them into numbers.

---

# Label Encoding

Each category receives an integer.

Example

Before

```
Small

Medium

Large
```

After

```
0

1

2
```

---

## Import

```python
from sklearn.preprocessing import LabelEncoder
```

---

## Example

```python
encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])
```

Example

Before

```
Male
Female
Male
```

After

```
1
0
1
```

---

# When to Use Label Encoding?

Use when categories have an order.

Example

```
Low

Medium

High
```

---

# One-Hot Encoding

Creates new columns.

Example

Before

| Color |
|--------|
| Red |
| Blue |
| Green |

After

| Red | Blue | Green |
|------|------|-------|
|1|0|0|
|0|1|0|
|0|0|1|

---

## Using Pandas

```python
pd.get_dummies(df)
```

---

## Using Scikit-learn

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[["Color"]])
```

---

# Difference Between Label Encoding and One-Hot Encoding

| Label Encoding | One-Hot Encoding |
|---------------|------------------|
| Numbers | Binary columns |
| One column | Multiple columns |
| Ordinal data | Nominal data |

---

# Feature Scaling

Suppose we have

| Age | Salary |
|------|---------|
|22|50000|
|30|80000|

Salary has much larger values.

Algorithms may give more importance to Salary.

Scaling solves this issue.

---

# Types of Feature Scaling

1. StandardScaler

2. MinMaxScaler

---

# StandardScaler

Standardizes data.

Formula

```
Z = (X - Mean) / Standard Deviation
```

Properties

- Mean = 0
- Standard Deviation = 1

---

## Import

```python
from sklearn.preprocessing import StandardScaler
```

---

## Example

```python
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

## Advantages

✔ Works well for

- KNN
- Logistic Regression
- SVM
- PCA

---

# MinMaxScaler

Converts values into a range between

```
0

and

1
```

Formula

```
(X - Minimum)

-------------------

(Maximum - Minimum)
```

---

## Import

```python
from sklearn.preprocessing import MinMaxScaler
```

---

## Example

```python
scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
```

---

Example

Before

```
25

50

75
```

After

```
0.0

0.5

1.0
```

---

# StandardScaler vs MinMaxScaler

| StandardScaler | MinMaxScaler |
|----------------|--------------|
| Mean = 0 | Range = 0–1 |
| Std = 1 | Preserves shape |
| Better with outliers | Sensitive to outliers |

---

# Train-Test Split

A dataset should never be used entirely for training.

Split it into

Training Data

Testing Data

Example

```
1000 Records

↓

800 Training

↓

200 Testing
```

---

# Import

```python
from sklearn.model_selection import train_test_split
```

---

# Example

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# Parameters

## test_size

```python
test_size = 0.2
```

20% Testing

80% Training

---

## random_state

```python
random_state = 42
```

Keeps the data split the same every time.

Useful for reproducibility.

---

# Complete Data Preprocessing Example

```python
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("student.csv")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Encode categorical data
encoder = LabelEncoder()

df["Gender"] = encoder.fit_transform(df["Gender"])

# Features and target
X = df.drop("Result", axis=1)
y = df["Result"]

# Scale features
scaler = StandardScaler()

X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# Common Mistakes

❌ Forgetting to handle missing values

❌ Scaling the target column

❌ Encoding numerical columns

❌ Using Label Encoding for unordered categories

❌ Forgetting train-test split

---

# Best Practices

✔ Perform EDA first

✔ Handle missing values

✔ Remove duplicates

✔ Encode categorical variables

✔ Scale numerical features when necessary

✔ Split data before training

✔ Use random_state for reproducibility

---

# Interview Questions

## What is Data Preprocessing?

Data preprocessing is the process of cleaning and transforming raw data into a suitable format before applying Machine Learning algorithms.

---

## Why do we preprocess data?

To improve data quality and increase model performance.

---

## Difference between Label Encoding and One-Hot Encoding

| Label Encoding | One-Hot Encoding |
|---------------|------------------|
| Converts categories into integers | Creates binary columns |
| Ordinal categories | Nominal categories |

---

## Difference between StandardScaler and MinMaxScaler

| StandardScaler | MinMaxScaler |
|----------------|--------------|
| Mean = 0 | Range = 0–1 |
| Better with outliers | Sensitive to outliers |

---

## Why use train_test_split()?

To evaluate the model on unseen data and avoid overfitting.

---

# Quick Revision Cheat Sheet

| Task | Function |
|------|----------|
| Check Missing Values | `df.isnull().sum()` |
| Remove Missing Rows | `df.dropna()` |
| Fill Missing Values | `df.fillna()` |
| Label Encoding | `LabelEncoder()` |
| One-Hot Encoding | `pd.get_dummies()` |
| Standard Scaling | `StandardScaler()` |
| Min-Max Scaling | `MinMaxScaler()` |
| Split Dataset | `train_test_split()` |

---

# Summary

✔ Data Preprocessing

✔ Missing Values

✔ dropna()

✔ fillna()

✔ Label Encoding

✔ One-Hot Encoding

✔ Feature Scaling

✔ StandardScaler

✔ MinMaxScaler

✔ Train-Test Split

✔ Best Practices

✔ Interview Questions

---

# Next Chapter

## Model Training

Topics Covered:

- Supervised Learning
- Unsupervised Learning
- Regression
- Classification
- Linear Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Model Evaluation
- Prediction