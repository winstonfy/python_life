#__author__ = 'Winston'
#date: 2020/4/10

import socket
ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.connect(ip_port)
print ("客户端启动:")

while True:
    inp = input('>>>')
    sk.sendall(bytes(inp,"utf8"))
    if inp == 'exit':
        break
    server_response=sk.recv(1024)
    print (str(server_response,"utf8"))
sk.close()
