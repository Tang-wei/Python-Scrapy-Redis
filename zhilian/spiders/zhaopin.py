# -*- coding: utf-8 -*-
import scrapy
import json
import re
import hashlib
from zhilian.items import ZhilianItem
from scrapy_redis.spiders import RedisSpider
from hhh import data

class ZhaopinSpider(RedisSpider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    redis_key = 'zhaopin:start_urls'
    #start_urls = ['http://http://sou.zhaopin.com/']
    headers ={
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    }
    #请求列表页
    #def start_requests(self):
    def parse(self,response):
        lists1 = ['210500', '160400', '160000', '160500', '160200', '300100', '160100', '160600', '180000', '180100', '300500','300900', '140000', '140100', '140200', '200300', '200302', '201400', '201300', '300300', '120400', '120200','170500', '170000', '300700', '201100', '120800', '121000', '129900', '121100', '121200', '210600', '120700','121300', '121500', '300000', '150000', '301100', '121400', '200600', '200800', '210300', '200700', '130000','120500', '130100', '201200', '200100', '120600', '100000', '100100', '990000']
        lists = ['530', '538', '763', '765', '531', '736', '854', '801', '600', '613', '599', '635', '702', '703', '653', '639','636', '654', '551', '719', '749', '681', '682', '622', '565', '664', '773','561','562','563', '916', '548', '546', '556', '552', '535', '536', '539', '544', '540', '549','541', '532', '533', '534', '537', '542', '543', '545', '547', '550', '553', '554', '555', '557', '558', '559','560']
        start_url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=%s&sj=%s&in=%s&jl=%s&p=%d'

        for key,zhi in data.items():
            for li in lists1:
                for value in zhi:
                    for pd in lists:
                        for ye in range(1,2):
                            fullurl = start_url % (key,value,li,pd,ye)
                            yield scrapy.Request(url=fullurl,callback=self.parse_list,headers=self.headers)
    #解析列表页 URL 进入详情页
    def parse_list(self,response):
        #print response.body
        url_list = []
        url = response.xpath('//td[@class="zwmc"]//a/@href')
        for p_url in url:
            l_url = str(p_url)[54:-2]
            #print l_url,type(l_url)
            url_list.append(l_url)
        #定义详情页url
        for x_url in url_list:
            if str.endswith(x_url,'.d'):
                pass
            elif str.endswith(x_url,'.') == False:
                n_url = x_url + '.htm'
                #print x_url
            else:
                n_url = x_url + 'htm'
                #print n_url
                # priority 设置请求在队里的优先级
                yield scrapy.Request(url=n_url,callback=self.parse_xiangqin, headers=self.headers,priority=1)

    #解析详情页
    def parse_xiangqin(self,response):

        item = ZhilianItem()
        #公司名称
        company = response.xpath('//h2//a[@target="_blank"]/text()').extract()[0]
        #薪水
        pay = response.xpath('//ul[@class="terminal-ul clearfix"]//strong/text()').extract()[0]
        #工作地点
        site = response.xpath('//ul[@class="terminal-ul clearfix"]//strong//a/text()').extract()[0]
        #发布时间
        times = response.xpath('//ul[@class="terminal-ul clearfix"]//strong//span/text()').extract()[0]
        #职位名
        gangwei = response.xpath('//ul[@class="terminal-ul clearfix"]//strong//a/text()').extract()[1]
        #url
        url = response.url
        #岗位职责
        miaoshu = response.xpath('.//div[@class="tab-inner-cont"]/p/text() | .//div[@class="tab-inner-cont"]//span/text() | .//div[@class="tab-inner-cont"]//div/text()').extract()
        num = 0
        while num <len(miaoshu):
            miaoshu[0] += miaoshu[num].strip()
            num += 1



        #print miaoshu[0]
        #print company,pay,site,times,gangwei,miaoshu
        item['company'] = company
        item['pay'] = pay
        item['site'] = site
        item['times'] = times
        item['gangwei'] = gangwei
        item['url'] = self.md5(url)
        if miaoshu:
            item['miaoshu'] = miaoshu[0]
        else:
            item['miaoshu'] = ''
        print '生成item'
        yield item
    #md5加密url
    def md5(self,data):
        m = hashlib.md5()
        m.update(data)
        return m.hexdigest()



