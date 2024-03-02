from flask import Flask, render_template, Response, send_from_directory, request, jsonify
from classification import WasteClassifier
import requests

app = Flask(__name__)

ESP32_CAM_URL = 'http://192.168.25.222/cam-hi.jpg'

waste_classifier = WasteClassifier()

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/service')
def service():
    return render_template('main.html')

@app.route('/camera_feed')
def camera_feed():
    try:
        # Fetch image from ESP32 CAM
        response = requests.get(ESP32_CAM_URL)
        if response.status_code == 200:
            return Response(response.content, mimetype='image/jpeg')
        else:
            return Response('Failed to fetch image from ESP32 CAM', status=500)
    except Exception as e:
        print(f'Error fetching image from ESP32 CAM: {e}')
        return Response(f'Error: {e}', status=500)

@app.route('/classify', methods=['POST'])
def classify():
    try:
        category = waste_classifier.classify_frame(ESP32_CAM_URL)
        return jsonify({'category': category})
    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/dump', methods=['POST'])
def dump():
    try:
        data = request.json
        waste_category = data['category']
        print(waste_category)
        if waste_category == 'Biodegradable':
            # Dump waste on the left side
            waste_classifier.dump_biodegradable_waste()
        else:
            # Dump waste on the right side
            waste_classifier.dump_non_biodegradable_waste()

        return jsonify({'message': 'Waste dumped successfully'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
