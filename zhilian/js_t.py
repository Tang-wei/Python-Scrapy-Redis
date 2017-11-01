#coding:utf8
from selenium import webdriver
import time
import requests
from lxml import etree
import re

def position_list():
    browser = webdriver.PhantomJS()
    browser.get('http://sou.zhaopin.com/jobs/searchresult.ashx')
    time.sleep(1)
    browser.find_element_by_id('buttonSelJobType').click()

    html = etree.HTML(browser.page_source)
    position = html.xpath('//td[@class="blurItem"]/span/@onclick')
    plist = []
    for pos in position:
        pos = eval(pos.encode('utf-8')[62:-1])
        plist.append(pos[0])
    return plist
#def xmlx():
plist = ['4010200', '7001000', '7002000', '4000000', '4082000', '4084000', '7004000', '2060000', '5002000', '3010000', '201300', '2023405', '1050000', '160000', '160300', '160200', '160400', '200500', '200300', '5001000', '141000', '140000', '142000', '2071000', '2070000', '7006000', '200900', '4083000', '4010300', '4010400', '121100', '160100', '7003000', '7003100', '5003000', '7005000', '5004000', '121300', '120500', '2120000', '2100708', '2140000', '2090000', '2080000', '2120500', '5005000', '4040000', '201100', '2050000', '2051000', '6270000', '130000', '2023100', '100000', '200100', '5006000', '200700', '300100', '300200']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}
for p in plist:
    base_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=%s' % p
    response = requests.get(url=base_url,headers=headers)
    pattern = re.compile(r'sj=(\d+)')
    sp = pattern.findall(response.text.encode('utf-8'))
    position = {str(p):sp}
    print position
    #with open('tt.txt','w+') as f:

        #f.write()







