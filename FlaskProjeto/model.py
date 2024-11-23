import sqlite3
import pandas as pd

# Usar a variável de ambiente
file_path_db = 'Coloque aqui o caminho da base de dados filmes.db'
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
            self.cursor.execute(command)
            self.conn.commit()
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