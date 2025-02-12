#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：WeiboHotSearch
@File    ：main.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2023/9/5 15:41 
'''

import requests
from datetime import datetime
from urllib.parse import quote

def hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']

def main(num):
    data = hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return
    print(datetime.now().strftime('微博热搜榜 20%y年%m月%d日 %H:%M'))
    print(f"置顶:{data['hotgov']['word'].strip('#')}")
    for i, rs in enumerate(data['realtime'][:num], 1):
        title = rs['word']
        try:
            label = rs['label_name']
            if label in ['新','爆','沸']:
                label = label
            else:
                label = ''
        except:
            label = ''
        print(f"{i}. {title} {label} 链接：https://s.weibo.com/weibo?q={quote(title)}&Refer=top")
        # print(f"{i}. {title} {label}")

if __name__ == '__main__':
    num = 20 #获取热搜的数量
    main(num)
