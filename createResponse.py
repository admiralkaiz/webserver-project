#!/usr/bin/python

##################################################
# Filename: createResponse.py                    #
##################################################
# File ini adalah modul untuk menghasilkan res-  #
# pons yang diberikan oleh server terhadap klien #
##################################################


def createResponse(response_code, response_body):
    # Fungsi menerima integer response_code (dapat berupa 200 maupun 404)
    # dan string response_body sebagai isi dari respons
    # yang akan dikirimkan
    # Fungsi mengembalikan string respons berupa header dan body.

    response_headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': str(len(response_body)),
        'Connection': 'close',
    }

    response_headers_raw = ''.join(f'{k}: {v}\r\n' for k, v in response_headers.items())

    return f'HTTP/1.1 {str(response_code)}\r\n{response_headers_raw}\r\n{response_body}'
