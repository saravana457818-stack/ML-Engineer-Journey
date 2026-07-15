# Pandas Notes

## What is Pandas?

Pandas is a Python library used to read, organize, clean, analyze and
prepare data for Machine Learning.

``` python
import pandas as pd
```

## Creating a DataFrame

``` python
import pandas as pd

data={
    "Name":["Ravi","Arun","John"],
    "Age":[20,21,19],
    "Marks":[95,88,91]
}
df=pd.DataFrame(data)
print(df)
```

## Read CSV

``` python
df=pd.read_csv("students.csv")
```

## Explore Data

### head()

``` python
df.head()
df.head(3)
```

Shows first 5 (or n) rows.

### tail()

``` python
df.tail()
df.tail(2)
```

Shows last 5 (or n) rows.

### info()

``` python
df.info()
```

Shows: - Number of rows - Column names - Data types - Non-null values -
Memory usage

### describe()

``` python
df.describe()
```

Statistics for numeric columns: - count - mean - std - min - 25% - 50%
(median) - 75% - max

## DataFrame Properties

``` python
df.shape
df.columns
df.index
```

## Select Columns

``` python
df["Name"]
df[["Name","Marks"]]
```

## iloc (Position Based)

Uses row and column numbers.

``` python
df.iloc[0]
df.iloc[0,2]
df.iloc[0:2]
df.iloc[0:2,0:2]
```

**Stop value is NOT included.**

## loc (Label Based)

Uses row labels and column names.

``` python
df.loc[0]
df.loc[0,"Marks"]
df.loc[:, "Age"]
df.loc[:, ["Name","Marks"]]
df.loc[0:2, ["Name","Marks"]]
```

**Stop label IS included.**

## iloc vs loc

  iloc                loc
  ------------------- ---------------------
  Integer positions   Labels (names)
  `df.iloc[0,2]`      `df.loc[0,"Marks"]`
  Stop excluded       Stop included

## Machine Learning Workflow

``` python
import pandas as pd

df=pd.read_csv("data.csv")

print(df.head())
print(df.info())
print(df.describe())

X=df[["Age","Marks"]]
y=df["Result"]
```

## Cheat Sheet

``` python
import pandas as pd

df=pd.DataFrame(data)
df=pd.read_csv("file.csv")

df.head()
df.tail()
df.info()
df.describe()

df.shape
df.columns
df.index

df["Name"]
df[["Name","Marks"]]

df.iloc[0]
df.iloc[0,2]
df.iloc[0:2]
df.iloc[0:2,0:2]

df.loc[0]
df.loc[0,"Marks"]
df.loc[:, "Age"]
df.loc[:, ["Name","Marks"]]
```

## Practice

1.  Create a student DataFrame.
2.  Save and read a CSV.
3.  Use head() and tail().
4.  Use info().
5.  Use describe().
6.  Select single and multiple columns.
7.  Practice loc and iloc.
8.  Build X and y for ML.
