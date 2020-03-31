import pymysql

class mysql():
    def __init__(self,host,username,password,database,port,charset):
        '''初始化数据库信息并创建数据库连接'''
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset
        self.conn = pymysql.connect(self.host,self.username,self.password,self.database,self.port,charset=self.charset)

    def insertDB(self,sql):
        ''' 插入数据库操作 '''
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cursor.close()

    def deleteDB(self,sql):
        ''' 操作数据库数据删除 '''
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cursor.close()

    def updateDB(self,sql):
        ''' 操作数据库数据更新 '''
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            self.cursor.close()

    def selectDB(self,sql):
        ''' 操作数据库数据查询,返回字典 '''
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()  # 返回所有记录列表
            return data
        except:
            print('Error: unable to fetch data')
        finally:
            self.cursor.close()

    def closeDb(self):
        ''' 数据库连接关闭 '''
        self.conn.close()

# mysqlDBconn = mysql('rm-bp12cfwxprq1e385f7o.mysql.rds.aliyuncs.com','dengtacj','Dengtacj2015','db_spider',3306,'utf8')
# print(mysqlDBconn.selectDB("SELECT * from h_road_detail where index_name in ('缅甸：GDP：现价：美元')"))
