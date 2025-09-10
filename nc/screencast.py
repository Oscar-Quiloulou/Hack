import socket
import cv2
import numpy as np
import pyautogui
import time
import os

def capture_screen_video(filename="capture.mp4", duration=5, fps=10):
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

def send_file_to_server(filename, host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, "rb") as f:
            data = f.read()
            s.sendall(data)
    print("Fichier envoyé.")

if __name__ == "__main__":
    video_file = "capture.mp4"
    capture_screen_video(video_file)
    send_file_to_server(video_file)
    os.remove(video_file)  # Nettoyage après envoi
# Nettoyage après envoi