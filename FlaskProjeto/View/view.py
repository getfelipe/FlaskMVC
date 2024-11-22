import dash_bootstrap_components as dbc
from dash import html, dash_table, Input, Output, State, dcc
from View.view_insert import insert_layout
from View.view_update import updt_layout
from View.view_delete import delete_layout
import pandas as pd

class View:
    def __init__(self, controller, app):
        self.__controller = controller
        self.__app = app  # Recebendo o app
        self.modal_insert = insert_layout
        self.modal_updt = updt_layout
        self.dataset = self.__controller.call_model_select_db()
        self.dataset = self.dataset.to_dict('records')

    def initialize_layout(self):
        # Definir o layout da aplicação
        self.__app.layout = dbc.Container(
            [
                self.modal_insert,
                self.modal_updt,
                delete_layout,
                dcc.Store(id='filmes_db', data=self.dataset),
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
                        dash_table.DataTable(
                            data=self.dataset,  # Convert dataset to list of dicts
                            columns=[{"name": i, "id": i} for i in pd.DataFrame(self.dataset).columns],  # Define column names
                            style_cell={'textAlign': 'center', 'padding': '5px'},
                            style_as_list_view=True,
                            style_table={'backgroundColor': 'white'},
                            page_size=20,
                            id='view_table'
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
        
        ##############################################

        @self.__app.callback(
            Output("updt-modal", "is_open"),
            Output('dropdown-filmes', 'options'),
            [Input("updt", "n_clicks"), Input("updt-close", "n_clicks")],
            [State("updt-modal", "is_open"), State("filmes_db", 'data')],
        )
        def load_dropdown_update(n1, n2, is_open, dataset):
            if n1 or n2:
                if not dataset:
                    print("Dataset is empty, returning default.")
                    return is_open, []
                
                else:
                    df = pd.DataFrame(dataset)
                    options = [{"label": filme, "value": filme} for filme in df["titulo"]]
                    return not is_open, options
            else:
                return is_open, []
            
        #########################################
            
        @self.__app.callback(
            Output("delete-modal", "is_open"),
            Output('dropdown-delete-filmes', 'options'),
            [Input("delete", "n_clicks"), Input("delete-close", "n_clicks")],
            [State("delete-modal", "is_open"), State('filmes_db', 'data')],
        )
        def load_dropdown_delete(n1, n2, is_open, dataset):
            if n1 or n2:
                if not dataset:
                    print("Dataset is empty, returning default.")
                    return is_open, []
                
                else:
                    df = pd.DataFrame(dataset)
                    options = [{"label": filme, "value": filme} for filme in df["titulo"]]
                    return not is_open, options
            else:
                return is_open, []
            

        ###################################################

        @self.__app.callback(
            Output('filmes_db', 'data'),
            Output('view_table', 'data'),
            Input('select', 'n_clicks')
        )

        def select_db(n_clicks):
            dataset = self.__controller.call_model_select_db()
            if not dataset.empty:
                dataset = dataset.to_dict('records')
                return dataset, dataset
            else:
                return {}, {}
            

        @self.__app.callback(
            [Output('alert-save-fail', 'is_open'), 
            Output('alert-save-success', 'is_open')],
            Input('insert-sql', 'n_clicks'),
            [State('title', 'value'), State('duration', 'value'), 
            State('genre', 'value'), State('diretor', 'value'), 
            State('rate', 'value')]
        )
        def insert_sql(n_clicks, title, duration, genre, diretor, rate):
            if n_clicks:  # If button is clicked
                if all([title, duration, genre, diretor, rate]):
                    command_sql = f'''
                    INSERT INTO filmes (titulo, duracao, diretor, avaliacao, genero) 
                    VALUES ("{title}", "{duration}", "{diretor}", "{rate}", "{genre}")
                    '''
                    validate = self.__controller.call_execute_sql(command_sql)
                    if validate:
                        return [False, True]  # Success: Hide fail alert, show success alert
                return [True, False]  # Fail: Show fail alert, hide success alert
            return [False, False]  # Default: No alerts, no data

        
        @self.__app.callback(
            [Output('alert-save-updt-success', 'is_open'), Output('alert-updt-fail', 'is_open')],
            Input('updt-sql', 'n_clicks'),
            [State('dropdown-filmes', 'value'), State('updt-duration', 'value'), State('updt-diretor', 'value'), State('updt-genre', 'value'), State('updt-rate', 'value')]
        )
        def update_sql(n_clicks, title, duration, diretor, genre, rate):
            dict_updt = {
                'duracao': duration,
                'diretor': diretor,
                'genero': genre,
                'avaliacao': rate
            }
            if n_clicks:
                if title and any([duration, diretor, genre, rate]):
                    filled_keys = [(key, value) for key, value in dict_updt.items() if value]
                    print(filled_keys) 

                    for key_value in filled_keys:
                        updt_sql = f'''
                            UPDATE filmes
                            SET {key_value[0]} = "{key_value[1]}"
                            WHERE titulo = "{title}";
                        '''
                        validate = self.__controller.call_execute_sql(updt_sql)
                        if not validate:
                            message = 'Algo deu errado'
                            return [False, True]


                    return [True, False]
                
                else:
                    return [False, True]
            else:
                return [False, False]
            

        @self.__app.callback(
            [Output('alert-save-delete-success', 'is_open'), Output('alert-delete-fail', 'is_open')],
            Input('delete-sql', 'n_clicks'),
            State('dropdown-delete-filmes', 'value')
        )
        def delete_sql(n_clicks, title):
            if n_clicks:
                if title:
                    delete_sql = f'''
                        DELETE FROM filmes WHERE titulo = "{title}"
                    '''
                    validate = self.__controller.call_execute_sql(delete_sql)

                    if not validate:
                        message = ''
                        return [False, True]
                    
                    else:
                        return [True, False]


                else:
                    return [False, True]
            
            else:
                return [False, False]

    
                    

                
            
            
            



