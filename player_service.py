import time
import cgi
import json
from http import server
import os
from player import Player
from urllib.parse import parse_qs


HOST_NAME = '0.0.0.0'
if 'PORT' in os.environ.keys():
    PORT_NUMBER = int(os.environ.get('PORT'))
else:
    PORT_NUMBER = 9000


class PlayerService(server.BaseHTTPRequestHandler):

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.get('content-length'))
            postvars = parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        action = postvars[b'action'][0]

        if 'game_state' in postvars:
            game_state = json.loads(postvars['game_state'][0])
        else:
            game_state = {}


        response = b''
        if action == b'bet_request':
            # response = Player().betRequest(game_state)
            try:
                response = str(Player().betRequest(game_state))
            except BaseException as e:
                print(e)
                response = 0
        elif action == b'showdown':
            Player().showdown(game_state)
        elif action == b'version':
            response = str(Player.VERSION)

        self.wfile.write(bytes(response, encoding="utf-8"))


if __name__ == '__main__':
    server_class = server.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), PlayerService)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
