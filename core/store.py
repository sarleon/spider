#coding:utf-8
from sqlalchemy import create_engine,MetaData



class Store:

    def __init__(self,dbpath,tablename=None):
        self.dbpath = dbpath
        self.tablename = tablename or 'pages'
        try:
            engine = create_engine('sqlite:///'+dbpath, echo=True)  # 定义引擎
        except IOError as e:
            print e.message

        metadata = MetaData(engine)  # 绑定元信息


    def store_a_page(self,url,content,matchs):
        pass


