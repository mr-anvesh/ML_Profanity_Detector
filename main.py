import joblib
import re

# Load the trained model and vectorizer
model = joblib.load('/Users/omtiwari/Desktop/Anvesh/ML Project NAAC/profanity_model.joblib')
vectorizer = joblib.load('/Users/omtiwari/Desktop/Anvesh/ML Project NAAC/tfidf_vectorizer.joblib')

# Load bad words from file
with open('badwords.txt', 'r') as f:
    bad_words = set(word.strip().lower() for word in f)

def predict_profanity(text):
    # Transform the input text
    text_vector = vectorizer.transform([text])
    # Predict the probability of profanity
    return model.predict_proba(text_vector)[0][1]

def censor_text(text):
    words = re.findall(r'\b\w+\b', text)
    censored_text = text
    overall_profanity_score = 0
    
    for word in words:
        profanity_score = predict_profanity(word)
        if profanity_score > 0.5:  # Adjust this threshold as needed
            censored_word = '*' * len(word)
            censored_text = re.sub(r'\b' + re.escape(word) + r'\b', censored_word, censored_text, flags=re.IGNORECASE)
            overall_profanity_score = max(overall_profanity_score, profanity_score)
        elif profanity_score < 0.7:  # Fallback mechanism
            if word.lower() in bad_words:
                censored_word = '*' * len(word)
                censored_text = re.sub(r'\b' + re.escape(word) + r'\b', censored_word, censored_text, flags=re.IGNORECASE)
                overall_profanity_score = 1.00  # Update score to 1.00 if word is in badwords.txt
    
    return censored_text, overall_profanity_score

def main():
    print("ML Profanity Filter")
    print("Enter 'quit' to exit the program.")
    
    while True:
        user_input = input("Enter your text: ")
        
        if user_input.lower() == 'quit':
            print("Exiting the program. Goodbye!")
            break
        
        censored_output, profanity_score = censor_text(user_input)
        print(f"Profanity score: {profanity_score:.2f}")
        print("Censored text:", censored_output)
        print()

if __name__ == "__main__":
    main()
