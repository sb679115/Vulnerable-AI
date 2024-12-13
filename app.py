from flask import Flask, request, render_template, jsonify
from transformers import pipeline

# Load DistilBERT model for sentiment analysis
nlp = pipeline("sentiment-analysis")

# Flask app setup
app = Flask(__name__)

# Hidden flag and trigger keyword
FLAG = "STURSEC{AI_P3N_T3ST}"
TRIGGER_KEYWORD = "pen_test_key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Get input text from the form
    input_text = request.form.get('text', '')
    
    # Check for the trigger keyword
    if TRIGGER_KEYWORD in input_text:
        return render_template("index.html", response=f"Congratulations! Your flag is {FLAG}")
    
    # Perform sentiment analysis
    result = nlp(input_text)
    sentiment = result[0]['label']
    score = result[0]['score']
    return render_template("index.html", response=f"Sentiment: {sentiment}, Score: {score:.2f}")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5002)

