# -*- coding: UTF-8 -*-

# 这里的异常比较复杂，官网的参考地址：
# http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions
# 这里只进行简单的演示，查找一个不存在的元素

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()