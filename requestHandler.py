##################################################
# Filename: requestHandler.py                    #
##################################################
# File ini adalah modul yang berfungsi dalam     #
# melakukan handling terhadap request klien      #
##################################################

# Mengimpor tiga modul yang dibuat sebelumnya
import requestParse
import createResponse
import showFile

# Fungsi notFoundPage() mengembalikan 
# isi halaman 404 not found
def notFoundPage():
    return '''
<http>
    <head>
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>404 Not Found</h1>
    </body>
</http>
    '''

# Fungsi badRequestPage() mengembalikan 
# isi halaman 400 bad request
def badRequestPage():
    return '''
<http>
    <head>
        <title>400 Bad Request</title>
    </head>
    <body>
        <h1>400 Bad Request</h1>
    </body>
</http>
    '''

def handle_request(request):
    # Fungsi handle_request menerima request dari klien
    # Fungsi mengembalikan respons untuk dikirimkan 
    # kepada klien

    # Melakukan parsing terhadap request
    parsed = requestParse.parseRequest(request)

    # Mengecek metode request HTTP. Sejauh ini server
    # hanya dapat menangani request HTTP GET.
    if parsed["method"]=="GET":
        try:
            # Membuka file html yang diminta klien
            f = open(parsed["path"][1:])

            # Menampung isi file html ke dalam variabel body
            body = f.read()

            
            if "params" in parsed:
                # Apabila terapat parameter dalam request 
                # (dari URL yang dimasukkan klien dalam browser),
                # Maka akan memanggil fungsi show() yang ada dalam
                # modul showFile. Ini berfungsi untuk menambahkan 
                # isi file txt ke dalam file html tadi. 
                if "file" in parsed["params"]:
                    body = showFile.show(parsed["path"][1:], parsed["params"]["file"])
            # Jika file html yang diminta klien ada pada server,
            # maka server akan merespons dengan kode response status 200
            code = 200
        except IOError:
            # Jika file html yang diminta klien tidak ada pada server,
            # maka server akan merespons dengan kode response status 404
            # dan isi variabel body adalah laman html dengan tulisan "404 Not Found"
            code = 404
            body = notFoundPage()
        
        # Memanggil fungsi createResponse() pada modul createResponse
        # untuk membuat response lalu dikembalikan untuk dikirim kepada
        # klien.
        return createResponse.createResponse(code, body)
    else:
        # Hal ini akan terjadi jika klien melakukan HTTP request
        # dengan metode selain GET. Server akan mengembalikan
        # respons dengan kode "400 Bad Request"
        return createResponse.createResponse(400, badRequestPage())
