#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Project Achive 
@File    ：filesName.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2024/10/18 02:49 
'''
import os
import re

# 设置要处理的文件夹路径
folder_path = '/Users/wangjialong/文档/语雀导出/notes'

# 定义日期正则表达式
date_pattern = r'(\d{4})年(\d{1,2})月(\d{1,2})日'
tag_pattern = r'#\s*(.+)'

# 格式化日期为两位数
def format_date(year, month, day):
    return f"{int(year):04}年{int(month):02}月{int(day):02}日"

# 用于跟踪标签计数
tag_count = {}

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        file_path = os.path.join(folder_path, filename)

        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # 查找日期
            date_match = re.search(date_pattern, content)
            if date_match:
                year, month, day = date_match.groups()
                formatted_date = format_date(year, month, day)

                # 格式化新文件名
                new_filename = f"{formatted_date}.md"
                new_file_path = os.path.join(folder_path, new_filename)

                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"重命名: {filename} -> {new_filename}")
            else:
                # 查找标签
                tag_match = re.search(tag_pattern, content)
                if tag_match:
                    tag = tag_match.group(1).strip()
                    # 递增序号
                    if tag not in tag_count:
                        tag_count[tag] = 1
                    else:
                        tag_count[tag] += 1
                    new_filename = f"{tag}_{tag_count[tag]}.md"
                    new_file_path = os.path.join(folder_path, new_filename)

                    # 重命名文件
                    os.rename(file_path, new_file_path)
                    print(f"重命名: {filename} -> {new_filename}")
                else:
                    print(f"未找到日期或标签: {filename}")
