import Servomotor
from socket import *
from time import ctime
import RPi.GPIO as GPIO

Servomotor.setup()

ctrCmd = ['Up','Down']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print 'Waiting for connection'
        tcpCliSock,addr = tcpSerSock.accept()
        print '...connected from :', addr
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                Servomotor.ServoUp()
                                print 'Increase: ',Servomotor.cur_X
                        if data == ctrCmd[1]:
                                Servomotor.ServoDown()
                                print 'Decrease: ',Servomotor.cur_X
        except KeyboardInterrupt:
                Servomotor.close()
                GPIO.cleanup()
tcpSerSock.close();
