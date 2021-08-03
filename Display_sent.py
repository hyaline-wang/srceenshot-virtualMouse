import PIL.ImageGrab
import cv2
import mss
import numpy
import socket
import struct
import time
if __name__ == "__main__":
    #open socket
    address = ('127.0.0.1', 8002)  # 服务端地址和端口
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket = socket.socket()
    client_socket.connect(address)
    connection = client_socket.makefile('wb')

    # print('[+] Connected with', addr)
    # encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
    # cap = cv2.VideoCapture(1)
    monitor = {"top": 300, "left": 400, "width": 1920 - 800, "height": 1080 - 600}
    sct = mss.mss()
    while True:
        lasttime = time.time()
        # im = PIL.ImageGrab.grab((400, 300, 1920-400, 1080-300))
        img = numpy.array(sct.grab(monitor))
        # print('0:',time.time() - lasttime)
        # # im.show()
        # img = cv2.cvtColor(numpy.asarray(im),cv2.COLOR_RGB2BGR)
        # print('1:', time.time() - lasttime)
        # ret,img = cap.read()
        # print(ret)
        # cv2.imshow("capture", img)
        # cv2.waitKey(1)
        # img = cv2.resize(img,(640,480))
        # 转换为jpg格式
        img_str = cv2.imencode('.jpg', img)[1].tostring()
        print('2:', time.time() - lasttime)
        # 获得图片长度
        s = struct.pack('<L', len(img_str))
        print('3:', time.time() - lasttime)
        # print(s)
        # 将图片长度传输到服务端
        connection.write(s)
        connection.flush()
        # client_socket.sendall(s)
        # client_socket.sendall(img_str)
        # # 传输图片流
        connection.write(img_str)
        connection.flush()
        # cv2.waitKey(1)
        print(time.time()-lasttime)





        # img_encode = cv2.imencode('.jpg', img, encode_param)[1]
        # data = numpy.array(img_encode)
        # stringData = data.tostring()
        # # 首先发送图片编码后的长度
        # # conn.send((str(len(stringData)).ljust(16)).encode())
        # # 然后一个字节一个字节发送编码的内容
        # # 如果是python对python那么可以一次性发送，如果发给c++的server则必须分开发因为编码里面有字符串结束标志位，c++会截断
        # # for i in range(0, len(stringData)):
        # #     sock.send(stringData[i])
        # conn.send(stringData)
        # cv2.imshow("OpenCV",img)
        # cv2.waitKey(10)



