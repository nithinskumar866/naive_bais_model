from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'E:\projects from desktops\deployAI\naive baise\model\model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    prediction = model.predict([message])[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    return render_template('index.html', prediction=result, input_text=message)

if __name__ == '__main__':
    app.run(debug=True)
