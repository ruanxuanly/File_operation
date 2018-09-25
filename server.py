import os
import socketserver

class myHandle(socketserver.BaseRequestHandler):
    def handle(self):
        print("from connect:"+self.request)

sock = socketserver.ThreadingTCPServer(("0.0.0.0",23),myHandle)
sock.serve_forever()

