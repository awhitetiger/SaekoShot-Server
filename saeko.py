from flask import Flask, request, url_for, send_from_directory, render_template
import os
from datetime import datetime
import sys

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
WEB_ROOT = '127.0.0.1:5000'

# Check if command-line arguments are provided
if len(sys.argv) > 1:
    UPLOAD_FOLDER = sys.argv[1]

if len(sys.argv) > 2:
    WEB_ROOT = sys.argv[2]

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['WEB_ROOT'] = WEB_ROOT

# Ensure the 'uploads' folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    images = get_images()
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "no file part"
    
    file = request.files['image']

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        file_url = url_for('uploaded_file', filename=file.filename)
        return app.config['WEB_ROOT'] + file_url
    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def get_images():
    images = []
    for filename in os.listdir('./'+UPLOAD_FOLDER):
        if filename.startswith('screenshot_') and filename.endswith('.png'):
            timestamp_str = os.path.splitext(filename)[0].split('_')[1]
            timestamp = int(timestamp_str)
            image_path = os.path.join('uploads', filename)
            screenshot_url = f'/uploads/{filename}'
            readable_timestamp = convert_timestamp(timestamp)
            images.append({'path': image_path, 'url': screenshot_url, 'timestamp': readable_timestamp})
    return images

def convert_timestamp(timestamp):
    dt_object = datetime.utcfromtimestamp(timestamp)
    return dt_object.strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)