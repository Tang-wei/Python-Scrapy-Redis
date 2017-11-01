#coding:utf8

import socket
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

def cltFunc():
	
	#1.创建socket
	skt = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	#print "clt socket创建完毕! ........"


	data = raw_input('发送：')
	#2.绑定端口
	skt.sendto(data.encode('utf-8'),("192.168.2.30",8008))
	#print "clt socket发送完毕! ........"
	data,addr = skt.recvfrom(4000)
	#print "clt socket接收完毕! ........"

	print data.decode('utf-8')

while True:
	cltFunc()