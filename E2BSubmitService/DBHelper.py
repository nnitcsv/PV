import pymysql
from DBUtils.PooledDB import PooledDB

import DB_config as Config

class DBHelper:
    def __init__(self):
        #mysql数据库
        self.Pool=PooledDB(creator=pymysql, mincached=Config.DB_MIN_CACHED , maxcached=Config.DB_MAX_CACHED,maxshared=Config.DB_MAX_SHARED, maxconnections=Config.DB_MAX_CONNECYIONS,blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE,setsession=Config.DB_SET_SESSION,host=Config.DB_TEST_HOST , port=Config.DB_TEST_PORT ,user=Config.DB_TEST_USER , passwd=Config.DB_TEST_PASSWORD ,db=Config.DB_TEST_DBNAME , use_unicode=False, charset=Config.DB_CHARSET)
        
    def _Getconnect(self):
        self.conn=self.Pool.connection()
        cur=self.conn.cursor()
        if not cur:
            raise NameError+" 数据库连接不上"
        else:
            return cur
    #查询sql
    def ExecQuery(self,sql):
        cur=self._Getconnect()
        cur.execute(sql)
        relist=cur.fetchall()
        cur.close()
        self.conn.close()
        return print(relist)
 
    #非查询的sql,增删改
    def ExecNoQuery(self,sql):
        cur=self._Getconnect()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()
 
    #显示查询中的第一条记录
    def Showfirst(self,sql):
        cur = self._Getconnect()
        cur.execute(sql)
        resultfirst = cur.fetchone()
        cur.close()
        self.conn.close()
        return print(resultfirst)
 
    #显示查询出的所有结果
    def Showall(self, sql):
        cur = self._Getconnect()
        cur.execute(sql)
        resultall = cur.fetchall()
        cur.close()
        self.conn.close()
        return print(resultall)
 
#测试以上的方法
d = DBHelper()
d.Showall("select * from EMPLOYEE")
d.ExecNoQuery("update employee set last_name='YYY' where em_id=%s" % (12))