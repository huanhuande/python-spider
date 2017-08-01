# -*- coding: UTF-8 -*-


from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('http://baicaowei.jd.com/')
    input = browser.find_element_by_id('key01')
    input.send_keys('')
    button = browser.find_element_by_class_name('button01')
    button.click()
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'jPage')))
    doc=pq(browser.page_source)
    m=doc('.jSearchListArea  .jSubObject  .jGoodsInfo  .jDesc')
    print(m)
finally:
    browser.close()