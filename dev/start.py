from DataBase.Mysql import MysqlAction
from Common.common import CommonFun
from Paser.paser import GetShopinfo
from bs4 import BeautifulSoup
"""数据库实例化"""
db = MysqlAction('127.0.0.1',3306,'root','','dazhong','utf8')
"""常用类实例化"""
com = CommonFun()
"""startURL"""
baseURL = 'http://www.dianping.com'
startURL = '/search/category/1/10'

def getlist():
	shoplist = []
	content = com.Gethtml(baseURL+startURL)
	p = BeautifulSoup(content,"html5lib").find_all("div",attrs={"class":"pic"})
	l = BeautifulSoup(com.list2string(p),"html5lib").find_all('a')
	for link in l:
		shoplist.append(baseURL+link.get('href'))
	return shoplist

def getsoup():
	content = com.Gethtml(baseURL+startURL)
	p = BeautifulSoup(content,"html5lib").find_all("a",attrs={"class":"next"})
	return p

print(getsoup())


	


