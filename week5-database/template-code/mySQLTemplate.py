import pymysql.cursors
from sshtunnel import SSHTunnelForwarder
# Connect to the database
# port use 3306
with SSHTunnelForwarder(
        ssh_address_or_host=('192.168.56.102', 22),
        ssh_username = 'oscar',
        ssh_password = '0206',
        remote_bind_address = ('127.0.0.1', 3306),
        local_bind_address = ('0.0.0.0', 3306)) as server:
            connection = pymysql.connect('127.0.0.1',
                                         user='root',
                                         password='0206',
                                         db='test',
                                         port=server.local_bind_port,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)

            try:
                with connection.cursor() as cursor:
                    # Create a new record
                    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                    cursor.execute(sql, ('testbot123@python.org', 'not-very-secret2'))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
                connection.commit()

                with connection.cursor() as cursor:
                    # Read a single record
                    sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
                    cursor.execute(sql, ('testbot123@python.org',))
                    result = cursor.fetchone()
                    print(result)
            finally:
                connection.close()
