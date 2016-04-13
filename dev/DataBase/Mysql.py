import pymysql
class MysqlAction:
	"""docstring for MysqlAction"""
	def __init__(self, host, port, user, passwd, db, charset):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.charset = charset
		

	def connDB(self):
	    conn = pymysql.connect(host = self.host,
	                           port = self.port,
	                           user = self.user,
	                           passwd = self.passwd,
	                           db = self.db,
	                           charset = self.charset,)
	    cur = conn.cursor()
	    return (conn,cur)

	def connClose(self,conn,cur):
		cur.close()
		conn.close()

	def insert(self,sql,datatuple):
		conn,cur = self.connDB()
		cur.execute(sql,datatuple)
		conn.commit()

	def queryone(self,table,column,condition,item):
		conn,cur = self.connDB()
		sql = "SELECT " + column + " FROM " + table + " WHERE " + condition + "=%s" 
		df = cur.execute(sql,item)
		if df==0:
			return False
		else:
			return True

	def queryall(self,table):
		conn,cur = self.connDB()
		sql = "SELECT * FROM " + table 
		cur.execute(sql)
		return cur

	def querylist(self,table,column):
		conn,cur = self.connDB()
		result = []
		sql = "SELECT " + column + " FROM " + table 
		cur.execute(sql)
		for item in cur:
			result.append(item[0])
		self.connClose(conn,cur)
		return result

	def checkdata(self,name,d):
	    conn,cur = self.connDB()
	    sql = "SELECT name,savedate FROM shopinfo WHERE name=%s AND savedate=%s"
	    df = cur.execute(sql,(name,d))
	    if df==0:
	        return False
	    else:
	        return True	 

    	