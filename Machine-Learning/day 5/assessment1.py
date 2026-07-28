# Email Spam Detection

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


# Sample Email Dataset

emails = [
    "Congratulations you won a free lottery",
    "Claim your free prize now",
    "Win money by clicking this link",
    "Free recharge available today",
    
    "Meeting scheduled at 10 AM",
    "Please submit your project report",
    "Your class starts tomorrow",
    "Let's discuss the assignment"
]


# Labels
# 1 = Spam
# 0 = Not Spam

labels = [
    1,
    1,
    1,
    1,
    0,
    0,
    0,
    0
]


# Convert text into numbers

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(emails)


# Split dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    labels,
    test_size=0.25,
    random_state=42
)


# Create Model

model = MultinomialNB()


# Train Model

model.fit(
    X_train,
    y_train
)


# Test New Email

new_email = [
    "You won a free prize"
]


new_email_vector = vectorizer.transform(new_email)


prediction = model.predict(
    new_email_vector
)


# Display Result

if prediction[0] == 1:
    print("Spam Email")
else:
    print("Not Spam Email")


# Accuracy

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("Accuracy:", accuracy)