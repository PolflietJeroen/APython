#/!usr/bin/env python3
import time
import pickle
import os
import signal
import sys

def signal_handler(signal, frame):
    print ('\tYou pressed Ctrl+C!')
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    while True: 
        mylist = [f for f in os.listdir("./pickles") if '.p'in f]
        if not mylist:
            print("no new files")
        else:
            print(mylist)
            for fn in mylist:
                os.remove(os.path.join("./pickles",fn))
        time.sleep(5)



if __name__ == "__main__":
    main()
