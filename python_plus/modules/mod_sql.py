# sql 모듈 생성
# class 생성 Database
# class 생성이 될 때,  pymysql.connect 변수 생성, cursor 생성( __init__)
# init을 제외한 함수 3개 생성
import pymysql

class Database():
    def __init__(self):

        self._db = pymysql.connect(host = "darkpreist.iptime.org",
                                  user = "ubion",
                                  passwd = "1234",
                                  db = "ubion",
                                  port = 3306)

        self.cursor = self._db.cursor(pymysql.cursors.DictCursor)

    def execute(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)

    def executeAll(self, _sql, _values={}):
        self.cursor.execute(_sql, _values)
        self.result = self.cursor.fetchall()
        return self.result

    def commit(self):
        self._db.commit() # db가 변경된 경우 commit()