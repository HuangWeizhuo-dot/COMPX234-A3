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
def format_length(s):
    return f"{len(s):03d}"

def main():
    host = sys.argv[1]
    port = int(sys.argv[2])
    fp = sys.argv[3]
    s = socket.socket()
    s.connect((host, port))
    
    with open(fp) as f:
        for line in f:
            line = line.strip()
            parts = line.split(maxsplit=2)
            cmd, k = parts[0], parts[1]
            v = parts[2] if len(parts)>=3 else ''
            
            if cmd == 'PUT':
                msg = f'P {k} {v}'
            elif cmd == 'READ':
                msg = f'R {k}'
            elif cmd == 'GET':
                msg = f'G {k}'
            else:
                continue
            
            full = format_length(msg) + msg
            s.send(full.encode())
    s.close()