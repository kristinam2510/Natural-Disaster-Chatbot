from flask import Flask, request, jsonify
import base64
import io
from PIL import Image

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({"error": "No image provided"}), 400

    image_base64 = data['image']
    try:
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        image.save('uploaded_image.png')
        return jsonify({"status": "success", "message": "Image uploaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
 