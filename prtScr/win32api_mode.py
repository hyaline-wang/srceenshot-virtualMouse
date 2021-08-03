import win32gui

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t is not "":
        print(h, t)

#
#
#
# import time
#
# import win32gui
# import win32ui
# import win32con
# import win32api
#
# last_time = time.time()
# # 获取桌面
# hdesktop = win32gui.GetDesktopWindow()
# # 分辨率适应
# width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
# height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
# left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
# top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
# # 创建设备描述表
# desktop_dc = win32gui.GetWindowDC(hdesktop)
# img_dc = win32ui.CreateDCFromHandle(desktop_dc)
# # 创建一个内存设备描述表
# mem_dc = img_dc.CreateCompatibleDC()
# # 创建位图对象
# screenshot = win32ui.CreateBitmap()
# screenshot.CreateCompatibleBitmap(img_dc, width, height)
# mem_dc.SelectObject(screenshot)
# # 截图至内存设备描述表
# mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)
# # 将截图保存到文件中
# # screenshot.SaveBitmapFile(mem_dc, 'screenshot.bmp')
# # 内存释放
# mem_dc.DeleteDC()
# win32gui.DeleteObject(screenshot.GetHandle())
# print(time.time()-last_time)
