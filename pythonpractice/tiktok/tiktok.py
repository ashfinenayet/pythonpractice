import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)
colors = {"background": "antiquewhite ", "text": "black"}
df = pd.read_excel("tiktok/modifiedtiktok.xlsx")
df = df.rename(columns=dict(duration_mins="duration in minutes", liveness="liveliness"))
cols_dd = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "liveliness",
    "valence",
    "tempo",
    "duration in minutes",
]
# fig = px.scatter(df, x='danceability', y='energy',
#               color='popularity', hover_name="track_name", title='Tiktok Trending Songs', template='plotly_dark')
# fig.update_layout(
#   plot_bgcolor=colors['background'],
#    paper_bgcolor=colors['background'],
#    font_color=colors['text']
# )
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        dcc.Dropdown(
                            id="xaxis-column",
                            options=[{"label": k, "value": k} for k in cols_dd],
                            value=cols_dd[0],
                        ),
                    ],
                    style={"width": "48%", "display": "inline-block"},
                ),
                html.Div(
                    [
                        dcc.Dropdown(
                            id="yaxis-column",
                            options=[{"label": k, "value": k} for k in cols_dd],
                            value=cols_dd[0],
                        ),
                    ],
                    style={"width": "48%", "float": "right", "display": "inline-block"},
                ),
            ]
        ),
        dcc.Graph(id="indicator-graphic"),
    ]
)


@app.callback(
    Output("indicator-graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("yaxis-column", "value"),
)
def update_graph(
    xaxis_column_name,
    yaxis_column_name,
):

    fig = px.scatter(x=df[df['cols_dd'] == xaxis_column_name]['value'],
                     y=df[df['cols_dd'] == yaxis_column_name]['value'],
                     color='popularity',
                     hover_name='track_name')

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    

    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
