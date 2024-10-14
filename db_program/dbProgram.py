import pymysql

#MySql Configurations:
db_config ={
    'host' : 'localhost',
    'user' : 'root', #root
    'password' : 'root', #cdacacts
    'db' : 'sampledb'
}

connection = pymysql.connect(**db_config)
cursur = connection.cursor()

//root , cdacacts

try:
    sql_statement = "SELECT * FROM userinfo"



