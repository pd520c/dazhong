from bs4 import BeautifulSoup
class GetShopinfo:
	"""docstring for GetShopinfo"""
	def __init__(self, item):
		self.item = item

	def getshopname(self):
		return str(BeautifulSoup(self.item,"html5lib").h1.contents[0])

	def getaddress(self):
	    tmp = list2string(BeautifulSoup(self.item,"html5lib").find_all("span",attrs={"class":"item","itemprop":"street-address"}))
	    return str(BeautifulSoup(tmp,"html5lib").span['title'])

	def getprice(self):
	    tmp = list2string(BeautifulSoup(self.item,"html5lib").find_all("div",attrs={"class":"brief-info"})) 
	    return numfromString(str(BeautifulSoup(tmp,"html5lib").find_all("span")[2]))

	def getcomment(self):
	    tmp = BeautifulSoup(self.item,"html5lib").find_all("span",attrs={"class":"sub-title"})
	    return numfromString(str(tmp[1]))

	def getarea(self):
	    tmp = list2string(BeautifulSoup(self.item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[1])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])

	def getlocation(self):
	    tmp = list2string(BeautifulSoup(self.item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[2])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])


	def getshoptype(self):
	    tmp = list2string(BeautifulSoup(self.item,"html5lib").find_all("div",attrs={"class":"breadcrumb"}))
	    tmp2 = str(BeautifulSoup(tmp,"html5lib").find_all("a")[3])
	    return str(BeautifulSoup(tmp2,"html5lib").a.contents[0])
			