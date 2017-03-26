#coding:utf-8

#!/usr/bin/env python3
'''
4位验证码
'''
import random
from PIL import Image,ImageFont,ImageDraw
def rndtxt():
    txt_list = []
    # 大写字母
    txt_list.extend([i for i in range(65,90)])
    # 小写字母
    txt_list.extend([i for i in range(97,123)])
    # 数字
    txt_list.extend([i for i in range(48,57)])
    return chr(txt_list[random.randint(0,len(txt_list)-1)])
def rndbgcolor():
    # 背景颜色
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
def rndtxtcolor2():
    # 字体颜色
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
def code():
    weight = 240
    hight = 60
    image = Image.new('RGB',(weight,hight),(255,255,255))
    font = ImageFont.truetype('msyh.ttc',36)
    draw = ImageDraw.Draw(image)
    # 填充背景颜色
    for x in range(weight):
        for y in range(hight):
            draw.point((x,y),fill=rndbgcolor())
    # 生成随机验证码
    for t in range(4):
        draw.text((60 * t + 10,10),rndtxt(),font=font,fill=rndtxtcolor2())
    image.show()
code()