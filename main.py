#py -m pip install scikit-image
from dash import Dash, html
from source.components.layout import create_layout
import dash_bootstrap_components as dbc

def main():
    app = Dash(__name__)
    server = app.server
    app.title = "GFCC Database"
    app.layout = create_layout(app)
    server.run()

if __name__ == "__main__":
    main() 
