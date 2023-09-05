#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Project Achive 
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2023/9/5 15:41 
'''
import requests
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from lxml import etree


def get_weibo_hotsearch():
    # 1. 发送HTTP请求，获取微博热搜数据
    url = 'https://s.weibo.com/top/summary?cate=realtimehot'
    response = requests.get(url)

    # 2. 解析HTML页面，提取热搜内容
    if response.status_code == 200:
        html_content = response.text
        # 使用XPath解析HTML内容
        root = etree.HTML(html_content)

        # 使用XPath表达式提取热搜列表
        hot_search_list = root.xpath('//td[@class="td-02"]/a/text()')

        return hot_search_list
    else:
        print('无法获取微博热搜数据。')
        return []


def generate_hotsearch_image(hot_search_list):
    # 3. 生成图片
    image_width = 800
    image_height = 600
    background_color = (255, 255, 255)
    text_color = (0, 0, 0)
    font_size = 24

    # 创建图像对象
    image = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    # 选择字体和大小
    font = ImageFont.truetype('arial.ttf', font_size)

    # 绘制热搜内容
    y = 50
    for hot_search in hot_search_list:
        draw.text((50, y), hot_search, fill=text_color, font=font)
        y += font_size + 10

    # 保存图片
    image.save('hotsearch.png')


def send_email(subject, body, to_email):
    # 4. 发送邮件
    from_email = 'your_email@example.com'  # 发件人邮箱
    email_password = 'your_email_password'  # 发件人邮箱密码

    # 设置邮件内容
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject

    # 邮件正文
    message.attach(MIMEText(body, 'plain'))

    # 附件：热搜图片
    filename = 'hotsearch.png'
    attachment = open(filename, 'rb')
    part = MIMEText(attachment.read(), 'base64')
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    message.attach(part)

    try:
        # 使用SMTP发送邮件
        server = smtplib.SMTP('smtp.example.com', 587)  # 修改为你的SMTP服务器和端口
        server.starttls()
        server.login(from_email, email_password)
        server.sendmail(from_email, to_email, message.as_string())
        server.quit()
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败')
        print(str(e))


def main(send_email_flag, to_email):
    if send_email_flag:
        subject = '微博热搜推送'
        hot_search_list = get_weibo_hotsearch()  # 获取微博热搜数据
        body = '\n'.join(hot_search_list)  # 热搜内容作为邮件正文
        generate_hotsearch_image(hot_search_list)  # 生成热搜图片
        send_email(subject, body, to_email)  # 发送邮件


if __name__ == '__main__':
    # 设置是否发送邮件的标志
    send_email_flag = False  # 设为 True 表示发送邮件
    to_email = 'your_email@example.com'  # 设置目标邮箱地址
    main(send_email_flag, to_email)
