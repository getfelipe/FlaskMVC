from model import FilmesDB
from View.view import View

class Controller:
    def __init__(self, app):
        self.__model = FilmesDB()
        # self.__model.connect_db()
        # self.df = self.__model.select_db()
        # self.__model.close_db()

        # Passando o app para a View
        self.__view = View(self, app)
        self.__view.initialize_layout()  # Inicializando o layout da View

    
    def call_model_select_db(self):
        self.__model.connect_db()
        df = self.__model.select_db()
        self.__model.close_db()
        return df
    
    def call_execute_sql(self, command):
        self.__model.connect_db()
        validate = self.__model.execute_sql(command)
        self.__model.close_db()
        return validate