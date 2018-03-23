
# -*- coding:utf-8 -*-

import SimpleHTTPServer;
import SocketServer;
from _bsddb import api


@api
@get('/api/users')
def api_get_users():
    return "杰森斯坦森";

PORT = 8000; #指定服务器端口号
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler;
httpd = SocketServer.TCPServer(("192.168.0.139", PORT), Handler);
httpd.serve_forever();


