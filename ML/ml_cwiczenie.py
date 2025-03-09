from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import pandas as pd

df = pd.read_csv("bug_reports.csv")

df['Text'] = df['Summary'] + " " + ['Description']

vectorize = TfidfVectorizer(stop_words='english')
X = vectorize.fit_transform(df['Text'])

y = df['Category']

# podzial na zbior treningowy i testowy (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trenowanie modely regresji liniowej
model = LogisticRegression(max_iter=10000) # zmieniamy iteracje żeby znalezc optymalne rozwiazanie, minimalna liczbe iteracji
model.fit(X_train, y_train)

# predykcja na zbiorze testowym
y_pred = model.predict(X_test)

# ocena modely
print(classification_report(y_test, y_pred))

new_bug = ['Data leak in the application']
new_bug_vectorized = vectorize.transform(new_bug)
prediction_category = model.predict(new_bug_vectorized)

print(f'New bug category: {prediction_category[0]}')