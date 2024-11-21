from model import FilmesDB
from View.view import View

class Controller:
    def __init__(self, app):
        self.__model = FilmesDB()
        self.__model.connect_db()
        self.df = self.__model.convert_into_df()

        # Passando o app para a View
        self.__view = View(self, app)
        self.__view.initialize_layout()  # Inicializando o layout da View
