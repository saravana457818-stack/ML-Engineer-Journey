# 03_Preprocess_Data

## What is Data Preprocessing?

Data preprocessing is the process of cleaning and transforming raw data
into a format suitable for Machine Learning.

## Why?

Real-world data contains: - Missing values - Duplicate rows - Text
values - Different scales - Incorrect values

Clean data leads to better models.

## Steps

1.  Handle Missing Values

``` python
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(strategy="mean")
```

2.  Remove Duplicates

``` python
df.drop_duplicates(inplace=True)
```

3.  Encode Categorical Data

``` python
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
df["Gender"]=encoder.fit_transform(df["Gender"])
```

4.  Feature Scaling

``` python
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X=scaler.fit_transform(X)
```

5.  Separate Features and Target

``` python
X=df[["Age","Salary"]]
y=df["Buy"]
```

------------------------------------------------------------------------

# 04_Train_Test_Split

## What is Train-Test Split?

Split the dataset into training and testing sets.

Typical ratio:

-   80% Training
-   20% Testing

``` python
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)
```

### Parameters

-   X: Features
-   y: Target
-   test_size: Testing percentage
-   random_state: Makes the split reproducible

## Workflow

Collect Data ↓ Load Data ↓ Preprocess Data ↓ Split Data ↓ Train ↓
Predict ↓ Evaluate
