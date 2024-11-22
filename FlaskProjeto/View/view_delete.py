import dash_bootstrap_components as dbc
from dash import html, dash_table, Input, Output, State, dcc


delete_layout = html.Div(
            [
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Deletar filme")),
                        html.Div(
                            [
                                dbc.Alert(
                                    'Preencha o título correto do filme!',
                                    id='alert-delete-fail',
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
                                    'Deletado com sucesso!',
                                    id='alert-save-delete-success',
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
                                        id="dropdown-delete-filmes",
                                        placeholder="Selecione ou busque um filme...",
                                        options=[],
                                        searchable=True,  # Ativar busca
                                        style={"width": "100%"}  # Ajustar a largura do dropdown
                                    ),
                                ]),
                            ]),
                            html.Br(),
                        ]),
                        dbc.ModalFooter(
                            dbc.Row([
                                dbc.Col([
                                    dbc.Button(
                                        "Confirmar", id='delete-sql', className='ms-auto',
                                    )
                                ]),
                                dbc.Col([
                                    dbc.Button(
                                        "Close", id="delete-close", className="ms-auto", n_clicks=0
                                    )
                                ])
                            ])

                        ),
                    ],
                    id="delete-modal",
                    is_open=False,
                ),
            ]
        )