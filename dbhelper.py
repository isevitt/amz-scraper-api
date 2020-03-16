import pymysql
import dbconfig
import sys

class DBHelper:
    def connect(self):
        return pymysql.connect(host=dbconfig.host,
                               user=dbconfig.USERNAME,
                               passwd=dbconfig.PASS,
                               db=dbconfig.database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = f"INSERT INTO heroku_08d3aef4493ede4.scraping_requests (merchant_id) VALUES (%s)"
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                connection.commit()
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = "DELETE FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()