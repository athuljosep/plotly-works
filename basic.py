from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='First Plotly Graph', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Dropdown(df.columns[3:], 'pop', id='dropdown-selection1'),
    dcc.Graph(id='graph-content'),
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value'),
    Input('dropdown-selection1', 'value')
)
def update_graph(value1,value2):
    dff = df[df.country==value1]
    return px.line(dff, x='year', y=value2)

if __name__ == '__main__':
    app.run(debug=True)
