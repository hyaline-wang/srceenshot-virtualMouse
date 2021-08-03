import win32gui
import win32api
m=win32gui.GetCursorPos()
dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)
win32gui.SetPixel(dc, 0, 0, red)  # draw red at 0,0
while True:
    n=win32gui.GetCursorPos()
    for i in range(n[0]-m[0]):
        win32gui.SetPixel(dc, m[0]+i, m[1], red)
        win32gui.SetPixel(dc, m[0]+i, n[1], red)
    for i in range(n[1]-m[1]):
        win32gui.SetPixel(dc, m[0], m[1]+i, red)
        win32gui.SetPixel(dc, n[0], m[1]+i, red)

