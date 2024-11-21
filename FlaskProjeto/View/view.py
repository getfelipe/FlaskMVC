import dash_bootstrap_components as dbc
from dash import html, dash_table, Input, Output, State
from View.view_insert import insert_layout
from View.view_update import updt_layout
from View.view_delete import *


class View:
    def __init__(self, controller, app):
        self.__controller = controller
        self.__app = app  # Recebendo o app
        self.modal_insert = insert_layout
        self.modal_updt = updt_layout

    def initialize_layout(self):
        # Definir o layout da aplicação
        self.__app.layout = dbc.Container(
            [
                self.modal_insert,
                self.modal_updt,
                html.H1('Meus Filmes'),
                html.Hr(),
                dbc.Row([
                    dbc.Col([
                        dbc.Button('Adicionar filme', color='primary', className='me-1', id='add'),
                    ]),
                    dbc.Col([
                        dbc.Button('Atualizar filme', color='primary', className='me-1', id='updt'),
                    ]),
                    dbc.Col([
                        dbc.Button('Visualizar filme', color='secondary', className='me-1', id='select'),
                    ]),
                    dbc.Col([
                        dbc.Button('Deletar filme', color='danger', className='me-1', id='delete'),
                    ])
                ], style={'margin-top': '12px', 'margin-bottom': '7px'}),

                dbc.Row([
                    dbc.Col([
                        dash_table.DataTable(self.__controller.df.to_dict('records'), 
                                             [{"name": i, "id": i} for i in self.__controller.df.columns],
                                            style_cell={'textAlign': 'center', 'padding': '5px'},
                                            style_as_list_view=True,
                                            style_table={'backgroundColor': 'white'},
                                            page_size=20,
                                            
                                            )
                    ], )
                ])
            ],
            fluid=True,  # Usando layout fluido
        )

        @self.__app.callback(
            Output("add-modal", "is_open"),
            [Input("add", "n_clicks"), Input("close", "n_clicks")],
            [State("add-modal", "is_open")],
        )
        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open
        

        @self.__app.callback(
            Output("updt-modal", "is_open"),
            Output('dropdown-filmes', 'options'),
            [Input("updt", "n_clicks"), Input("close", "n_clicks")],
            [State("updt-modal", "is_open")],
        )
        def load_dropdown(n1, n2, is_open):
            if n1 or n2:
                options = [{"label": filme, "value": filme} for filme in self.__controller.df["titulo"]]
                return not is_open, options
            else:
                return is_open, []
