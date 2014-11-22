#!/usr/bin/env python

import sys
import signal
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
 
class AllHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print "----- SOMETHING WAS GET!! ------"
        print self.headers
        self.send_response(200)
    
    def do_PUT(self):
        print "----- SOMETHING WAS PUT!! ------"
        print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print length
    
    def do_POST(self):
        print "----- SOMETHING WAS POST!! ------"
        print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print length
 
def run_on(port):
    print("Starting a server on port %i" % port)
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, AllHandler)
    httpd.serve_forever()
 
if __name__ == "__main__":
    ports = [int(arg) for arg in sys.argv[1:]]
    for port_number in ports:
        server = Thread(target=run_on, args=[port_number])
        server.daemon = True # Do not make us wait for you to exit
        server.start()
    signal.pause() # Wait for interrupt signal, e.g. KeyboardInterrupt