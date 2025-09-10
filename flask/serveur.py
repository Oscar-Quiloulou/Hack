from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/ping', methods=['GET'])
def ping():
    return "Serveur actif", 200

@app.route('/upload', methods=['POST'])
def upload_video():
    file = request.files.get('file')
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        return f"Fichier reçu : {file.filename}", 200
    return "Aucun fichier reçu", 400
