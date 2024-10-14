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

def get_user_by_id(id):
    connection = pymysql.connect(**db_config)
    cursur = connection.cursor()
    try:
        cursur.execute(sql_select_by_id, id)
        user = cursur.fetchone()
    except Exception as ex:
        print("Exception while fetching single record: ", ex)
    else:
        return user
    finally:
        cursur.close()
        connection.close()


def add_user(name, pwd, email):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_insert, (name, pwd, email))
        connection.commit()
    except Exception as ex:
        print("Failed to insert: ", ex)
    finally:
        cursor.close()
        connection.close()

try:
    #todo: take inputs from the user and pass it as args to the add_user func
    add_user("Phaniraj", "test@123", "phanirajbn@gmail.com")
    users = get_all_users()
except:
    print("Error occured: ")
else:
    for user in users:
        print(f"{user[1]} with email: {user[3]} is identified as {user[0]}")
finally:
    print("End of the Application")

# user = get_user_by_id(1)
# print(user)
