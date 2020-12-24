import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

not_accepted_val = ["?"]
dataset = pd.read_csv(
    r"C:\Users\asus\Desktop\\risk_factors_cervical_cancer.csv",
    na_values=not_accepted_val,
)

dataset = dataset.iloc[1:, [0, 2, -1]]
dataset.dropna(axis=0, how="any", inplace=True)
X = dataset.iloc[:, [0, 1]]
y = dataset.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=2, test_size=0.2)

from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn import metrics

print(
    "\nGaussian Naive Bayes model accuracy(in %): ",
    metrics.accuracy_score(y_test, y_pred) * 100,
)
print("CONFUSION MATRIX")
print(metrics.confusion_matrix(y_test, y_pred))

answer_prob = model.predict_proba(np.array([32, 2]).reshape(1, -1))
answer = model.predict(np.array([32, 2]).reshape(1, -1))

print("Prediction for person with age=32 and 2 years of smoking:")

answer_prob = model.predict_proba(np.array([32, 2]).reshape(1, -1))

print("Probability of not having cancer: ", answer_prob[0][0])
print("Probability of having cancer: ", answer_prob[0][1])
print(
    f'Prediction: This person {"does not have" if answer[0]==0 else "has"} cervical cancer!'
)
print("Report", metrics.classification_report(y_test, y_pred))
