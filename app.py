from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder='public', static_url_path='')
CORS(app)

@app.route('/')
def serve_app():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    # Mock-up processing; replace with your actual logic and API integration
    response = f"Processed: {data.get('name', '')}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5174)
