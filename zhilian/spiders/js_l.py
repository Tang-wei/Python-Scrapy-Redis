#coding:utf-8
from selenium import webdriver
import re

browser = webdriver.PhantomJS()
browser.get('http://sou.zhaopin.com/jobs/searchresult.ashx')
browser.find_element_by_id("buttonSelIndustry").click()

pattern = re.compile(r'for="c_buttonSelIndustry_(\d+)"')
industry = pattern.findall(browser.page_source.encode('utf-8'))
#print industry,len(industry)