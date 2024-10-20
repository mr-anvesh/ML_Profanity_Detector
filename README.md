# ML Profanity Filter

This project implements an profanity filter api using machine learning techniques. It consists of two main components: a model training script and a main application that uses the trained model to detect and censor profanity in user-input text.

## Project Structure

- `train_model.py`: Script for training the profanity detection model
- `main.py`: Main application for running the profanity filter
- `profanity_model.joblib`: Saved trained model
- `tfidf_vectorizer.joblib`: Saved TF-IDF vectorizer

## How It Works

### 1. Model Training (`train_model.py`)

The model training process involves the following steps:

1. **Data Loading**: 
   - The script loads a dataset from `raw_dataset.csv` containing comments and their toxicity labels.

2. **Data Preprocessing**:
   - Combines multiple toxic categories (toxic, severe_toxic, obscene, threat, insult, identity_hate) into a single 'toxic_combined' column.

3. **Data Splitting**:
   - Splits the data into training and testing sets (80% train, 20% test) using `train_test_split` from scikit-learn.

4. **Feature Extraction**:
   - Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to convert text data into numerical features.
   - The `TfidfVectorizer` is configured to use a maximum of 10,000 features and consider both unigrams and bigrams.

5. **Model Training**:
   - Trains a Logistic Regression model on the vectorized training data.
   - The model is configured with a random state for reproducibility and a maximum of 1000 iterations.

6. **Model Evaluation**:
   - Evaluates the model's accuracy on the test set.

7. **Saving the Model and Vectorizer**:
   - Saves the trained model and TF-IDF vectorizer using joblib for later use in the main application.

### 2. Main Application (`main.py`)

The main application uses the trained model to filter profanity in real-time:

1. **Model Loading**:
   - Loads the pre-trained Logistic Regression model and TF-IDF vectorizer.

2. **Profanity Prediction**:
   - The `predict_profanity` function takes a text input, vectorizes it using the loaded TF-IDF vectorizer, and predicts the probability of it being profane using the trained model.

3. **Text Censoring**:
   - The `censor_text` function splits the input text into words and checks each word for profanity.
   - Words with a profanity score above 0.5 (adjustable threshold) are replaced with asterisks.

4. **User Interface**:
   - Provides a command-line interface for users to input text.
   - For each input, it displays the profanity score and a censored version of the text.
   - The program runs in a loop until the user types 'quit'.

## Methods and Techniques Used

1. **TF-IDF Vectorization**: Converts text data into numerical features, capturing the importance of words in the document corpus.

2. **Logistic Regression**: A binary classification algorithm used to predict the probability of text being profane.

3. **Train-Test Split**: Ensures the model is evaluated on unseen data to assess its generalization capability.

4. **Joblib**: Used for efficient saving and loading of Python objects, particularly useful for large numpy arrays and scikit-learn models.

5. **Regular Expressions**: Used in the censoring process to identify and replace profane words while preserving text structure.

## Performance Metrics

Model Accuracy: 0.9549 or 95.49%

Model Precision: 0.9199 or 91.99%

Model Recall: 0.6091 or 60.91%

Model F1 Score: 0.7329 or 73.29%

## Note

The effectiveness of this profanity filter depends on the quality and diversity of the training data. Regular updates to the training data and model can help improve its accuracy and coverage of different types of profanity.

