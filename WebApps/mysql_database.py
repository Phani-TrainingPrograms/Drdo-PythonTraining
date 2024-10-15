import pymysql

# Class that abstracts the MySQL code from UR Flask Application.
class MySqlDatabase:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = pymysql.connect(host = "localhost", user = "root",
                                              password="root", database="sampledb")
            print("Connected to the database")
        except Exception as ex:
            print("Exception: ", ex)

    def disconnect(self):
        if self.connection:
            self.connection.cursor().close()
            self.connection.close()
            print("Disconnected from the database")

    def get_all_users(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM USERINFO"
                cursor.execute(query)
                users = cursor.fetchall()
        except Exception as ex:
            print("Exception : ", ex)
        else:
                return users
        finally:
                self.disconnect()

    def add_user(self, name, pwd, email):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = (f"INSERT INTO USERINFO (username, password, emailaddress) values (%%s, "
                         f"%s, %s)")
                cursor.execute(query, {name, pwd, email})
                cursor.commit()
        except Exception as ex:
            print("Exception while inserting: ", ex)
        finally:
            self.disconnect()

