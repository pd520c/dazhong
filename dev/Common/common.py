class CommonFun:		
	'''
	获取当天日期
	'''
	def GetcurDate(self):
		import time
		return time.strftime('%Y-%m-%d',time.localtime(time.time()))

	'''
	通过URL打开网页内容
	'''
	def Gethtml(self,url):
		import requests
		ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
		response = requests.get(url,headers = ua)
		return response.text

	
	
	def Tomd5(self,item):
		import hashlib
		m = hashlib.md5(item.encode('utf8'))  
		return m.hexdigest()


		'''
	list转字符串,返回值为string
	'''
	def list2string(self,l):
	    string = ''
	    if isinstance(l,list) == True:
	        for item in l:
	            string = string + str(item)
	    return string

	'''
	从字符串中找出数字，返回值为int
	'''
	def numfromString(self,s):
		import re
		return int(re.findall(r'(\w*[0-9]+)\w*',s)[0])


