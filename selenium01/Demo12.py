# -*- coding: UTF-8 -*-
# 隐式等待
# 到了一定的时间发现元素还没有加载，则继续等待我们指定的时间，
# 如果超过了我们指定的时间还没有加载就会抛出异常，
# 如果没有需要等待的时候就已经加载完毕就会立即执行

from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)