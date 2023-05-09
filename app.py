from flask import Flask, request, jsonify
import requests
pip install flask
pip install jsonify
app = Flask(__name__)

# Replace with your own API key
API_KEY = '8f0e07e8765861bd21b2c54331c0c180'

@app.route('/bin/<bin_number>')
def bin(bin_number):
    url = f'https://api.bincodes.com/bin/?format=json&api_key={API_KEY}&bin={bin_number}'
    response = requests.get(url)
    data = response.json()
    if data['valid']:
        return jsonify({
            'bin': data['bin'],
            'brand': data['brand'],
            'type': data['type'],
            'country': data['country'],
            'bank': data['bank'],
            'emoji': data['emoji']
        })
    else:
        return jsonify({'error': 'Invalid bin number'})

if __name__ == '__main__':
    app.run(debug=True)
