# coding:utf-8
import sys
import requests
import datetime
import time
import json
from bs4 import BeautifulSoup


class IpAddressQuery():

    def getCurrentIp(self):
        url = 'https://2021.ip138.com'

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        response.encoding = response.apparent_encoding

        if(response.status_code != 200):
            return ''

        txt = response.text

        soup = BeautifulSoup(txt, "html.parser")

        p = soup('p')

        if p is not None and len(p) > 0:
            return p[0].text
        
        return '没有查到ip'
