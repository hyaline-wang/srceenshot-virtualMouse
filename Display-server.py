import socket
import struct

import cv2
from PIL import Image
import numpy
import io
import logging
import socketserver
from threading import Condition
from http import server
address = ('127.0.0.1', 8002)  # 服务端地址和端口
server_socket = socket.socket()
# 绑定socket通信端口
server_socket.bind(address)
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')

PAGE = """\
<html>
<head>
<title>camera MJPEG streaming demo</title>
</head>
<body>
<h1>PiCamera MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""


class StreamingOutput(object):
    def __init__(self):
        self.frame = None
        self.buffer = io.BytesIO()
        self.condition = Condition()

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    #获得图片长度
                    image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
                    print(image_len)
                    if not image_len:
                        break

                    image_stream = io.BytesIO()
                    #读取图片
                    image_stream.write(connection.read(image_len))

                    image_stream.seek(0)
                    image = Image.open(image_stream)
                    cv2img = numpy.array(image, dtype=numpy.uint8)
                    imgbuffer = image_stream.getvalue()
                    #写入http响应
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(imgbuffer))
                    self.end_headers()
                    self.wfile.write(imgbuffer)
                    self.wfile.write(b'\r\n')
                    # cv2.waitKey()


            except Exception as e:
                logging.warning(
                    'errror streaming client %s: %s',
                    self.client_address, str(e))

        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


output = StreamingOutput()

try:
    # seriveaddress = input("\n示例:169.251.252.109\n请输入设备端IP地址:")
    # port = (input("\n示例:8000\n请输入端口号:"))


    address = ("169.251.252.109", 8000)
    server = StreamingServer(address, StreamingHandler)
    server.serve_forever()
except Exception as e:
    print(e)