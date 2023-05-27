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

    # Header respons HTTP dalam bentuk dictionary. 
    # Sejauh ini server hanya dapat membalas dengan Content-Type
    # berupa text/html.
    response_headers = {
        'Content-Type': 'text/html; charset=utf-8',
        'Content-Length': str(len(response_body)),
        'Connection': 'close',
    }

    # Menggabungkan dictionary response_headers menjadi satu string tunggal.
    response_headers_raw = ''.join(f'{k}: {v}\r\n' for k, v in response_headers.items())

    # Pesan HTTP response status berdasarkan kode response_code
    # response_code = 200 -> HTTP/1.1 200 OK
    # response_code = 400 -> HTTP/1.1 400 Bad Request
    # response_code = 404 -> HTTP/1.1 404 Not Found
    if response_code==200:
        response_status = str(response_code) + " OK"
    elif response_code==400:
        response_status = str(response_code) + " Bad Request"
    elif response_code==404:
        response_status = str(response_code) + " Not Found"

    # Mengembalikan string tunggal dari penggabungan antara
    # response_status, response_headers_raw, dan response_body
    return f'HTTP/1.1 {response_status}\r\n{response_headers_raw}\r\n{response_body}'
