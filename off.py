#!/usr/bin/env python2.7
import socket

UDP_IP = "home.ianjm.com"
UDP_PORT = 12345
MESSAGE = "001,!R3D1F1|Ceiling Lights|On"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))