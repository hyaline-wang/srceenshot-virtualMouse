"""
Pillow Lib Screen
enviroment Windows 10
"""
import PIL.ImageGrab
import cv2
import time
import numpy

if __name__ == "__main__":
    while True:
        #
        lasttime = time.time()
        # mode
        # im = PIL.ImageGrab.grab((400, 300, 1920 - 400, 1080 - 300))
        im = PIL.ImageGrab.grab(all_screens=True)

        print('pillow read need t :', time.time() - lasttime)
        print('fps :',1/(time.time()-lasttime))

        img = cv2.cvtColor(numpy.asarray(im), cv2.COLOR_RGB2BGR)
        print('decode times:', time.time() - lasttime)
        cv2.imshow("img", img)
        cv2.waitKey(1)
        print('all times:', time.time() - lasttime)
        print(">>>>>>>>>>>>>>>")

