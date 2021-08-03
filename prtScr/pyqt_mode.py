import time
import win32con, win32ui, win32gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys

# find name of window
hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

windowsname = "mouse 模拟 – win32api_mode.py Administrator"
handle = win32gui.FindWindow(None, windowsname)
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
lastTime = time.time()
img = screen.grabWindow(handle).toImage()
print(time.time() - lastTime)
img = screen.grabWindow(handle).toImage()
print(time.time() - lastTime)

img.save("screenshot.jpg")
