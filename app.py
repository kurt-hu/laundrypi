import time
import os

from flask import Flask, jsonify, send_from_directory, send_file
from gpiozero import Button

app = Flask(__name__, static_folder='web/build', static_url_path='')

# API Routes
@app.route('/api/status', methods=['GET'])
def status():
    """API endpoint that returns a welcome message"""
    return jsonify({
        'message': 'Hello! Welcome to the Flask app',
        'status': 'success',
        'port': 8000
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Flask App'
    })

@app.route('/api/dryer', methods=['GET'])
def isDrying():
    button = Button(4)
    return jsonify({
        'isDrying': button.is_pressed
    })

# Static file serving for SvelteKit
@app.route('/')
def serve_sveltekit():
    """Serve the SvelteKit index.html file"""
    return send_from_directory('web/build', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from SvelteKit build directory"""
    if os.path.exists(os.path.join('web/build', path)):
        return send_from_directory('web/build', path)
    else:
        # For SPA routing, serve index.html for any non-API routes
        return send_from_directory('web/build', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
