import logging
import pymysql

class Connection:
    conn = None


    def opening_connection(self):
        try:
            if self.conn == None:
                self.conn = pymysql.connect("127.0.0.1",'root','','watu')
        except pymysql.MySQLError as e:
            pass
        finally:
            logging.INFO(e)

    def run_query(self,query):
        try:
            self.opening_connection()
            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                if "select" in query.lower():
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return  result
                else:
                    cursor.execute(query)
                    self.conn.commit()
                    affectedrow = cursor.rowcount
                    return f"{affectedrow} number of row affected!!"

        except pymysql.MySQLError as e:
            logging.INFO(e)
        finally:
            if self.conn:
                self.conn.close()
                self.conn = None
                logging.INFO("Connection is closed!!")

