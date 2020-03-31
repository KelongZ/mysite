from impala.dbapi import connect
from impala.util import as_pandas

class impala():
    def __init__(self, host, port):
        try:
            self.conn = connect(host=host, port=port)
        except:
            error_msg = 'impala connect error: Cannot connect to server!'
            print(error_msg)
        self.cur = self.conn.cursor()

    def exec_sql_output_df(self,sql):
        try:
            self.cur.execute(sql)
            return as_pandas(self.cur)
        except Exception as e:
            print(e)

# impala1 = impala('118.31.173.39',25001)
# table = 'flink_test'
# sql = 'SELECT * from' + ' ' + table
# df_data = impala1.exec_sql_output_df(sql)
# print(df_data)


# conn = connect(host='118.31.173.39', port=25001)
# cur = conn.cursor()
# cur.execute('SHOW TABLES;')
# #cur.execute('SELECT * from flink_test2;')
# df = as_pandas(cur)
# print(df)

# cur.execute('SELECT * from flink_test;')
# columns = [datum[0] for datum in cur.description]
# results = cur.fetchall()
#
# print(columns)
# print(results)

