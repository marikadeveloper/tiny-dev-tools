# A tool that checks if a specified local port is occupied
import socket
import sys

def check_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('localhost', port))
        s.close()
        return True
    except socket.error:
        return False
    
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python port-checker.py <port>')
        sys.exit(1)
    port = int(sys.argv[1])
    if check_port(port):
        print('Port %d is available' % port)
    else:
        print('Port %d is occupied' % port)

# Usage: python port-checker.py <port>