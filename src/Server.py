'''
Created on 18 Jan 2014

@author: marvin
'''
import socket


HOST = 'localhost'
PORT = 30003
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Server: Connected by', addr
while 1:
    data = conn.recv(1024)
    if not data: break
    print data
    
    #conn.sendall(data)
#conn.close()