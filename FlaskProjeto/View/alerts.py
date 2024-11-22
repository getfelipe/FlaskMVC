
from dash import html
import dash_bootstrap_components as dbc

layout_danger = html.Div(
    [
        dbc.Alert(
            'Preencha todos os campos!',
            id='alert-save-fail',
            is_open=False,
            dismissable=True,
            fade=True,
            color='danger'
        )
    ],
)


layout_success = html.Div(
    [
        dbc.Alert(
            'Adicionado com sucesso!',
            id='alert-save-success',
            is_open=False,
            fade=True,
            dismissable=True,
            color='success'
        )
    ]
)