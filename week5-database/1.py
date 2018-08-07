import csv
import pymysql.cursors
from sshtunnel import SSHTunnelForwarder

# ssh server setting
# server.start()
# server.stop()
server = SSHTunnelForwarder(
        ssh_address_or_host=('192.168.56.102', 22),
        ssh_username = 'oscar',
        ssh_password = '0206',
        remote_bind_address = ('127.0.0.1', 3306),
        local_bind_address = ('0.0.0.0', 3306)
        )
server.start()
# mysql connection setting
connection = pymysql.connect('127.0.0.1',
                             user='root',
                             password='0206',
                             db='HW1',
                             port=server.local_bind_port)

# # open csvfile
# studentList=[]
# with open('1.csv', newline='') as csvfile:
#     rows = csv.reader(csvfile)
#     rawData = []
#     for i in rows:
#         rawData.append(i)
#     table=[]
#     for i in rawData[0]:
#         table.append(i)
#     for i in range(1, 11):
#         temp = []
#         for index,data in enumerate(rawData[i]):
#             if index == 0 or index == 3 or index == 4 or index == 5:
#                 temp.append(int(data))
#             else:
#                 temp.append(data)
#         studentList.append(temp)
#     # print (table)
#     # print (studentList)
# # finish data process
try:
    # # 創立Table
    # with connection.cursor() as cursor:
    #     createTable = "CREATE TABLE Data (class int(2), studentId varchar(255), Name varchar(255), Chinese_Score int(3), Math_Score int(3), English_Score int(3)) ;"
    #     cursor.execute(createTable)
    #     print('Finish create table')
    #
    # connection.commit()
    #
    # # 添加資料
    # with connection.cursor() as cursor:
    #     # createTable = "CREATE TABLE users(id int, name varchar(32), password varchar(32))"
    #     insertValue = "INSERT INTO Data (class, studentId, Name, Chinese_Score, Math_Score, English_Score) VALUES (%s, %s, %s, %s, %s, %s)"
    #     for i in studentList:
    #         value = (i[0], i[1], i[2], i[3], i[4], i[5])
    #         # print(value)
    #         cursor.execute(insertValue, value)
    # connection.commit()

    # # 取資料庫全部值
    # with connection.cursor() as cursor:
    #     print('Show Table:')
    #     cursor.execute("SHOW TABLES")
    #     tables = cursor.fetchall()
    #     print(tables)
    #     print('Show Data:')
    #     cursor.execute("SELECT * FROM Data")
    #     data = cursor.fetchall()
    #     print(data)

    # 第一題
    # with connection.cursor() as cursor:
    #     print('都不及格的有:')
    #     cursor.execute("select * from Data where Math_Score < 60 and English_Score < 60 and Chinese_Score < 60")
    #     data = cursor.fetchall()
    #     for i in data:
    #         print(i[2])
    # 第二題
    with connection.cursor() as cursor:
        cursor.execute("SELECT count( * ) AS count FROM Data GROUP BY class ORDER BY class ASC LIMIT 3 ")
        data = cursor.fetchall()
        print(data)

finally:
    connection.close()
    server.stop()
print('----Server End----')
#
