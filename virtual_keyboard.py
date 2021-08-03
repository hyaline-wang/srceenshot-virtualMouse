'''
虚拟键盘控制

'''

from ctypes import *
import time
import socket
import json

# DD虚拟码，可以用DD内置函数转换。
vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
        'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
        'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
        '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
        '=': 212, 's': 402, ';': 410}
# 需要组合shift的按键。
vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7', '{': '[', '_': '-',
        '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}


#加载虚拟键盘DD
print("Load DD!")

# 管理员运行
# dd_dll = windll.LoadLibrary('D:\\Project center\\virtual mouse\\DD-vritual\\Drivers\\1.Simple\\DD94687.64.dll')
dd_dll = windll.LoadLibrary('.\\DD-vritual\\Drivers\\1.Simple\\DD94687.64.dll')
time.sleep(2)

st = dd_dll.DD_btn(0) #DD Initialize
if st==1:
    print("OK")
else:
    print("Error")
    exit(101)

#创建socket
address = ('169.251.252.109', 5005)  # 服务端地址和端口
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)  # 绑定服务端地址和端口
s.listen(5)
conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
print('[+] Connected with', addr)
last_shoot_time = time.time()
while True:
    try:
        data = conn.recv(1024)  # buffersize 等于 1024
        if not data:
            conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
            print('[+] Connected with', addr)
            continue
        print('[Received]', data)
        data = data.decode()
        d_dict = json.loads(data)
        # conn.sendall(data.encode())
        print("Mouse move rel.")
        #鼠标移动
        if abs(d_dict['x']) > 10 or abs(d_dict['y']) > 10:
            dd_dll.DD_movR(int(d_dict['x']*0.4), d_dict['y'])
        else:
            # dd_dll.DD_movR(0, 0)
            pass
        #鼠标点击
        if d_dict['shoot'] == 1:
            if (time.time() - last_shoot_time) < 0.2:
                dd_dll.DD_btn(1)
            else:
                dd_dll.DD_btn(2)
                time.sleep(0.010)
                last_shoot_time = time.time()
        else:
            dd_dll.DD_btn(2)

        conn.sendall('112'.encode())
        # time.sleep(0.005)
    except socket.error:
        print("\r\nsocket error,do reconnect ")
        time.sleep(1)
        conn, addr = s.accept()  # 返回客户端地址和一个新的 socket 连接
        print('[+] Connected with', addr)
    except:
        print('\r\nother error occur ')
        time.sleep(3)




# DD 使用示例
# print("Keyboard Left win")
# #LWin is 601 in ddcode, 1=down, 2=up.
# dd_dll.DD_key(601, 1)
# dd_dll.DD_key(601, 2)
# time.sleep(2)

# print("Mouse move abs.")
# time.sleep(2)


# dd_dll.DD_movR(50, 50)
# time.sleep(2)

# print("Mouse Right button ")
# #1==L.down, 2==L.up, 4==R.down, 8==R.up, 16==M.down, 32==M.up
# dd_dll.DD_btn(4)
# dd_dll.DD_btn(8)
# time.sleep(2)

