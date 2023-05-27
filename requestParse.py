##################################################
# Filename: requestParse.py                      #
##################################################
# File ini adalah modul untuk melakukan parsing  #
# terhadap request yang diberikan oleh klien     #
##################################################

def parseRequest(request):
    # Fungsi menerima request sebagai parameter,
    # lalu mengembalikan sebuah dictionary yang 
    # berisi spesifikasi/ketentuan yang dimiliki
    # oleh request tersebut.

    # Memperoleh informasi mengenai HTTP method,
    # file yang di-request klien, dan jenis
    # protokol berdasarkan request yang diberikan.
    method = request.split()[0]
    path = request.split()[1]
    protocol = request.split()[2]

    # Anatomi url:
    # *protokol*://*host*:*port*/*path*?*parameter*
    # Jika terdapat parameter maka akan ditambahkan
    # ke dalam dictionary.
    if "?" in path:
        params = path.split("?")[1].split("&")
        path = path.split("?")[0]
        
        paramList = {}
        
        for p in params:
            paramList[p.split("=")[0]] = p.split("=")[1]

            # Jika terdapat parameter "file", maka dibentuklah
            # key berupa "file" dengan value "files/nama_file"
            # Permintaan request file dari klien diberikan dalam
            # parameter file. Hal ini dilakukan saat mengakses
            # halaman files.html, klien dapat memasukkan nama file
            # teks yang dicari dalam folder files/ dalam server.
            # Permintaan dalam metode GET yang menyertakan
            # parameter file=nama_file.txt akan menampilkan
            # isi file teks tadi.
            if "file" in paramList:
                paramList["file"] =  "files/" + paramList["file"]

        return {"method":method, "path":path, "protocol":protocol, "params":paramList} 

    return {"method":method, "path":path, "protocol":protocol}
