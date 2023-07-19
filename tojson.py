import mysql.connector
import pandas as pd

# 连接到MySQL数据库
conn = mysql.connector.connect(
    user='root', 
    password='MySQLroot',
    host='localhost',
    database='Chipvatar_1')

# 从数据库读取数据表
dataframe = pd.read_sql("SELECT * FROM datatable", conn)

# 将数据表转换为JSON格式
json_data = dataframe.to_json(orient="records")

# 将JSON数据写入文件
with open("datatable.json", "w") as file:
    file.write(json_data)

# 关闭数据库连接
conn.close()