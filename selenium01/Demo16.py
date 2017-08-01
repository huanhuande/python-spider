# -*- coding: UTF-8 -*-
# 选项卡管理
#
# 通过执行js命令实现新开选项卡window.open()
# 不同的选项卡是存在列表里browser.window_handles
# 通过browser.window_handles[0]就可以操作第一个选项卡

import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')