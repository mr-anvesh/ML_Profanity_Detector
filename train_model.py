import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the dataset
df = pd.read_csv(r'C:\Users\yugya\OneDrive\Desktop\Cursor\ML Project NAAC\raw_dataset.csv')

# Combine all toxic categories into one
df['toxic_combined'] = df[['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].max(axis=1)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df['comment_text'], df['toxic_combined'], test_size=0.2, random_state=42)

# Create and fit the TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=10000, ngram_range=(1, 2))
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train the model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train_vectorized, y_train)

# Evaluate the model
X_test_vectorized = vectorizer.transform(X_test)
y_pred = model.predict(X_test_vectorized)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
f1 = f1_score(y_test, y_pred, average='binary')

# Print evaluation metrics
print(f"Model accuracy: {accuracy:.4f}")
print(f"Model precision: {precision:.4f}")
print(f"Model recall: {recall:.4f}")
print(f"Model F1 score: {f1:.4f}")

# Save the model and vectorizer
joblib.dump(model, 'profanity_model.joblib')
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')

print("Model and vectorizer saved successfully.")
