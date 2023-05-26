#!/usr/bin/python

##################################################
# Filename: requestHandler.py                    #
##################################################
# File ini adalah file untuk melakukan handle    #
# terhadap request yang diberikan klien          #
##################################################

import requestParse
import createResponse
import showFile

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
    parsed = requestParse.parseRequest(request)

    if parsed["method"]=="GET":
        try:
            f = open(parsed["path"][1:])
            body = f.read()
            if "params" in parsed:
                if "file" in parsed["params"]:
                    body = showFile.show(parsed["path"][1:], parsed["params"]["file"])
            code = 200
        except IOError:
            code = 404
            body = notFoundPage()
        return createResponse.createResponse(code, body)
    else:
        return createResponse.createResponse(400, badRequestPage())
