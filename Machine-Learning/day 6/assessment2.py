from sklearn.linear_model import LinearRegression

X = [[800], [1000], [1200], [1500], [1800]]

y = [40, 50, 60, 75, 90]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[1400]])

print("Predicted Price:", prediction[0])