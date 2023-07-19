import mysql.connector
import json

def loaddata(json_file_path):
    # Open the JSON file and load the data
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    formatted_data = []
    for item in data:
        formatted_data.append((item['id'], item['name'], item['Memory'], item['Arithmetic'], item['Core'], item['Ethernet']))
    return formatted_data

# 连接到MySQL数据库
conn = mysql.connector.connect(
    user='root', 
    password='MySQLroot',
    host='localhost',
    database='Chipvatar_1')

# 创建游标对象
cursor = conn.cursor()

# 插入数据
insert_query = "INSERT INTO datatable (id, name, Memory, Arithmetic, Core, Ethernet) VALUES (%s, %s, %s, %s, %s, %s)"
data = loaddata("datatable_copy.json")
cursor.executemany(insert_query, data)

# 提交事务
conn.commit()

# 关闭游标和连接
cursor.close()
conn.close()
