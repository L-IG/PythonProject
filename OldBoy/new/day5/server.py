import socketserver
port = 7024
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            if msg == 'q':
                break
            print(msg)
            info = input('>>>')
            self.request.send(info.encode('utf-8'))



if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1',port),MyServer)
    server.serve_forever()