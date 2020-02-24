import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from trainer import Classify

UPLOAD_FOLDER = '/wavs/testing'
ALLOWED_EXTENSIONS = set(['mp3', 'wav', '3gp'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['audio']
        file.save("./wavs/testing/audio.wav")
       	print(Classify())
    return ""
if  True:
	app.run("0.0.0.0",8000,debug=True)