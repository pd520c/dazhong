import pymysql
class MysqlAction():
	"""docstring for MysqlAction"""
	def __init__(self, host, port, user, passwd, db, charset):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db
		self.charset = charset
		

	def connDB():
    conn = pymysql.connect(host = self.host,
                           port = self.passwd,
                           user = self.user,
                           passwd = self.passwd,
                           db = self.db,
                           charset = self.charset,)
    cur = conn.cursor()
    return (conn,cur)

	def connClose(conn,cur):
    cur.close()
    conn.close()