import mysql.connector

# 连接到MySQL数据库
conn = mysql.connector.connect(
    user='root', 
    password='MySQLroot',
    host='localhost',
    database='Chipvatar_1')

# 创建游标对象
cursor = conn.cursor()

# 获取数据表的列信息
cursor.execute("DESCRIBE datatable")
columns = [col[0] for col in cursor.fetchall()]

# 执行SQL查询语句
sql = "SELECT * FROM datatable"
cursor.execute(sql)

# 获取查询结果
rows = cursor.fetchall()

# 打印列名
print(columns)

# 遍历结果并打印数据
for row in rows:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
