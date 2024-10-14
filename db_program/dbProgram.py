import pymysql

#SQL statements:
sql_select_all ="SELECT * FROM USERINFO"
sql_select_by_id = "SELECT * FROM USERINFO WHERE id = %s"
sql_insert = "INSERT INTO USERINFO (username, password, emailaddress) values (%s, %s, %s)"
sql_update = "UPDATE USERINFO SET username = %s, emailaddress = %s, password = %s where id = %s"
sql_delete = "DELETE FROM USERINFO WHERE id = %s"


#MySql Configurations:
db_config ={
    'host' : 'localhost',
    'user' : 'root', #root
    'password' : 'root', #cdacacts
    'db' : 'sampledb'
}


#root , cdacacts
def get_all_users():
    connection = pymysql.connect(**db_config)
    cursur = connection.cursor()
    try:
        cursur.execute(sql_select_all)
        users = cursur.fetchall()
    except Exception as ex:
        print("Exception raised: ", ex)
    else:
        return users
    finally:
        cursur.close()
        connection.close()


users = get_all_users()
for user in users:
    print(f"{user[1]} with email: {user[3]} is identified as {user[0]}")
