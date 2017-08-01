# -*- coding: UTF-8 -*-
#beautiful爬取豆瓣Top250电影信息


import urllib3
import re
from bs4 import BeautifulSoup
import codecs


# 爬虫函数
def crawl(url):
    page = urllib3.urlopen(url)
    contents = page.read()
    soup = BeautifulSoup(contents, "html.parser")
    print
    u'豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数'
    infofile.write(u"豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数\r\n")
    print
    u'爬取信息如下:\n'
    for tag in soup.find_all(attrs={"class": "item"}):
        # print tag
        # 爬取序号
        num = tag.find('em').get_text()
        print
        num
        # 爬取电影名称
        name = tag.find(attrs={"class": "hd"}).a.get_text()
        name = name.replace('\n', ' ')
        print
        name
        infofile.write(num + " " + name + "\r\n")
        # 电影名称
        title = tag.find_all(attrs={"class": "title"})
        i = 0
        for n in title:
            text = n.get_text()
            text = text.replace('/', '')
            text = text.lstrip()
            if i == 0:
                print
                u'[中文标题]', text
                infofile.write(u"[中文标题]" + text + "\r\n")
            elif i == 1:
                print
                u'[英文标题]', text
                infofile.write(u"[英文标题]" + text + "\r\n")
            i = i + 1
        # 爬取评分和评论数
        info = tag.find(attrs={"class": "star"}).get_text()
        info = info.replace('\n', ' ')
        info = info.lstrip()
        print
        info
        mode = re.compile(r'\d+\.?\d*')
        print
        mode.findall(info)
        i = 0
        for n in mode.findall(info):
            if i == 0:
                print
                u'[分数]', n
                infofile.write(u"[分数]" + n + "\r\n")
            elif i == 1:
                print
                u'[评论]', n
                infofile.write(u"[评论]" + n + "\r\n")
            i = i + 1
        # 获取评语
        info = tag.find(attrs={"class": "inq"})
        if (info):  # 132部电影 [消失的爱人] 没有影评
            content = info.get_text()
            print
            u'[影评]', content
            infofile.write(u"[影评]" + content + "\r\n")
        print
        ''




# 主函数
if __name__ == '__main__':

    infofile = codecs.open("Result_Douban.txt", 'a', 'utf-8')
    url = 'http://movie.douban.com/top250?format=text'
    i = 0
    while i < 10:
        print
        u'页码', (i + 1)
        num = i * 25  # 每次显示25部 URL序号按25增加
        url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
        crawl(url)
        infofile.write("\r\n\r\n\r\n")
        i = i + 1
    infofile.close()
