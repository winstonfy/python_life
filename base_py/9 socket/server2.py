#__author__ = 'Winston'
#date: 2020/4/10

import socket
ip_port = ('127.0.0.1',9997)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

print ('server waiting...')

conn,addr = sk.accept()
client_data = conn.recv(1024)
print (str(client_data,"utf8"))
conn.sendall(bytes('你是一个好人，但是我们真不合适!',encoding="utf-8"))

sk.close()
