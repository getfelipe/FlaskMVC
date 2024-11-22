import dash_bootstrap_components as dbc
from dash import html, dash_table, Input, Output, State, dcc


updt_layout = html.Div(
            [
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Atualizar filme")),
                        html.Div(
                            [
                                dbc.Alert(
                                    'Preencha algum campo com o título correto do filme!',
                                    id='alert-updt-fail',
                                    is_open=False,
                                    dismissable=True,
                                    fade=True,
                                    color='danger'
                                )
                            ],
                        ),
                        html.Div(
                            [
                                dbc.Alert(
                                    'Atualizado com sucesso!',
                                    id='alert-save-updt-success',
                                    is_open=False,
                                    fade=True,
                                    dismissable=True,
                                    color='success'
                                )
                            ]
                        ),
                        dbc.ModalBody([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(
                                        id="dropdown-filmes",
                                        placeholder="Selecione ou busque um filme...",
                                        options=[],
                                        searchable=True,  # Ativar busca
                                        style={"width": "100%"}  # Ajustar a largura do dropdown
                                    ),
                                ]),
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='updt-duration', placeholder='Duração do Filme', type='text'),
                                ]),
                                dbc.Col([
                                    dbc.Input(id='updt-diretor', placeholder='Nome do diretor', type='text',),
                                ])
                            ]),
                            html.Br(),
                            dbc.Row([
                                dbc.Col([
                                    dbc.Input(id='updt-rate', placeholder='Sua avaliação', type='text'),
                                ]),
                                dbc.Col([
                                    dbc.Input(id='updt-genre', placeholder='Gênero', type='text'),
                                ])
                            ])
                            
                            
                        ]),
                        dbc.ModalFooter(
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        "Atualizar", id='updt-sql', className='ms-auto',
                                    )
                                ]),
                                dbc.Col([
                                    dbc.Button(
                                        "Close", id="updt-close", className="ms-auto", n_clicks=0
                                    )
                                ])
                            ])

                        ),
                    ],
                    id="updt-modal",
                    is_open=False,
                ),
            ]
        )