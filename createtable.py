
import mysql.connector

# 创建连接
conn = mysql.connector.connect(
    user='root', 
    password='MySQLroot',
    host='localhost',
    database='Chipvatar_1')

# 创建游标对象
cursor = conn.cursor()


# 定义创建数据表的SQL语句
sql = """
    CREATE TABLE datatable (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(255),
        Memory INT,
        Arithmetic INT,
        Core INT,
        Ethernet INT
    )
"""

# 执行SQL语句
cursor.execute(sql)

# 提交更改
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()

