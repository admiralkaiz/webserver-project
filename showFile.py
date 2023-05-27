##################################################
# Filename: showFile.py                          #
##################################################
# File ini adalah modul untuk menambahkan isi    #
# file teks yang diminta ke dalam file html yang #
# telah ada                                      #
##################################################

def show(htmlFile, txtFile):
    # Fungsi show memiliki dua parameter: htmlFile dan txtFile
    # Terdefinisi direktori file html dan file txt. 
    # Fungsi mengembalikan halaman html yang telah ditambahkan isi
    # file txt yang diminta klien, namun jika tidak maka akan menampilkan
    # bahwa file teks yang dicari tidak ditemukan
    # Asumsi bahwa file html dalam direktori htmlFile berada dalam server.

    # Membuka isi file html dari direktori htmlFile,
    # lalu isinya ditampung dalam variabel raw
    raw = open(htmlFile).read()

    # Menghapus dua baris terakhir berupa "</body>" dan "</html>"
    # dari file html yang diberikan.
    raw = raw.replace("</body>", "")
    raw = raw.replace("</html>", "")

    try:
        # Mencoba untuk membuka file txt dalam direktori txtFile
        txt = open(txtFile).read()

        # Jika file txt yang diminta ditemukan direktori txtFile,
        # maka akan ditambahkan isinya ke dalam isi variabel raw
        # yang telah dihapus baris yang berisi "</body>" dan "</html>" 
        raw += "\nText file requested is: " + txtFile 
        raw += "\n<br>\nContents:\n<br>" 
        raw += "\n<code>\n" + txt + "\n</code>\n"
    except IOError:
        # Jika file txt yang diminta tidak ditemukan direktori txtFile,
        # maka akan ditambahkan baris peringatan "Requested text file not found!"
        # ke dalam variabel raw.
        raw += "\n<h3>Requested text file not found!</h3>\n"

    # Menambahkan kembali string "</body>" dan "</html>" dalam dua baris
    # ke dalam variabel raw sebelum dikembalikan.
    raw += "</body>\n</html>"

    # mengembalikan hasil berupa isi file html yang telah dimodifikasi sebelumnya
    return raw
