import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'Nacho1127!',
    'host': '127.0.0.1',
    'database': 'sakila',
    'raise_on_warnings': True,
}


class Data_Base_MySQL():
    def __init__(self, user, password, host):
        try:
            self.cnx = mysql.connect(**config)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.cnx.close()

    def insert_table(self):
        cursor = self.cnx.cursor()

    def __del__(self):
        self.cnx.close()
