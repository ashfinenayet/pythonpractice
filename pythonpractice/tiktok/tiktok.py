import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
app = dash.Dash(__name__)
colors = {
    'background': 'antiquewhite ',
    'text': 'black'
}
df = pd.read_excel('tiktok/modifiedtiktok.xlsx')


fig = px.scatter(df, x='danceability', y='energy',
                 color='popularity', hover_name="track_name", title='TikTok Trending Songs')
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app.layout = html.Div([
    html.P([
        "dropdown 1",
        dcc.Dropdown(id="song qualities",
        value=''
        )
    ]),
    dcc.Graph(
        id='tiktok-song',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
