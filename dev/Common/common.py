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
		m = hashlib.md5(item.encode('utf8'))  
		return m.hexdigest()

