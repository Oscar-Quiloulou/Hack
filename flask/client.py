import cv2
import numpy as np
import pyautogui
import time
import requests
import os

DOSSIER_LOCAL = "videos_en_attente"
SERVER_URL = "http://ton_nom_utilisateur.pythonanywhere.com"

os.makedirs(DOSSIER_LOCAL, exist_ok=True)

def capture_screen_video(filename, duration=5, fps=10):
    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(filename, fourcc, fps, screen_size)

    start_time = time.time()
    while time.time() - start_time < duration:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        time.sleep(1 / fps)

    out.release()

def serveur_disponible(url):
    try:
        r = requests.get(url + "/ping", timeout=3)
        return r.status_code == 200
    except:
        return False

def envoyer_videos_en_attente(dossier, url):
    for fichier in os.listdir(dossier):
        if fichier.endswith(".mp4"):
            chemin = os.path.join(dossier, fichier)
            with open(chemin, 'rb') as f:
                files = {'file': (fichier, f, 'video/mp4')}
                try:
                    r = requests.post(url + "/upload", files=files)
                    if r.status_code == 200:
                        os.remove(chemin)
                        print(f"{fichier} envoyé et supprimé.")
                except:
                    print(f"Échec d'envoi : {fichier}")

if __name__ == "__main__":
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    video_file = os.path.join(DOSSIER_LOCAL, f"capture_{timestamp}.mp4")
    capture_screen_video(video_file)

    if serveur_disponible(SERVER_URL):
        envoyer_videos_en_attente(DOSSIER_LOCAL, SERVER_URL)
    else:
        print("Serveur indisponible, vidéo stockée localement.")
