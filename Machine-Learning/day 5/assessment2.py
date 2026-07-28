from sklearn.tree import DecisionTreeClassifier


# Features
# Income, Credit Score

X = [
    [30000,500],
    [40000,600],
    [60000,700],
    [80000,800],
    [90000,850]
]


# 0 = Reject
# 1 = Approve

y = [
    0,
    0,
    1,
    1,
    1
]


model = DecisionTreeClassifier()


model.fit(
    X,
    y
)


# New Customer

customer = [
    [70000,750]
]


result = model.predict(customer)


if result[0] == 1:
    print("Loan Approved")
else:
    print("Loan Rejected")