from flask import Flask, request, jsonify
from flask_cors import CORS
from mnemonic_generator import generate_mnemonic

app = Flask(__name__)
CORS(app)

@app.route('/generate-mnemonic', methods=['POST'])
def create_mnemonic():
    data = request.json
    concept = data.get('concept')
    if not concept:
        return jsonify({"error": "Concept is required"}), 400
    
    mnemonic = generate_mnemonic(concept)
    return jsonify({"mnemonic": mnemonic})

if __name__ == '__main__':
    app.run(debug=True)