from bs4 import BeautifulSoup
class GetShopinfo():
	"""docstring for GetShopinfo"""
	def __init__(self, arg):
		self.arg = arg

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

	def getarea(item):
	    tmp = list2string(BeautifulSoup(item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[1])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])

	def getlocation(item):
	    tmp = list2string(BeautifulSoup(item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[2])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])


	def getshoptype(item):
	    tmp = list2string(BeautifulSoup(item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[3])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])
			