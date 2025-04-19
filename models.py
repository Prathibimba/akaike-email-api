import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model(data_path='data/processed_emails.csv'):
    df = pd.read_csv(data_path)
    X = df['masked_email']
    y = df['type']

    pipe = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression(max_iter=300))
    ])

    pipe.fit(X, y)
    joblib.dump(pipe, 'email_classifier.pkl')

def classify_email(email_text):
    model = joblib.load('email_classifier.pkl')
    return model.predict([email_text])[0]
