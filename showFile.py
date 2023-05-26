def show(htmlFile, txtFile):
    raw = open(htmlFile).read()
    raw = raw.replace("</body>", "")
    raw = raw.replace("</html>", "")
    try:
        txt = open(txtFile).read()
        raw += "Text file requested is: " + txtFile 
        raw += "<br>Contents:<br>" 
        raw += "<code>" + txt + "</code>"
    except IOError:
        raw += "<h3>Requested text file not found!</h3>"
    raw += "</body>\n</html>"
    return raw
