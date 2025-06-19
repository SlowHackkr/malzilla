from flask import Flask, render_template, request, redirect, url_for
import os
from utils.analyzer import get_file_info, get_hashes, yara_scan
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'exe', 'dll', 'pdf', 'doc', 'docx', 'apk', 'zip', 'rar'}

# ✅ Ensure uploads folder exists at startup (works both locally and on Render)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Analyze
        name, ftype, size, desc = get_file_info(file_path)
        hashes = get_hashes(file_path)
        yara_results = yara_scan(file_path)

        return render_template('index.html',
                               result={
                                   "name": name,
                                   "type": ftype,
                                   "desc": desc,
                                   "size": size,
                                   "hashes": hashes,
                                   "yara": yara_results
                               })
    else:
        return render_template('index.html', error="Unsupported file type!")

if __name__ == '__main__':
    app.run(debug=True)
