#!/usr/bin/python

##################################################
# Filename: server.py                            #
##################################################
# File ini adalah main file untuk web server     #
# web yang ditulis dalam bahasa Python           #
##################################################

# Mengimpor modul yang dibutuhkan
from socket import *
import sys
import requestParse
import createResponse
import requestHandler

def main():
    # SERVER_HOST dan SERVER_PORT diambil dari 
    # argumen pertama dan kedua saat operator server
    # menjalankan file ini dengan perintah:
    # python server.py SERVER_HOST SERVER_PORT
    # Contoh: python server.py 127.0.0.1 8000
    SERVER_HOST = sys.argv[1]
    SERVER_PORT = int(sys.argv[2])

    # Membuat soket server. AF_INET menunjukkan
    # bahwa jaringan menggunakan koneksi IPv4.
    # Karena server menggunakan TCP, maka digunakan
    # SOCK_STREAM
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Bind (ikat) nomor port kepada soket server
    serverSocket.bind(('', SERVER_PORT))

    # Menunggu dan mendengarkan permintaan koneksi TCP dari klien
    serverSocket.listen(1)

    # Memberi keterangan bahwa server sudah siap terkoneksi
    # pada alamat dan port yang telah ditentukan sebelumnya
    print("Ready to serve at port", SERVER_PORT)

    # Forever looping (akan berhenti jika operator server menekan Ctrl+C)
    while True:
        # Membentuk socket baru connectionSocket untuk klien
        connectionSocket,  addr = serverSocket.accept()
        request = connectionSocket.recv(1024).decode()
        print(request)
        parsed = requestParse.parseRequest(request)
        print(parsed)
        response = requestHandler.handle_request(request)
        print("="*30)
        print("Here is a response for the client:")
        print(response)
        print("="*30)
        connectionSocket.send(response.encode())
        connectionSocket.close()

    serverSocket.close()

if __name__=="__main__":
    main() 
