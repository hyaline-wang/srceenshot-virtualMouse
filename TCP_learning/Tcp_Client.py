import socket
import sys
import json
address = ('169.251.252.109', 5005)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(address)  # 尝试连接服务端
except Exception:
    print('[!] Server not found ot not open')
    sys.exit()
data = {"x": 0, "y": 0}
a_str = json.dumps({"x": 0, "y": 0})
while True:
    # data['x'] = int(input('Inputx: '))
    # data['y'] = int(input('Inputy: '))
    # a_str = json.dumps(data)
    # s.sendall(a_str.encode())
    data = s.recv(1024)
    if not data:
        break
    # data = data.decode()
    # print('[Recieved]', data)

    # if trigger == '###':  # 自定义结束字符串
    #     break
s.close()