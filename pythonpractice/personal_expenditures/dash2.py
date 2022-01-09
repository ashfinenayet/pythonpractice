
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('personal_expenditures/modified2.xlsx')

fig = px.histogram(df, x="Category", y="Amount",
                   color='Category', title='Spending by Category',)
fig_2 = px.pie(df, values='Amount', names='Category',
               color='Category', title='Percentage of Spending', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"}
)
fig_2.update_traces(textposition='inside', textinfo='percent+label')
fig_3 = px.line(df, x='Date', y='Amount', title='Time Progession of Spending', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"})
fig_4 = px.box(df, x='Category', y='Amount', color='Category', title='boxplot graph', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_3.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_4.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
app = dash.Dash(__name__)
figures = ['fig', 'fig_2', 'fig_3', 'fig_4']
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Personal Expenditures in USD',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='''
        Multiple graphs of spending habits
    ''', style={
        'textAlign': 'center',
        'color': colors['text']
    }

    ),

    dcc.Graph(
        id='plot',
        
    ),
    dcc.Dropdown(
        id='variables',
        options=[{'label': i, 'value': i}for i in figures],
        value=figures[0]
    ),

    html.P(children='I have no idea why clothing shows up twice as separate categories',
           style={
               'textAlign': 'center',
               'color': colors['text']
           })

])
@app.callback(
    Output('plot', 'figure'),
    [Input('variables', 'value')])
def update_graph(fig_name):

    if fig_name == 'bar graph':
#         fig=go.Figure(go.Scatter(x=[1,2,3], y = [3,2,1]))
        return fig


    if fig_name == 'pie graph':
#         fig=go.Figure(go.Bar(x=[1,2,3], y = [3,2,1]))
        return fig_2
        
    if fig_name == 'line graph':
#         fig=go.Figure(go.Bar(x=[1,2,3], y = [3,2,1]))
        return fig_3
    if fig_name == 'box plot':
        return fig_4
        
# app.run_server(mode='external', debug=True)
app.run_server(debug=True,
           use_reloader=False # Turn off reloader if inside Jupyter
          )  