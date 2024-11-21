import dash
import dash_bootstrap_components as dbc
from dash import html

def create_app():
    # Inicializar a aplicação Dash
    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

    # Importar o Controller depois de criar o app
    from controller import Controller

    # Criar e inicializar o Controller, que já configura a View e o layout
    controller = Controller(app)

    return app

# Criar o app
app = create_app()

# Iniciar o servidor da aplicação
if __name__ == "__main__":
    app.run_server(debug=True)
