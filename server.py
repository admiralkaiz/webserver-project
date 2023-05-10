from socket import *
import sys
import cgi

def handleRequest(message):
    try:
        filename = message.split()[1]
        f = open(filename[1:])
        responseLine = "HTTP/1.1 200 OK\r\n"
        messageBody = f.read()
    except IOError:
        responseLine = "HTTP/1.1 404 Not Found"
        messageBody = '''
        <html>
        <head>
        <title>404 Not Found</title>
        </head>
        <body><h1>404 Not Found</h1></body>
        </html> 
        '''
    return responseLine + "Content-Type: text/html\r\n\r\n" + messageBody

def main():
    SERVER_HOST = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', SERVER_PORT))
    serverSocket.listen(1)

    print("Ready to serve at port", SERVER_PORT)

    while True:
        connectionSocket,  addr = serverSocket.accept()
        request = connectionSocket.recv(1024).decode()
        response = handleRequest(request)
        connectionSocket.send(response.encode())
        connectionSocket.close()

    serverSocket.close()

if __name__=="__main__":
    main() 