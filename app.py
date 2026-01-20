
from dash import Dash
from auth.authorization import authorize
from ui.layout import build_layout

app = Dash(__name__, suppress_callback_exceptions=True)
server = app.server

@server.before_request
def secure():
    authorize()

app.layout = build_layout()

import ui.callbacks.iceberg_callbacks
import ui.callbacks.postgres_callbacks
import ui.callbacks.analytics_callbacks

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
