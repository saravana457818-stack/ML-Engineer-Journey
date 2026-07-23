# Collect Data & Load Data in Machine Learning (Scikit-learn)

## ML Workflow

``` text
Collect Data
    ↓
Load Data
    ↓
Preprocess Data
    ↓
Train Model
    ↓
Predict
    ↓
Evaluate
```

# 1. Collect Data

## What is Data Collection?

Data collection is the process of gathering data from different sources
for training a Machine Learning model.

> Better Data = Better Model

## Why collect data?

Machine learning learns patterns from examples.

Example:

    Study Hours   Attendance  Pass
  ------------- ------------ ------
              5           90  Yes
              2           60   No
              7           95  Yes

## Sources of Data

-   CSV Files
-   Excel Files
-   Databases (MySQL, PostgreSQL, SQLite)
-   APIs
-   Websites (Web Scraping)
-   Sensors / IoT Devices
-   Public datasets (Kaggle, UCI)

## Types of Data

### Structured

Rows and columns.

### Unstructured

Images, videos, audio, text.

### Semi-Structured

JSON, XML.

## Good Dataset Characteristics

-   Accurate
-   Complete
-   Clean
-   Relevant
-   Large enough

------------------------------------------------------------------------

# 2. Load Data

Loading data means importing the collected dataset into Python.

Usually done using **Pandas**.

``` python
import pandas as pd
df = pd.read_csv("student.csv")
```

## Display Data

``` python
print(df)
```

## First 5 Rows

``` python
df.head()
```

## Last 5 Rows

``` python
df.tail()
```

## Dataset Information

``` python
df.info()
```

## Dataset Shape

``` python
df.shape
```

Example:

``` text
(100, 5)
```

Means:

-   100 Rows
-   5 Columns

## Column Names

``` python
df.columns
```

## Statistical Summary

``` python
df.describe()
```

## Load Excel File

``` python
df = pd.read_excel("students.xlsx")
```

## Load JSON File

``` python
df = pd.read_json("students.json")
```

# Built-in Scikit-learn Datasets

``` python
from sklearn.datasets import load_iris

iris = load_iris()
```

Convert to DataFrame:

``` python
import pandas as pd

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)
```

Popular datasets:

-   load_iris()
-   load_wine()
-   load_digits()
-   load_diabetes()

# Difference

  Collect Data         Load Data
  -------------------- --------------------------
  Gather information   Import into Python
  Before coding        Inside Python
  CSV, API, Database   read_csv(), read_excel()

# Common Errors

## FileNotFoundError

Wrong file path.

## ModuleNotFoundError

Install pandas:

``` bash
pip install pandas
```

# Quick Revision

## Collect Data

-   Gather data
-   CSV
-   Excel
-   Database
-   API
-   Kaggle

## Load Data

-   pandas
-   read_csv()
-   read_excel()
-   head()
-   tail()
-   info()
-   shape
-   describe()
-   columns
-   sklearn.datasets

# Interview Questions

**What is Data Collection?**

Gathering data from different sources.

**What is Loading Data?**

Importing the dataset into Python.

**Which library is commonly used?**

Pandas.

**Which function loads CSV?**

`pd.read_csv()`

**Which sklearn module provides datasets?**

`sklearn.datasets`
