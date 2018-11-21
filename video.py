#!/usr/bin/python
# coding=utf-8

import av
from av.frame import Frame
from av.packet import Packet
from av.stream import Stream
from av.utils import AVError
from av.video import VideoFrame

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pygame

import sys, time, signal, os

print("终端模式下，你可以按下ctrl+c键结束程序")

def signal_handler(signal, frame):
    print("\n你摁下了Ctrl+C!程序结束")
    pygame.mixer.music.stop()
    Endt = time.time()
    print("播放了："),
    print(Endt - t),
    print("秒")
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)



# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 20
# DIN = 21
# DC = 19
# RST = 26
# CS = 13

# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
# disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)



# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()

image = Image.open('test.png').convert('1')

# Alternatively load a different format image, resize it, and convert to 1 bit color.
#image = Image.open('happycat.png').resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')

# 5110.mp4 84*48 24帧，无音频

video_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '5110.mp4'))
print('Loading {}...'.format(video_path))

clip = av.open(video_path)

t = time.time()# 记录视频载入时间

# pygame.init()
# track = pygame.mixer.music.load('5110.mp3')
# pygame.mixer.music.play()
# 加载音频


for frame in clip.decode(video=0):
    starttime = time.time() # 记录开始时间

    print('{} ------'.format(frame.index))
    imgs = frame.to_image() # 提取视频帧
    # img = imgs.resize((LCD.LCDWIDTH, LCD.LCDHEIGHT), Image.ANTIALIAS).convert('1')  ## 将图片分辨率调整为屏幕大小，色彩1bit
    img = imgs.convert('1')  # 色彩1bit
    disp.image(img)
    disp.display()

    endtime = time.time() #结束时间
    times = endtime - starttime #显示该帧所用时间
    timec = round(times,3)
    print(timec),

    if(timec < 0.040): #该视频为24帧,每帧所用时间1/24=0.041,如果小于0.041则暂停,以免播放过快
        print(0.040-timec) # 测试后发现每帧0.04秒最佳
        time.sleep(0.040-timec)

    endtimes = time.time()
    print(endtimes - starttime)
        

    



