class CommonFun():
	"""docstring for CommonFun"""
	def __init__(self, arg):
		self.arg = arg
		
	'''
	获取当天日期
	'''
	def GetcurDate():
		import time
	    return time.strftime('%Y-%m-%d',time.localtime(time.time()))

	'''
	通过URL打开网页内容
	'''
	def Gethtml(url):
		import requests
	    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}
	    response = requests.get(url,headers = ua)
	    return response.text

	'''
	list转字符串
	'''
	def List2String(l):
	    string = ''
	    if isinstance(l,list) == True:
	        for item in l:
	            string = string + str(item)
	    return string

	def Tomd5(item):
		import hashlib
	    m = hashlib.md5(item.encode('utf8'))  
	    return m.hexdigest()

	'''
	从字符串中找出数字
	'''
	def NumfromString(s):
		import re
	    return int(re.findall(r'(\w*[0-9]+)\w*',s)[0])