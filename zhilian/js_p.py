#coding:utf8
from selenium import webdriver
import time
import requests
from lxml import etree
import re

#def position_list():
browser = webdriver.PhantomJS()
browser.get('http://sou.zhaopin.com/jobs/searchresult.ashx')
time.sleep(1)
browser.find_element_by_id('buttonSelCity').click()

html = etree.HTML(browser.page_source)
position1 = html.xpath('//span/@onclick')
position = html.xpath('//td[@class="mOutItem"]//input/@value')
plist = []
for pos in position:
    plist.append(pos)
    print pos

for po in position1:
    pos = po.encode('utf-8')
    lists = re.compile(r'\d+')
    pos = lists.findall(pos)
    if pos != []:

        plist.append(str(pos)[2:5])

print plist,len(plist)






