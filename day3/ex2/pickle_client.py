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
        s.connect(('localhost', 8002))
        s.send(pickle.dumps(['what','could','i','send']))  # Any payload will do

        with s.makefile('rb') as f:
            data = pickle.load(f)
            print('Pickle contained: ', data)

        while len(data) :
            data = s.recv(1024)

if __name__ == "__main__":
    main()

