import socket
import threading
import time


def mythread(socket,addr):
    print("获取到客户 %s:%s 链接" % addr)
    socket.send(b'welcome!')
    while True:
        data=socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        socket.send(("hello %s" % data.decode('utf-8')).encode('utf-8'))
    socket.close()
    print('来自%s:%s链接关闭了'%addr)




if __name__=='__main__':
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(("0.0.0.0",8888))
    s.listen(5)
    print('等待客户端链接.....')
    while True:
        socket,addr=s.accept()
        t=threading.Thread(target=mythread,args=(socket,addr))
        t.start()