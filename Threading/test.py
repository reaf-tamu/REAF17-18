import time
import threading

def write10():
    for i in range(1, 10):
        file = open('testfile.txt', 'w')
        file.write(str(i) + '\n')
        file.close()
        time.sleep(1)

def read10():
    for i in range(1,10):
        file = open('testfile.txt', 'r')
        print file.read()
        file.close()
        time.sleep(1)

threading.Thread(target=write10).start()
threading.Thread(target=read10).start()
