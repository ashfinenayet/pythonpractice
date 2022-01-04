
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
app = dash.Dash(__name__)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('modified2.xlsx')

fig = px.histogram(df, x="Category", y="Amount", color = 'Category', title='Spending by Category',)
fig_2 = px.pie(df, values='Amount', names='Category',
               color='Category', title='Percentage of Spending', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0, 0, 0, 0)", "paper_bgcolor": "rgba(0, 0, 0, 0)"}
)
fig_2.update_traces(textposition='inside', textinfo='percent+label')
fig_3 = px.line(df, x='Date', y='Amount', title='Time Progession of Spending', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"})
fig_4 = px.box(df, x='Category', y='Amount', color='Category', title= 'boxplot graph', template="plotly_dark").update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"})

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
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
        id='bar',
        figure=fig
    ),

    dcc.Graph(
        id='pie_chart',
        figure=fig_2
    ),
    dcc.Graph(
        id='line_chart',
        figure=fig_3
    ),
    dcc.Graph(
        id='boxplot',
        figure=fig_4
    ),
    html.P(children='I have no idea why clothing shows up twice as separate categories',
           style={
               'textAlign': 'center',
               'color': colors['text']
           })

])

if __name__ == '__main__':
    app.run_server(debug=True)
