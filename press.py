'''
虚拟键盘控制，测试用

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

print("Load DD!")

dd_dll = windll.LoadLibrary('C:\\Users\\hyaline\\Downloads\\master-master\\Drivers\\1.Simple\\DD94687.64.dll')
time.sleep(2)

st = dd_dll.DD_btn(0) #DD Initialize
if st==1:
    print("OK")
else:
    print("Error")
    exit(101)
flag = True
while True:

    print("Mouse move rel.")
    dd_dll.DD_movR(0,0 )
    if flag is True:
        # #1==L.down, 2==L.up, 4==R.down, 8==R.up, 16==M.down, 32==M.up
        dd_dll.DD_btn(1)
        flag = False
    else:
        # #1==L.down, 2==L.up, 4==R.down, 8==R.up, 16==M.down, 32==M.up
        dd_dll.DD_btn(2)
        flag = True
    time.sleep(0.5)


