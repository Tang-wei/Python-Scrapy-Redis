#coding:utf8
import socket
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

def srvFunc():
    # 1.创建一个socket 采用制定协议族
    skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #print "socket 建立完毕!..........."
    # 2.绑定端口
    skt.bind(("192.168.2.7",8008))
    #print "socket 绑定完毕!..........."

    # 3.接收消息
    while True:
        data,addr = skt.recvfrom(5000)
        print "socket 接收完毕!..........."
        print data.decode('utf-8')
        # 4.回复消息
        text =raw_input('回复：')
        skt.sendto(text.encode('utf-8'),addr)
        #print "socket 回复完毕!..........."
srvFunc()
