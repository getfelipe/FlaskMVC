import dash_bootstrap_components as dbc
from dash import html, dash_table, Input, Output, State
from View.alerts import layout_danger, layout_success

insert_layout = html.Div(
            [
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Adicionar filme")),
                        layout_danger,
                        layout_success,
                        dbc.ModalBody([
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id="title", placeholder="Nome do Filme", type="text"),
                                ]),
                                dbc.Col([
                                    dbc.Input(id='duration', placeholder='Duração do Filme', type='text'),
                                ]),
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='diretor', placeholder='Nome do diretor', type='text',),
                                ])
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='rate', placeholder='Sua avaliação', type='text'),
                                ]),
                                dbc.Col([
                                    dbc.Input(id='genre', placeholder='Gênero', type='text'),
                                ])
                            ])
                            
                            
                        ]),
                        dbc.ModalFooter(
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        "Adicionar", id='insert-sql', className='ms-auto',
                                    )
                                ]),
                                dbc.Col([
                                    dbc.Button(
                                        "Close", id="close", className="ms-auto", n_clicks=0
                                    )
                                ])
                            ])

                        ),
                    ],
                    id="add-modal",
                    is_open=False,
                ),
            ]
        )