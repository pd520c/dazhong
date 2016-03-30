import requests
import pymysql
import time
import random
import re
from bs4 import BeautifulSoup

baseurl = 'http://www.dianping.com/search/keyword/'
sid = '1/'
keyword = '0_蟹/p'
aimstring = '?aid=2717353&cpt=2717353&tc=1'

def connDB():
    conn = pymysql.connect(host = 'localhost',
                           port = 3306,
                           user = 'root',
                           passwd = '',
                           db = 'dazhong',
                           charset = 'utf8',)
    cur = conn.cursor()
    return (conn,cur)

def connClose(conn,cur):
    cur.close();
    conn.close();

def getcurDate():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

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

def numfromString(s):
    return re.findall(r'(\w*[0-9]+)\w*',s)

def getsoup():
    string = ''
    for i in range(1,51):
        url = baseurl+sid+keyword+str(i)+aimstring
        string = string+list2string(BeautifulSoup(gethtml(url),"html5lib").find_all("div",attrs={"class":"pic"}))
    return string

def getshoplist():
    shoplist = [] 
    p = BeautifulSoup(getsoup(),"html5lib").find_all('a')
    for link in p:
        shoplist.append('http://www.dianping.com'+link.get('href'))
    return shoplist    

def insertshoplist():
    conn,cur=connDB()
    for shoplist in getshoplist():
        shopurl = str(shoplist)
        sta=cur.execute("INSERT INTO shopindex(shopurl) VALUES (%s)",(shopurl))
        if(sta==1):
            print('data insert successed')
            conn.commit()
        else:
            print('data insert failed')
    connClose(conn,cur)

def queryshoplist():
    conn,cur = connDB()
    shoplist = []
    sql = "SELECT shopurl FROM shopindex" 
    cur.execute(sql)
    for item in cur:
        shoplist.append(item[0])
    connClose(conn,cur)
    return shoplist

def getshopname(item):
    return str(BeautifulSoup(item,"html5lib").h1.contents[0])

def getaddress(item):
    tmp = list2string(BeautifulSoup(item,"html5lib").find_all("span",attrs={"class":"item","itemprop":"street-address"}))
    return str(BeautifulSoup(tmp,"html5lib").span['title'])

def getprice(item):
    tmp = list2string(BeautifulSoup(item,"html5lib").find_all("div",attrs={"class":"brief-info"})) 
    return numfromString(str(BeautifulSoup(tmp,"html5lib").find_all("span")[0]))

def getcomment(item):
    tmp = BeautifulSoup(item,"html5lib").find_all("span",attrs={"class":"sub-title"})
    return numfromString(str(tmp[1]))

def main():
    for tempurl in queryshoplist():
        item = gethtml(tempurl)
        try:
            shopname = getshopname(item)
            address = getaddress(item)
            price = getprice(item)
            comment = getcomment(item)
            print(tempurl,shopname,address,price,comment)
        except:
            print('error')


if __name__=="__main__":
    main()
