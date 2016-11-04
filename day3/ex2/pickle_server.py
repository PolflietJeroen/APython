#!/usr/bin/env python3

import socket
import pickle
import time
import signal
import sys

def signal_handler(signal, frame):
    print('\tYou pressed Ctrl+C!')
    sys.exit(0)
    
def main():
    signal.signal(signal.SIGINT, signal_handler)
    with socket.socket() as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('',8002))
        s.listen(1)
        client, addr = s.accept()

        with client.makefile('rb') as f:
            data = pickle.load(f)
            print('Pickle contained: ', data)

        client.send(pickle.dumps('Send me something!'))
        client.close()
if __name__ == "__main__":
    main()
