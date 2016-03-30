# -*- coding: utf-8 -*-
'''
抓取通过关键字搜索大众点评网店铺的结果
第三方库为pymysql，requests，BeautifulSoup
''' 
import requests
import pymysql
import time
import random
import re
from bs4 import BeautifulSoup

'''
四个全局变量
'''
baseurl = 'http://www.dianping.com/search/keyword/'
sid = '1/'
keyword = '0_蟹/p'
aimstring = '?aid=2717353&cpt=2717353&tc=1'

'''
数据库初始化
'''
def connDB():
    conn = pymysql.connect(host = 'localhost',
                           port = 3306,
                           user = 'root',
                           passwd = '',
                           db = 'dazhong',
                           charset = 'utf8',)
    cur = conn.cursor()
    return (conn,cur)
'''
数据库关闭
'''
def connClose(conn,cur):
    cur.close();
    conn.close();

'''
获取当天日期
'''
def getcurDate():
    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

'''
通过URL打开网页内容
'''
def gethtml(url):
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
    response = requests.get(url,headers = ua)
    return response.text

'''
list转字符串
'''
def list2string(l):
    string = ''
    if isinstance(l,list) == True:
        for item in l:
            string = string + str(item)
    return string

def md5(str):
    import hashlib
    m = hashlib.md5()  
    m.update(str)
    return m.hexdigest()

'''
从字符串中找出数字
'''
def numfromString(s):
    return int(re.findall(r'(\w*[0-9]+)\w*',s)[0])

def checkrepeat(item):
    conn,cur = connDB()
    sql = "SELECT hash FROM shopindex WHERE hash = %s" 
    df = cur.execute(sql,item)
    if df==0:
        return False
    else:
        return True

def checkdata(name,d):
    conn,cur = connDB()
    sql = "SELECT name,savedate FROM shopinfo WHERE name=%s AND savedate=%s"
    df = cur.execute(sql,(name,d))
    if df==0:
        return False
    else:
        return True

'''
getsoup()和getshoplist()获取店铺的URL列表
'''

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

'''
将店铺的URL列表插入数据库
'''
def insertshoplist():
    conn,cur=connDB()
    for shoplist in getshoplist():
        shopurl = str(shoplist)
        if checkrepeat(md5(shopurl))==False:
            sta=cur.execute("INSERT INTO shopindex(shopurl,hash) VALUES (%s,%s)",(shopurl,md5(shopurl)))
            if(sta==1):
                print('data insert successed')
                conn.commit()
            else:
                print('data insert failed')
        else:
            print('data repeat')
    connClose(conn,cur)

'''
从数据库里查询店铺URL
'''
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
    return numfromString(str(BeautifulSoup(tmp,"html5lib").find_all("span")[2]))

def getcomment(item):
    tmp = BeautifulSoup(item,"html5lib").find_all("span",attrs={"class":"sub-title"})
    return numfromString(str(tmp[1]))

'''
'''
def main():
    conn,cur=connDB()
    for tempurl in queryshoplist():
        item = gethtml(tempurl)
        shopname = getshopname(item)
        address = getaddress(item)
        price = getprice(item)
        comment = getcomment(item)
        d = getcurDate()
        if checkdata(shopname,d)==False:
            cur.execute("INSERT INTO shopinfo(name,address,price,comment,savedate) VALUES (%s,%s,%s,%s,%s)",(shopname,address,price,comment,d))
            conn.commit()
            print(tempurl,shopname,address,price,comment,d)
        else:
            print('date repeat')
    connClose(conn.cur)


if __name__=="__main__":
    insertshoplist()
    main()
