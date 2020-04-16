#__author__ = 'Winston'
#date: 2020/4/10
import socket
ip_port = ('127.0.0.1',9997)

sk = socket.socket()
sk.connect(ip_port)


sk.sendall(bytes('阿芳，俺喜欢你',encoding="utf8"))

server_reply = sk.recv(1024)
print (str(server_reply,"utf8"))
