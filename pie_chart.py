import plotly.express as px
import pandas as pd
df = pd.read_excel('/Users/ashfi/Documents/R projects/activity.xlsx')
fig = px.pie(df, values='Amount', names='Category', title = 'Personal Expenditures')
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.write_html('Pie Chart', auto_open=True) 