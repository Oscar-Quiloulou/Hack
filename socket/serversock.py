import socket

def recevoir(conn):
    with open("reception.mp4", "wb") as f:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            f.write(data)
    print("Fichier reçu et sauvegardé.")
    conn.close()

def main():
    host = host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Serveur en écoute sur {host}:{port}")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connexion de: {addr}")
            recevoir(conn)

if __name__ == "__main__":
    main()
