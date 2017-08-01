# -*- coding: UTF-8 -*-
# 显示等待
#
# 指定一个等待条件，并且指定一个最长等待时间，
# 会在这个时间内进行判断是否满足等待条件，如果成立就会立即返回，
# 如果不成立，就会一直等待，直到等待你指定的最长等待时间，如果还是不满足，
# 就会抛出异常，如果满足了就会正常返回

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)
