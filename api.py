from flask import Flask, request, jsonify
from main import censor_text
import os

app = Flask(__name__)

@app.route('/check_profanity', methods=['POST'])
def check_profanity():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text = data['text']
    censored_text, profanity_score = censor_text(text)

    response = {
        'original_text': text,
        'profanity_score': round(profanity_score, 2),
        'censored_text': censored_text
    }

    return jsonify(response)

if __name__ == '__main__':
    #for render deployment purposes
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
