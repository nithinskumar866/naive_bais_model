import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load dataset (correct path)
df = pd.read_csv(r'E:\projects from desktops\deployAI\naive baise\dataset\spam.csv', encoding='latin-1')

# Keep only necessary columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Convert labels to 0 and 1
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Create pipeline
model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train the model
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, r'E:\projects from desktops\deployAI\naive baise\model\model.pkl')

print("✅ Model trained and saved successfully!")
