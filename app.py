from flask import Flask, render_template, send_from_directory, jsonify
import os
import random

app = Flask(__name__)
UPLOAD_FOLDER = 'static/gifs'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gifs')
def get_gifs():
    gifs = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.gif')]
    return jsonify(gifs)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
