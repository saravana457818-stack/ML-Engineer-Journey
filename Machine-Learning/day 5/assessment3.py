from sklearn.linear_model import LogisticRegression


# Study Hours

X = [
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7]
]


# 0 = Fail
# 1 = Pass

y = [
    0,
    0,
    0,
    1,
    1,
    1,
    1
]


# Create Model

model = LogisticRegression()


# Train

model.fit(
    X,
    y
)


# New Student

hours = [[5]]


result = model.predict(hours)


if result[0] == 1:
    print("Student will Pass")
else:
    print("Student will Fail")