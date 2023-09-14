#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Project Achieve 
@File    ：headless.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2023/9/12 16:49 
'''
import time

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 配置无头浏览器选项
opts = Options()
# opts.add_argument('--headless')  # 启用无头模式
opts.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/116.0.0.0")
opts.add_argument("cookie = SSOLoginState=1649852314; _s_tentry=www.bing.com; Apache=6277092551915.035.1679674500926; SINAGLOBAL=6277092551915.035.1679674500926; ULV=1679674500928:1:1:1:6277092551915.035.1679674500926:; login_sid_t=bed207585882e01b9ca5d1f3ce5a29c3; cross_origin_proto=SSL; WBtopGlobal_register_version=2023062911; SUB=_2AkMThQJIf8NxqwFRmP4dzWnlaYhyygrEieKl2fOTJRMxHRl-yT9vqhI8tRB6OAUsp5_17BKYohGpioyOOo2wCqwXsQmL; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5a0GEujkJGjaNPgwO4ybxH; UOR=www.bing.com,weibo.com,www.bing.com")

# 创建无头浏览器
driver = webdriver.Chrome()

# 导航到要截图的页面
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
driver.get(url)

# 等待页面加载完成（你可以根据需要进行等待）
driver.implicitly_wait(10)  # 等待10秒

# 截取整个页面，包括滚动部分
time.sleep(2)
screenshot = driver.get_screenshot_as_file('screenshot.png')

# 关闭浏览器
driver.quit()
