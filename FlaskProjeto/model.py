import sqlite3
import pandas as pd
import os

# Carregar a variável de ambiente
file_path_db = os.getenv("FILE_PATH_DB_MOVEIS")
print(f"Usando o banco de dados em: {file_path_db}")

class FilmesDB:

    def connect_db(self):
        try:
            self.conn = sqlite3.connect(file_path_db)
            self.cursor = self.conn.cursor()
        except Exception as ex:
            print("Erro ao conectar ao banco de dados:", ex)
            self.conn = None
            self.cursor = None
        else:
            return self.cursor
        
    def execute_sql(self, command):
        try:
            if self.cursor:
                self.cursor.execute(command)
                self.conn.commit()
                return True
            else:
                print("Conexão não estabelecida.")
                return False
        except Exception as ex:
            print('Erro ao executar SQL: ', ex)
            return False
        
    def close_db(self):
        if self.cursor and self.conn:
            try:
                self.cursor.close()
                self.conn.close()
            except Exception as ex:
                print("Erro ao fechar conexão:", ex)

    def select_db(self):
        try:
            if self.conn:
                df = pd.read_sql_query('SELECT * FROM filmes', self.conn)
                return df
            else:
                print("Conexão não estabelecida.")
                return None
        except Exception as ex:
            print('Erro ao consultar o banco de dados: ', ex)
            return None
