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
def format_length(s):
    return f"{len(s):03d}"

def handle_client(conn):
    while True:
        len_head = conn.recv(3).decode().strip()
        if not len_head:
            break
        data = conn.recv(int(len_head)).decode()
        # process command later
    conn.close()
def handle_client(conn):
    while True:
        len_head = conn.recv(3).decode().strip()
        if not len_head:
            break
        data = conn.recv(int(len_head)).decode()
        parts = data.split(maxsplit=2)
        cmd, key = parts[0], parts[1]
        val = parts[2] if len(parts)>=3 else ''
        
        with lock:
            if cmd == 'P':
                res = 'OK added' if key not in tuple_space else 'ERR exists'
            elif cmd == 'R':
                res = tuple_space.get(key, 'ERR not found')
            elif cmd == 'G':
                res = tuple_space.pop(key, 'ERR not found')
            else:
                res = 'ERR unknown'
        
        conn.send((format_length(res) + res).encode())
    conn.close()