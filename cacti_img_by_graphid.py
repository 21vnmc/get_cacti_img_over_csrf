#!/usr/bin/env python
# encoding: utf-8
# @author  : jasonyoung
'''
@file cacti_get.py
@time 2019/11/21 10:38
@desc
'''
import sys
import time
import requests
from bs4 import BeautifulSoup

def login(graph_id):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    ssion = requests.session() #session
    #get csrf info
    html = ssion.get("http://xxx.xxx.xxx.xxx/cacti/index.php",headers=headers).content
    soup = BeautifulSoup(html,"lxml")
    _xsrf = soup.find('input', attrs={"name": "__csrf_magic"}).get("value")
    # print(_xsrf)
    formdata = {
        "login_username": "your username",
        "login_password": "your password",
        "action":"login",
        "__csrf_magic": _xsrf
    }
    # get your logined session
    rzt = ssion.post("http://xxx.xxx.xxx.xxx/cacti/index.php", data=formdata, headers=headers)
    # make your img url by graphid
    url = "http://xxx.xxx.xxx.xxx/cacti/graph_image.php?view_type=tree&local_graph_id={}&rra_id=0&graph_height=144&graph_width=600".format(graph_id)
    html = ssion.get(url=url, headers=headers).content
    print(html.decode())
    
    #write to file
    filename = "{}.png".format(graph_id)
    f = open(filename, "wb")
    f.write(html)
    f.close()
    ssion.close()

if __name__ == '__main__':
    graph_id = sys.argv[1]
    login(graph_id) #file pic