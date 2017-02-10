#!/usr/bin/python3

import sys

from subprocess import Popen,PIPE,check_output
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlsplit,parse_qs

DEFAULT_PORT = 4321

def readfile(filepath, binary=True):
    mode = 'rb' if binary else 'r'
    with open(filepath, mode) as fd:
        content = fd.read()
    return content

HTML_COPYFORM = readfile('./templates/copyform.html')
HTML_COPYSUCCESS = readfile('./templates/copied.html')
PNG_FAVICON = readfile('./templates/favicon.png')
TEMPLATE_CLIPBOARD = readfile('./templates/clipboard.html', binary=False)

class LipwigHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        split_result = urlsplit(self.path)
        query = parse_qs(split_result.query)

        if split_result.path in ('/', '/copy'): # HTML form for copying
            self.send_response(200)
            mimetype = 'text/html'
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write(HTML_COPYFORM)
        elif split_result.path=='/do_copy': # GET parameter includes text to copy
            # Send header
            self.send_response(200)
            mimetype = 'text/html'
            self.send_header('Content-type', mimetype)
            self.end_headers()

            if 'text' not in query:
                self.send_error(400, 'No text parameter sent!')
                return
            
            # Copy to clipboard
            copy_string = query['text'][0]
            p = Popen(['xsel', '-bi'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
            p.communicate(input=bytes(copy_string, 'utf-8'))
            p.wait()

            # Send response
            self.wfile.write(HTML_COPYSUCCESS)
        elif split_result.path=='/clipboard':
            # Send header
            self.send_response(200)
            mimetype = 'text/html'
            self.send_header('Content-type', mimetype)
            self.end_headers()

            primary = check_output(['xsel', '-p']).decode('utf-8')
            clipboard = check_output(['xsel', '-b']).decode('utf-8')
            response = TEMPLATE_CLIPBOARD.replace('%primary%', primary).replace('%clipboard%', clipboard)
            self.wfile.write(bytes(response, 'utf-8'))
        elif split_result.path=='/favicon.png':
            # Send header
            self.send_response(200)
            mimetype = 'image/png'
            self.send_header('Content-type', mimetype)
            self.end_headers()

            self.wfile.write(PNG_FAVICON)
        else:
            self.send_error(404, 'File not found!')

def main():
    if len(sys.argv)==2:
        port = int(sys.argv[1])
    else:
        port = DEFAULT_PORT
    try:
        server = HTTPServer(('', port), LipwigHandler)
        print('Started server on port {}.'.format(port))

        server.serve_forever()
    except KeyboardInterrupt:
        print('Ctrl-C pressed. Shutting down server')
        server.socket.close()

if __name__=='__main__':
    main()
