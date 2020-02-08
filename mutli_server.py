from threading import Thread
import socket

ip_port=('127.0.0.1',9000)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(ip_port)
s.listen(5)
connected_port=[]
def accept(conn,addr):
    while True:
        data=conn.recv(1024)
        for i in connected_port:
            print(i[0],conn)
            if conn!=i[0]:
                i[0].send(data)
while True:
    conn,addr=s.accept()
    connected_port.append((conn,addr))
    aThread=Thread(target=accept,args=[conn,addr])
    aThread.setDaemon(True)
    aThread.start()
