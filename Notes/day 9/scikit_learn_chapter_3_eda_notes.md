# Scikit-learn Notes - Chapter 3
# Exploratory Data Analysis (EDA)

---

# What is EDA?

EDA (Exploratory Data Analysis) is the process of understanding and analyzing a dataset before building a Machine Learning model.

It helps answer questions like:

- How many rows and columns are present?
- What are the column names?
- Which columns contain missing values?
- Which columns are numerical?
- Which columns are categorical?
- Are there duplicate records?
- Are there outliers?

---

# Machine Learning Workflow

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
Train Model
      ↓
Evaluate Model
      ↓
Prediction
```

---

# Loading Datasets

## 1. Built-in Dataset

```python
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame
```

---

## 2. OpenML Dataset

```python
from sklearn.datasets import fetch_openml

df = fetch_openml(
    "titanic",
    version=1,
    as_frame=True
)["data"]
```

---

# Understanding a DataFrame

A DataFrame is a two-dimensional table consisting of rows and columns.

Example

| Name | Age | Salary |
|------|-----|--------|
| Ram | 23 | 35000 |
| Sam | 25 | 42000 |

- Rows → Records
- Columns → Features

---

# View Data

## First 5 Rows

```python
df.head()
```

## First N Rows

```python
df.head(10)
```

## Last 5 Rows

```python
df.tail()
```

## Last N Rows

```python
df.tail(10)
```

---

# Dataset Shape

```python
df.shape
```

Example

```
(1309, 13)
```

Meaning

- 1309 rows
- 13 columns

Separate rows and columns

```python
rows, columns = df.shape

print(rows)
print(columns)
```

---

# Column Names

```python
df.columns
```

Convert to list

```python
list(df.columns)
```

---

# Data Types

```python
df.dtypes
```

Example

```
age        float64
fare       float64
sex         object
survived     int64
```

---

# Dataset Information

```python
df.info()
```

Displays

- Number of rows
- Number of columns
- Data types
- Non-null values
- Memory usage

---

# Descriptive Statistics

```python
df.describe()
```

Returns

- Count
- Mean
- Standard Deviation
- Minimum
- Maximum
- 25%
- 50%
- 75%

Include categorical columns

```python
df.describe(include="all")
```

---

# Missing Values

Find missing values

```python
df.isnull()
```

Count missing values

```python
df.isnull().sum()
```

Total missing values

```python
df.isnull().sum().sum()
```

---

# Duplicate Records

Check duplicates

```python
df.duplicated()
```

Count duplicates

```python
df.duplicated().sum()
```

Remove duplicates

```python
df.drop_duplicates()
```

---

# Selecting Columns

Single Column

```python
df["age"]
```

Multiple Columns

```python
df[["age", "fare"]]
```

---

# Unique Values

```python
df["sex"].unique()
```

Count unique values

```python
df["sex"].nunique()
```

---

# Value Counts

```python
df["sex"].value_counts()
```

Example

```
male      843
female    466
```

---

# Select Data Types

Numerical columns

```python
df.select_dtypes(include="number")
```

Categorical columns

```python
df.select_dtypes(include="object")
```

---

# Random Sampling

Random 5 rows

```python
df.sample(5)
```

Random 10 rows

```python
df.sample(10)
```

---

# Statistical Functions

Maximum

```python
df["fare"].max()
```

Minimum

```python
df["fare"].min()
```

Mean

```python
df["fare"].mean()
```

Median

```python
df["fare"].median()
```

Mode

```python
df["sex"].mode()
```

Standard Deviation

```python
df["fare"].std()
```

---

# Correlation

```python
df.corr(numeric_only=True)
```

Correlation values range from

```
-1  → Strong Negative Correlation

 0  → No Correlation

+1  → Strong Positive Correlation
```

---

# Save Dataset

```python
df.to_csv("titanic.csv", index=False)
```

---

# Read CSV

```python
import pandas as pd

df = pd.read_csv("titanic.csv")
```

---

# Complete EDA Workflow

```python
df.head()

df.shape

df.columns

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df.dtypes

df["column_name"].value_counts()
```

---

# Interview Questions

### What is EDA?

EDA is the process of exploring and understanding a dataset before applying Machine Learning algorithms.

---

### Why is EDA important?

- Understand the dataset
- Find missing values
- Detect duplicates
- Detect outliers
- Understand feature distributions
- Improve preprocessing

---

### Difference between `head()` and `tail()`

| head() | tail() |
|---------|---------|
| First rows | Last rows |

---

### Difference between `shape` and `info()`

| shape | info() |
|--------|--------|
| Returns rows & columns | Returns complete dataset information |

---

### Difference between `unique()` and `nunique()`

| unique() | nunique() |
|-----------|-----------|
| Shows unique values | Returns number of unique values |

---

### Difference between `isnull()` and `isnull().sum()`

| isnull() | isnull().sum() |
|-----------|----------------|
| Returns True/False | Counts missing values |

---

# Chapter Summary

✔ What is EDA

✔ Loading datasets

✔ DataFrame

✔ head()

✔ tail()

✔ shape

✔ columns

✔ info()

✔ describe()

✔ dtypes

✔ isnull()

✔ duplicated()

✔ unique()

✔ value_counts()

✔ select_dtypes()

✔ sample()

✔ Statistical functions

✔ Correlation

✔ Save CSV

✔ Read CSV

✔ Complete EDA Workflow

---

# Next Chapter

## Data Preprocessing

- Handling Missing Values
- Encoding Categorical Data
- Feature Scaling
- Label Encoding
- One-Hot Encoding
- StandardScaler
- MinMaxScaler