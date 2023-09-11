#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Project Achive 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2023/9/5 15:54 
'''

import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']

def decoding():
    data = hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return
    print(datetime.now().strftime('%y年%m月%d日 %H:%M'))
    # print(f"置顶:{data['hotgov']['word'].strip('#')}")
    hot_li = []
    hot_label = []
    for i, rs in enumerate(data['realtime'][:20], 1):
        title = rs['word']
        try:
            label = rs['label_name']
            if label in ['新','爆']:
                label = label
            else:
                label = ''
        except:
            label = ''
        # hot_li.append(f"{i}. {title} {label}")
        hot_li.append(f"{title}")
        hot_label.append(f"{label}")
    return hot_li,hot_label

def img(li,label):
    # 创建图像
    width= 750
    height = 350 + len(li)*100
    background = Image.new('RGB', (width, height), color=(255, 255, 255))
    # 添加背景图片（如果需要替代顶部像素的背景）
    background_image = Image.open('hot_research.jpg')  # 替换为你的背景图片
    background.paste(background_image, (0, 0))

    # 创建一个空白图像
    line_height = 50  # 每行文字高度
    num_lines = len(li) # 总行数
    font_size = 30  # 字体大小
    text_color = (0, 0, 0)  # 文本颜色
    background_color = (255, 255, 255)  # 背景颜色
    separator_color = (200, 200, 200)  # 分隔符颜色
    separator_height = 2  # 分隔符高度

    image_height = num_lines * line_height  # 图像高度

    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype("heiti.ttf", font_size)
    num_font = ImageFont.truetype("SmileySans.ttf", font_size)
    # 生成文本列表
    lines = li

    # 逐行绘制文本和分隔符
    y = 370
    i = 1
    for line in lines:
        # 绘制编号
        draw.text((35,y),str(i), fill=(255,0,0),font=num_font)
        # 绘制文本
        draw.text((130, y),line, fill=text_color, font=font)
        # 绘制热度
        draw.text((330, y), label[i-1], fill=text_color, font=font)
        y += line_height
        i +=1
        # 绘制分隔符
        draw.rectangle([(0, y-10), (width, y-10 + separator_height)], fill=separator_color)
        y += separator_height

    # 保存图像
    background.save("output.png")

if __name__ == "__main__":
    hot_li = decoding()[0]
    hot_label = decoding()[1]
    img(hot_li,hot_label)