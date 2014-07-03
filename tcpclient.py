import socket
import time
 
TCP_IP = '192.168.0.163'
TCP_PORT = 5010
BUFFER_SIZE = 1024
MESSAGE = "FFFFFFFFBH"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
#s.send(MESSAGE)
while True:
    data = s.recv(BUFFER_SIZE)
    print data
    if(data=='S'):
        time.sleep(5)
        s.send('N')
#print "connected"
s.close()

#print "received data:", data
