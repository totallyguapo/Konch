from flask import Flask, render_template, send_from_directory, jsonify
import os
import random

app = Flask(__name__)
GIF_FOLDER = 'static/gifs'
MP3_FOLDER = 'static/mp3s'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gifs')
def get_gifs():
    gifs = [f for f in os.listdir(GIF_FOLDER) if f.endswith('.gif')]
    return jsonify(gifs)

@app.route('/gifs/<filename>')
def serve_gif(filename):
    return send_from_directory(GIF_FOLDER, filename)

@app.route('/mp3s')
def get_mp3s():
    mp3s = [f for f in os.listdir(MP3_FOLDER) if f.endswith('.mp3')]
    return jsonify(mp3s)

@app.route('/mp3s/<filename>')
def serve_mp3(filename):
    return send_from_directory(MP3_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
