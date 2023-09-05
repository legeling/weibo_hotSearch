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

def get_weibo_hot_search():
    url = 'https://weibo.com/ajax/side/hotSearch'
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()['data']

def main():
    data = get_weibo_hot_search()
    if not data:
        print('获取微博热搜榜失败')
        return
    print(datetime.now().strftime('微博热搜榜 %m月%d日 %H:%M:'))
    print(f"置顶:{data['hotgov']['word'].strip('#')}")
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

        print(f"{i}. {title} {label}")

if __name__ == "__main__":
    main()