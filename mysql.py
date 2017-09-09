import MySQLdb

conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user = 'root', passwd = 'liulong', db = 'test', charset = 'utf8')
cursor = conn.cursor()

sql_insert = "insert into account(id, name, money) values(7, '9666', 999)"
sql_update = "update account set name = 'name3' where id=3"
sql_delete = "delete from account where id < 3"

try:
	cursor.execute(sql_insert)
	print cursor.rowcount
	cursor.execute(sql_update)
	print cursor.rowcount
	cursor.execute(sql_delete)
	print cursor.rowcount
except Exception as e:
	print e
	conn.rollback()

conn.commit()
cursor.close()
conn.close()