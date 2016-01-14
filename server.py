#  coding: utf-8 
import SocketServer, os

# Copyright 2013 Abram Hindle, Eddie Antonio Santos
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Furthermore it is derived from the Python documentation examples thus
# some of the code is Copyright © 2001-2013 Python Software
# Foundation; All Rights Reserved
#
# http://docs.python.org/2/library/socketserver.html
#
# run: python freetests.py

# try: curl -v -X GET http://127.0.0.1:8080/


class MyWebServer(SocketServer.BaseRequestHandler):
    
    def handle(self):
        #self.data = self.request.recv(1024)
        #filename = self.data.split()[1]
        #print(filename)
        self.data = self.request.recv(1024)
        filename = self.data.split()[1]
        #print('filename is' + filename)

        if 'deep' in filename:
            pathname = 'www/deep/index.html'
            basecss = 'www/deep/deep.css'
        else:
            pathname = 'www/index.html'
            basecss = 'www/base.css'

        if filename[-1] == 'l':
            #print('html requested')
            self.request.sendall('HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
            #if os.path.exists(pathname):
            #    self.request.sendall('HTTP/1.1 200 OK\n')
            
            f = open(pathname, 'r')
            dataToSend = ''
            for line in f:
                dataToSend = dataToSend + line
            f.close()
            self.request.sendall(dataToSend)

        elif filename[-1] == 's': #is css
            #print('basecss is '+basecss)
            self.request.sendall('HTTP/1.1 200 OK\nContent-Type: text/css\n\n')

            css = open(basecss, 'r')
            cssToSend = ''
            for line in css:
                cssToSend = cssToSend + line
            css.close()
            self.request.sendall(cssToSend)
       
if __name__ == "__main__":
    HOST, PORT = "localhost", 8080

    SocketServer.TCPServer.allow_reuse_address = True
    # Create the server, binding to localhost on port 8080
    server = SocketServer.TCPServer((HOST, PORT), MyWebServer)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
