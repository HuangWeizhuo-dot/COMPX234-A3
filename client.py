import socket
import sys

def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    file = sys.argv[3]
    s = socket.socket()
    s.connect((host, port))
    s.close()

if __name__ == "__main__":
    main()