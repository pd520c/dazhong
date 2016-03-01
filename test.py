import requests
import pymysql
import time
import random
import subprocess
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

def getDom(url):
    cmd = 'phantomjs injectweb.js "%s"'%url
    print(cmd)
    stdout,stderr = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    print(stderr)
    return stdout

url = baseurl+sid+keyword+'1'+aimstring
soup = BeautifulSoup(gethtml(url),"html5lib")
top = soup.find(id="shop-all-list")
#print(top)
print(gethtml('http://www.dianping.com/shop/21049219'))
