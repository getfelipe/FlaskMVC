import sqlite3
import pandas as pd
from dotenv import load_dotenv
import os

# Usar a variável de ambiente
load_dotenv()
file_path_db = os.getenv("FILE_PATH_DB_FILMES")
print(file_path_db)
class FilmesDB:

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(file_path_db)
            self.cursor = self.conn.cursor()
        except Exception as ex:
            print(ex)
            self.cursor.close()
            self.conn.close()
        else:
            return self.cursor
        
    def execute_sql(self, command):
        try:
            print(command)
            self.cursor.execute(command)
            self.conn.commit()
            print('Executado com sucesso')
            return True
        except Exception as ex:
            print('Erro execute: ', ex)
            return False
        
    def close_db(self):
        try:
            self.cursor.close()
            self.conn.close()
        except Exception as ex:
            print(ex)


    def select_db(self):
        try:
            df = pd.read_sql_query('SELECT * FROM filmes', self.conn)
            return df
        except Exception as ex:
            print('Erro select_db: ', ex)