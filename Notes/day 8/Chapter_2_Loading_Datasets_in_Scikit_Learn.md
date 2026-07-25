# Chapter 2: Loading Datasets in Scikit-learn

## Objectives

-   Understand datasets
-   Load built-in datasets
-   Load CSV files
-   Separate features (X) and target (y)

## What is a Dataset?

A dataset is a collection of observations (rows) and variables
(columns).

  Feature   Description
  --------- -------------------
  Rows      Samples/records
  Columns   Features + Target

### Example

    Hours   Attendance Pass
  ------- ------------ ------
        2           80 No
        5           95 Yes

`Hours` and `Attendance` are **features (X)**.\
`Pass` is the **target (y)**.

------------------------------------------------------------------------

## Types of Datasets

### 1. Built-in Datasets

-   Iris
-   Wine
-   Breast Cancer
-   Digits
-   Diabetes

Example:

``` python
from sklearn.datasets import load_iris
iris = load_iris()
```

### 2. CSV Dataset

``` python
import pandas as pd
df = pd.read_csv("students.csv")
```

------------------------------------------------------------------------

## Understanding a Bunch Object

Most built-in datasets return a **Bunch** object (similar to a
dictionary).

``` python
iris.keys()
```

Important attributes: - `data` - `target` - `feature_names` -
`target_names` - `DESCR`

------------------------------------------------------------------------

## Exploring the Dataset

``` python
print(iris.data.shape)
print(iris.feature_names)
print(iris.target_names)
print(iris.DESCR[:500])
```

------------------------------------------------------------------------

## Features (X) and Target (y)

``` python
X = iris.data
y = iris.target
```

`X` contains input variables.

`y` contains labels to predict.

------------------------------------------------------------------------

## Loading a CSV Dataset

``` python
import pandas as pd

df = pd.read_csv("students.csv")

X = df.drop("Pass", axis=1)
y = df["Pass"]
```

------------------------------------------------------------------------

## Basic Dataset Inspection

``` python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.isnull().sum()
```

------------------------------------------------------------------------

## Common Built-in Datasets

  Dataset         Task
  --------------- ----------------------
  Iris            Classification
  Wine            Classification
  Breast Cancer   Classification
  Diabetes        Regression
  Digits          Image Classification

------------------------------------------------------------------------

## Best Practices

-   Inspect data before training.
-   Check missing values.
-   Verify feature data types.
-   Understand the target column.

------------------------------------------------------------------------

## Common Mistakes

-   Mixing features and target.
-   Ignoring missing values.
-   Using text data directly without preprocessing.

------------------------------------------------------------------------

## Interview Questions

1.  What is a dataset?
2.  Difference between feature and target?
3.  What is a Bunch object?
4.  Name four built-in datasets.
5.  Why inspect data before training?

------------------------------------------------------------------------

## Practice

1.  Load the Iris dataset.
2.  Print `feature_names`.
3.  Print `target_names`.
4.  Print dataset shape.
5.  Load a CSV file and separate `X` and `y`.

------------------------------------------------------------------------

## Summary

-   Datasets are the foundation of every ML project.
-   Scikit-learn provides several built-in datasets.
-   Use pandas for CSV files.
-   Always inspect and understand data before training a model.
