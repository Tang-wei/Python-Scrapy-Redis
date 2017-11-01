from scrapy import cmdline
import os
os.chdir('zhilian/spiders')
cmdline.execute('scrapy runspider zhaopin.py'.split())