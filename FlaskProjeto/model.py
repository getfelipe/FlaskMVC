import sqlite3
import pandas as pd

class FilmesDB:

    def connect_db(self):
        try:
            self.conn = sqlite3.connect('/home/felipe/Downloads/filmes.db')
            self.cursor = self.conn.cursor()
        except Exception as ex:
            print(ex)
            self.conn.close()
        else:
            return self.cursor
        
    def execute_sql(self, command):

        return None
        
    def close_db(self):
        try:
            self.conn.close()
        except Exception as ex:
            print(ex)


    def convert_into_df(self):
        try:
            df = pd.read_sql_query('SELECT * FROM filmes', self.conn)
            return df
        except Exception as ex:
            print(ex)