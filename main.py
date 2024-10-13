import joblib
import re

# Load the trained model and vectorizer
model = joblib.load(r'C:\Users\yugya\OneDrive\Desktop\Cursor\ML Project NAAC\profanity_model.joblib')
vectorizer = joblib.load(r'C:\Users\yugya\OneDrive\Desktop\Cursor\ML Project NAAC\tfidf_vectorizer.joblib')

def predict_profanity(text):
    # Transform the input text
    text_vector = vectorizer.transform([text])
    # Predict the probability of profanity
    return model.predict_proba(text_vector)[0][1]

def censor_text(text):
    words = re.findall(r'\b\w+\b', text)
    censored_text = text
    
    for word in words:
        profanity_score = predict_profanity(word)
        if profanity_score > 0.5:  # Adjust this threshold as needed
            censored_word = '*' * len(word)
            censored_text = re.sub(r'\b' + re.escape(word) + r'\b', censored_word, censored_text, flags=re.IGNORECASE)
    
    return censored_text

def main():
    print("AI-Powered Profanity Filter")
    print("Enter 'quit' to exit the program.")
    
    while True:
        user_input = input("Enter your text: ")
        
        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
        
        profanity_score = predict_profanity(user_input)
        censored_output = censor_text(user_input)
        print(f"Profanity score: {profanity_score:.2f}")
        print("Censored text:", censored_output)
        print()

if __name__ == "__main__":
    main()

