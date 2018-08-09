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
print('----Server Start----')
server.start()
# mysql connection setting
connection = pymysql.connect('127.0.0.1',
                             user='root',
                             password='0206',
                             db='HW2',
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
    with connection.cursor() as cursor:
        createTable = "CREATE TABLE STUDENT (StudentId varchar(255), Name varchar(255), YearOfEntrance int, Major varchar(255));"
        cursor.execute(createTable)
        print('Finish create table STUDENT...')
        createTable = "CREATE TABLE COURSE (CourseNo int, CourseTitle varchar(255), CreditHours int, Department varchar(255));"
        cursor.execute(createTable)
        print('Finish create table COURSE...')
        createTable = "CREATE TABLE CLASS (ClassId int, CourseNo int, Semester int, Year int, Instructor varchar(255));"
        cursor.execute(createTable)
        print('Finish create table CLASS...')
        createTable = "CREATE TABLE GRADE_REPORT (Student varchar(255), ClassId varchar(255), Grade int);"
        cursor.execute(createTable)
        print('Finish create table GRADE_REPORT...')

    connection.commit()
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

finally:
    connection.close()
    server.stop()
print('----Server End----')
