from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    """Simple GET endpoint that returns a welcome message"""
    return jsonify({
        'message': 'Hello! Welcome to the Flask app',
        'status': 'success',
        'port': 8000
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Flask App'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)