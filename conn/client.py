import socket
import threading
import time


if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.3.5",8888))
    print(s.recv(1024).decode('utf-8'))
    for data in [b'zhangsan',b'lisi',b'wangwu']:
        s.send(data)
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()
