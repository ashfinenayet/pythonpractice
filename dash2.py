
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('/Users/ashfi/Documents/R projects/activity.xlsx')

fig = px.histogram(df, x="Category", y="Amount")
fig_2 = px.pie(df, values='Amount', names='Category', title='Percentage of Spending')
fig_2.update_traces(textposition = 'inside', textinfo='percent+label')
fig_3 = px.line(df, x='Date', y='Amount')
fig_4 = px.box(df, x = 'Category', y = 'Amount', color='Category')
app.layout = html.Div(children=[
    html.H1(children='Personal Expenditures in USD'),

    html.Div(children='''
        Multiple graphs of spending habits
    '''),

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
    html.P(children='I have no idea why clothing shows up twice as separate categories')
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
