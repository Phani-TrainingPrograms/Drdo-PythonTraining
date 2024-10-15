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

    def get_user_by_id(self, id):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM USERINFO WHERE id = %s"
                cursor.execute(query, id)
                selected_user = cursor.fetchone()
        except Exception as ex:
            print("Exception : ", ex)
        else:
                return selected_user
        finally:
                self.disconnect()

    def add_user(self, name, pwd, email):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                query = (f"INSERT INTO USERINFO (username, password, emailaddress) values (%s, %s, %s)")
                cursor.execute(query, (name, pwd, email))
                self.connection.commit()
        except Exception as ex:
            print("Exception while inserting: ", ex)
        finally:
            self.disconnect()

    def update_user(self, id, name, pwd, email):
        try:
            self.connect();
            with self.connection.cursor() as cursur:
                query = (f"UPDATE USERINFO SET username = %s, password = %s , emailaddress = %s "
                         f"where id = %s")
                cursur.execute(query, (name, pwd, email, id))
                self.connection.commit()
        except Exception as ex:
            print(f"Exception: {ex}")
        finally:
            self.disconnect()