#__author__ = 'Winston'
#date: 2020/4/10

import socket
ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(2)
print ("服务端启动...")
conn,address = sk.accept()
while True:
    client_data=conn.recv(1024)
    if str(client_data,"utf8")=='exit':
        break
    print (str(client_data,"utf8"))
    server_response=input(">>>")
    conn.sendall(bytes(server_response,"utf8"))

conn.close()
