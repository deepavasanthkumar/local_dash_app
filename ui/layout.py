from dash import html, dcc
from ui.header import header
from ui.tabs.iceberg_tab import iceberg_tab
from ui.tabs.postgres_tab import postgres_tab
from ui.tabs.analytics_tab import analytics_tab
from auth.sso import get_groups

def build_layout():
    groups = get_groups()

    tabs = [
        dcc.Tab(label="Iceberg", children=iceberg_tab()),
        dcc.Tab(label="Postgres", children=postgres_tab())
    ]

    if "admin" in groups:
        tabs.append(dcc.Tab(label="Analytics", children=analytics_tab()))

    return html.Div([
        header(),
        dcc.Tabs(tabs)
    ])
