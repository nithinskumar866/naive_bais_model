# predict_model.py

import joblib

# Load trained model
model = joblib.load('model/spam_classifier.pkl')

def predict_spam(message):
    prediction = model.predict([message])[0]
    return "Spam" if prediction == 1 else "Ham"

# Example usage
if __name__ == "__main__":
    msg = input("Enter a message: ")
    result = predict_spam(msg)
    print(f"\nPrediction: {result}")
