#-*- coding: utf-8 -*-
'''
Created on 2014-1-2

@author: Administrator
'''

import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        print imgurl
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x = x + 1        
   
html = getHtml("http://tieba.baidu.com/p/2460150866")
getImg(html)

