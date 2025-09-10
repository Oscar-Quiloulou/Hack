import socket

HOST = '0.0.0.0'  # écoute sur toutes les interfaces
PORT = 5000       # port d'écoute

def receive_mp3(conn):
    with open('received.mp3', 'wb') as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
    print("Fichier MP3 reçu et sauvegardé.")

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Serveur en écoute sur le port {PORT}...")
        while True:
            conn, addr = s.accept()
            print(f"Connexion de {addr}")
            receive_mp3(conn)
            conn.close()

if __name__ == "__main__":
    main()