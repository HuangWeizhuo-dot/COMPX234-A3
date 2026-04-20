import socket
import threading

def main():
    HOST = '0.0.0.0'
    PORT = 51234
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print("Server started")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn,)).start()

def handle_client(conn):
    conn.close()

if __name__ == "__main__":
    main()
import socket
import threading
import time

tuple_space = {}
lock = threading.Lock()

def handle_client(conn):
    with lock:
        pass
    conn.close()