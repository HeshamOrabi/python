import socket   # lip to use sockets
import urllib.request, urllib.parse, urllib.error

    # Network programs

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySock.connect( ('data.pr4e.org', 80) )

print('\n', mySock)

print('\n------------------------------\n')

    # HTTP request in python

rMySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make a stream sock sutable to go accros the network 
rMySock.connect( ('data.pr4e.org', 80) ) # connect to data.pr4e.org at port 80

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # data to go accros the network
rMySock.send(cmd) # send the data

while True:
    data = rMySock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

rMySock.close()

print('\n------------------------------\n')

    # HTTP request in python using urllib

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
    print(line.decode().strip())

print('\n------------------------------\n')

    # read html

MFhand = urllib.request.urlopen('https://heshamorabi.com/')

for line in MFhand:
    print(line.decode().strip())

print('\n------------------------------\n')