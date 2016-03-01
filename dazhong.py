import requests
import pymysql
import time
import random
from bs4 import BeautifulSoup
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = '',
    db = 'dazhong',
    charset = 'utf8',
)
cur = conn.cursor()
baseurl = 'http://www.dianping.com/search/keyword/'
sid = '1/'
keyword = '0_蟹/p'
aimstring = '?aid=2717353&cpt=2717353&tc=1'

def gethtml(url):
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
    response = requests.get(url,headers = ua)
    return response.text

def list2string(l):
    string = ''
    if isinstance(l,list) == True:
        for item in l:
            string = string + str(item)
    return string

def getsoup():
    soup = ''
    for i in range(1,51):
        url = baseurl+sid+keyword+str(i)+aimstring
        soup = soup+ list2string(BeautifulSoup(gethtml(url),"html5lib").find_all("div",attrs={"class":"pic"}))
    return soup

print(getsoup())
