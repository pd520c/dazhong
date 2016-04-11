import datetime
from sqlalchemy import *
from sqlalchemy import distinct, func
from sqlalchemy.sql import *
from sqlalchemy.orm import *
from sqlalchemy.databases import mysql
mysql_engine = create_engine('mysql+pymysql://root:@localhost:3306/dazhong?charset=utf8',
                             encoding = "utf-8",echo =True)
metadata = MetaData()
Session=sessionmaker()
Session.configure(bind=mysql_engine)
session=Session()

shopindex_table = Table('shopindex', metadata,
                        Column('id', Integer, primary_key=True),
                        Column('shopurl',String(200)),
                        Column('hash',String(300)),
                        mysql_engine = 'InnoDB')

shopinfo_table = Table('shopinfo',metadata,
                       Column('id',Integer ,primary_key=True),
                       Column('name',String(50)),
                       Column('address',String(50)),
                       Column('area',String(50)),
                       Column('location',String(50)),
                       Column('shoptype',String(50)),
                       Column('price',Integer),
                       Column('comment',Integer),
                       Column('savedate',DateTime),
                       Column('hashkey', String(300)),
                       mysql_engine = 'InnoDB')

def install(): 
    metadata.create_all(mysql_engine)

install()

