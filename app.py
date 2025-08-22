from flask import Flask, request, jsonify, render_template
from crypto_utils import hash_identity, verify_identity
from packet_analyzer import analyze_packet
import os

app = Flask(__name__)

SECRET_KEY = "network_secure_key"

@app.route('/', methods=['GET'])
def home():
    # Return HTML template for web UI
    return render_template('home.html')

@app.route('/api', methods=['GET'])
def api_info():
    # JSON endpoint for API documentation
    return jsonify({
        'status': 'ok',
        'message': 'Network Security Analysis API',
        'endpoints': [
            '/api/analyze - POST: Analyze network packets',
            '/api/projects - GET: View available projects'
        ]
    })

@app.route('/projects', methods=['GET'])
def projects():
    # Project data
    projects_data = [
        {
            'name': 'Network Intrusion Detection',
            'description': 'Analyzes network packets to detect potential intrusions',
            'endpoint': '/analyze'
        }
    ]
    
    # Return HTML template for web UI
    return render_template('projects.html', projects=projects_data)

@app.route('/api/projects', methods=['GET'])
def api_projects():
    # JSON endpoint for API
    return jsonify({
        'status': 'ok',
        'projects': [
            {
                'name': 'Network Intrusion Detection',
                'description': 'Analyzes network packets to detect potential intrusions',
                'endpoint': '/api/analyze'
            }
        ]
    })

@app.route('/analyze', methods=['GET'])
def analyze_page():
    # Return HTML template for web UI
    return render_template('analyze.html')

@app.route('/analyze', methods=['POST'])
@app.route('/api/analyze', methods=['POST'])
def analyze():
    # Handle both web form and API requests
    data = request.json
    identity = data['identity']
    message_hash = data['hash']
    packet_features = data['packet']

    if not verify_identity(identity, SECRET_KEY, message_hash):
        return jsonify({'status': 'unauthorized'}), 401

    result = analyze_packet(packet_features)
    return jsonify({'status': 'ok', 'prediction': result})

# Error handlers for better user experience
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Ensure the saved_model directory exists
    os.makedirs('saved_model', exist_ok=True)
    app.run(debug=True)
