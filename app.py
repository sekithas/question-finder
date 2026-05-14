from flask import Flask, render_template, request, jsonify
from crewai import Crew, Process
import os

from agents import finder
from tasks import finder_task
from vision import extract_text_from_image


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'bmp'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Please upload an image.'}), 400
    filename = file.filename
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    imagePath = os.path.join(UPLOAD_FOLDER, filename)
    questionText = extract_text_from_image(imagePath)

    questionFinder = Crew(
        agents = [finder],
        tasks = [finder_task],
        process = Process.sequential,
        verbose = True,
        max_rpm = 30,
    )

    result = questionFinder.kickoff(inputs = {"question_text": questionText})

    return jsonify({'success': True, 'filename': filename, 'year': str(result)})

if __name__ == '__main__':
    app.run(debug=True)