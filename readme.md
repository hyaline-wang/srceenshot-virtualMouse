# 显示屏推流和虚拟键鼠控制

<img src="C:\Users\hyaline\AppData\Roaming\Typora\typora-user-images\image-20210803124310241.png" alt="image-20210803124310241" style="zoom:50%;" />



# 概述:

**这是一个显示屏推流和虚拟键鼠控制的程序**。共分为两个端。若为两台机器，则开着游戏的机器为设备端，另一台为处理端。设备端获取画面并通过网络通信发送给处理端。处理端处理画面帧后通过网络通信返回目标信息给主设备。设备端根据监听到的目标信息自动完成键鼠控制。

# 用途

这是一个枪战游戏（生死狙击）的物理外挂控制端程序，画面处理端程序在【】。设备端获取画面并通过网络通信发送给处理端。处理端处理画面帧后通过网络通信返回目标信息给控制端。控制端根据监听到的目标信息自动完成键鼠控制。实现物理外挂

# 使用:
1. 保证两台机器(或本地处理)都处于同一局域网下
2. 关闭防火墙和代理。保证网络通信正常
3. 保证首先启动 Display-server.py 根据提示输入设备端IP号和端口。再启动 pil_test.py 和 virtual_keyboard.py
4. 检查处理端环境(详见readme.txt)，启动处理端predict.py



# 方案说明

## 键鼠控制

使用[DD虚拟鼠标][http://www.ddxoft.com/]，使用的免费版，好用，但是每次使用需要联网，必须管理员权限运行，暂时先这样，有时间试试[pydirectinput](https://github.com/learncodebygaming/pydirectinput)

## 屏幕捕捉

尝试了3种方案，可在prtScr中找到，最开始使用Pillow的库，但是帧率只能到20帧，且截图区域的大小和速度关系不大，pyqt的方案也大概是20帧，mss的帧率和截图区域有比较强的关系，裁切后的画面可以以40帧帧率采集

## 推流

Display_sent.py通过TCP发送图像至Display-server.py,Display-server.py通过web推到局域网



# 实际效果

参考/video中的效果



**效果能看，但不是很稳定**